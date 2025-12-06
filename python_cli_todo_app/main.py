#!/usr/bin/env python3
"""
todo_rich.py — In-memory Rich-based CLI Todo App
All todos exist only in RAM. Nothing is saved to disk.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()
DATE_FMT = "%Y-%m-%d %H:%M:%S"


# --------------------------------------------------------------------
# Data Models (In Memory Only)
# --------------------------------------------------------------------
@dataclass
class TodoItem:
    id: int
    title: str
    note: str = ""
    done: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().strftime(DATE_FMT))
    completed_at: Optional[str] = None
    tags: List[str] = field(default_factory=list)


class InMemoryTodoStore:
    def __init__(self):
        self.todos: List[TodoItem] = []

    def all(self):
        return self.todos

    def add(self, title: str, note="", tags=None):
        next_id = max([t.id for t in self.todos], default=0) + 1
        item = TodoItem(id=next_id, title=title, note=note, tags=tags or [])
        self.todos.append(item)
        return item

    def find(self, ident: int):
        return next((t for t in self.todos if t.id == ident), None)

    def update(self, ident: int, **kwargs):
        t = self.find(ident)
        if not t:
            return None
        for k, v in kwargs.items():
            if hasattr(t, k):
                setattr(t, k, v)
        if kwargs.get("done") is True:
            t.completed_at = datetime.now().strftime(DATE_FMT)
        if kwargs.get("done") is False:
            t.completed_at = None
        return t

    def delete(self, ident: int):
        before = len(self.todos)
        self.todos = [t for t in self.todos if t.id != ident]
        return len(self.todos) < before

    def clear(self):
        self.todos = []

    def search(self, query: str):
        q = query.lower()
        return [
            t for t in self.todos
            if q in t.title.lower()
            or q in t.note.lower()
            or any(q in tag.lower() for tag in t.tags)
        ]


# --------------------------------------------------------------------
# UI Helpers
# --------------------------------------------------------------------
def render_header():
    header = Text("✨ Rich Todo CLI (In-Memory)", style="bold white on blue")
    sub = Text("\nAll tasks are temporary — nothing is saved.", style="dim")
    console.print(Panel(header + sub, expand=True, box=box.ROUNDED))


def render_table(items: List[TodoItem]):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Done")
    table.add_column("Title")
    table.add_column("Tags")
    table.add_column("Created", style="dim")
    table.add_column("Completed", style="dim")

    for t in items:
        mark = "[green]✔[/green]" if t.done else "[yellow]●[/yellow]"
        title = Text(t.title)
        if t.done:
            title.stylize("strike dim")
        tags = ", ".join(t.tags)
        table.add_row(
            str(t.id), mark, title, tags, t.created_at, t.completed_at or "-"
        )

    console.print(table)


def prompt_add(store: InMemoryTodoStore):
    title = Prompt.ask("Title").strip()
    if not title:
        console.print("[red]Title cannot be empty.[/red]")
        return

    note = Prompt.ask("Note", default="")
    tags_raw = Prompt.ask("Tags (comma separated)", default="")
    tags = [t.strip() for t in tags_raw.split(",")] if tags_raw else []

    item = store.add(title=title, note=note, tags=tags)
    console.print(f"[green]Added:[/green] #{item.id} {item.title}")


def show_help():
    console.print(Panel("""
Commands:
  add               Add new todo (interactive)
  list              List todos
  done <id>         Mark as done
  undone <id>       Mark as not done
  edit <id>         Edit the todo
  delete <id>       Delete todo
  clear             Delete all todos
  search <query>    Search todos
  exit              Quit app
""", title="Help", box=box.ROUNDED))


# --------------------------------------------------------------------
# Command Handler
# --------------------------------------------------------------------
def handle_command(store, parts):
    if not parts:
        return

    cmd = parts[0].lower()
    args = parts[1:]

    if cmd == "add":
        prompt_add(store)

    elif cmd == "list":
        items = store.all()
        if not items:
            console.print("[dim]No todos yet.[/dim]")
        else:
            render_table(items)

    elif cmd in ("done", "undone"):
        if not args:
            console.print("[red]Provide an ID.[/red]")
            return

        try:
            ident = int(args[0])
        except:
            console.print("[red]ID must be a number.[/red]")
            return

        t = store.update(ident, done=(cmd == "done"))
        if t:
            console.print(f"[green]Updated:[/green] #{ident}")
        else:
            console.print("[red]Todo not found.[/red]")

    elif cmd == "edit":
        if not args:
            console.print("[red]Provide an ID.[/red]")
            return

        ident = int(args[0])
        t = store.find(ident)
        if not t:
            console.print("[red]Not found.[/red]")
            return

        console.print(Panel(f"Editing #{t.id}", title="Edit"))
        new_title = Prompt.ask("Title", default=t.title)
        new_note = Prompt.ask("Note", default=t.note)
        tags_raw = Prompt.ask("Tags", default=",".join(t.tags))
        tags = [x.strip() for x in tags_raw.split(",")] if tags_raw else []

        store.update(ident, title=new_title, note=new_note, tags=tags)
        console.print("[green]Updated[/green]")

    elif cmd == "delete":
        if not args:
            console.print("[red]ID missing[/red]")
            return

        ident = int(args[0])
        if store.delete(ident):
            console.print("[green]Deleted[/green]")
        else:
            console.print("[red]Not found[/red]")

    elif cmd == "clear":
        if Confirm.ask("Clear all todos?"):
            store.clear()
            console.print("[green]All cleared[/green]")

    elif cmd == "search":
        if not args:
            console.print("[red]Provide a query[/red]")
            return
        q = " ".join(args)
        results = store.search(q)
        render_table(results)

    elif cmd in ("exit", "quit"):
        console.print("[bold]Bye![/bold]")
        raise SystemExit

    elif cmd == "help":
        show_help()

    else:
        console.print("[red]Unknown command.[/red]")


# --------------------------------------------------------------------
# Main REPL
# --------------------------------------------------------------------
def main():
    store = InMemoryTodoStore()
    render_header()

    while True:
        try:
            cmd = Prompt.ask("[bold green]todo[/bold green]").strip()
            handle_command(store, cmd.split())
        except KeyboardInterrupt:
            console.print()
            if Confirm.ask("Exit?"):
                break
        except SystemExit:
            break


if __name__ == "__main__":
    main()
