# Auto Reply Chatbot (Python)

This project is a simple automation bot that reads chat content from a browser window and automatically replies using Google Gemini (Generative AI). It's implemented in Python and uses OS-level automation (mouse/keyboard) to copy the chat history, generate a response via Gemini, and paste/send the reply.

## Features

- Monitors a chat window (Chrome) by selecting text with mouse drag and reading the clipboard.
- Uses Google Generative AI (Gemini) to craft context-aware replies.
- Keeps a small in-memory memory to avoid duplicate replies.
- Personas and response style defined via a prompt (example: Tony — a Karachi hustler in Hinglish).

## Requirements

- Python 3.8+ (recommend 3.10 or 3.11)
- A Google Gemini API key (stored in `.env` as `GEMINI_API_KEY`).
- Packages (install with pip):
  - pyautogui
  - pyperclip
  - python-dotenv
  - google-generativeai

You can install dependencies with:

```powershell
python -m pip install -r requirements.txt
```

If you don't have `requirements.txt`, install directly:

```powershell
python -m pip install pyautogui pyperclip python-dotenv google-generativeai
```

Note: On Windows, `pyautogui` may require additional packages for screenshots/automation and permissions; see the PyAutoGUI docs if you run into issues.

## Files

- `bot.py` — main automation script that monitors chat and replies.
- `bot_1.py` / `main.py` — additional project files (present in workspace). See repository for details.
- `.gitignore` — files to ignore (created by this project).

## Configuration

Create a `.env` file in the project root with your Gemini API key:

```
GEMINI_API_KEY=your_real_api_key_here
```

Keep `.env` private and never commit it — `.gitignore` in this repo already excludes it.

## How to run (Windows PowerShell)

1. Open PowerShell in the project directory.
2. Ensure dependencies are installed.
3. Add your API key to `.env`.
4. Start the bot:

```powershell
python bot.py
```

Before running, make sure Chrome (or the chat window) is visible and at the expected resolution/position, because the bot uses fixed screen coordinates to click/drag. You may need to update coordinates in `bot.py` to match your screen.

## bot.py — logic and explanation

This section walks through the high-level logic implemented in `bot.py` (fully included in the repository). The script uses OS-level automation — be careful while running because it will move your mouse and send keyboard events.

1) Load environment and configure Gemini

- The script loads environment variables using `python-dotenv` and reads `GEMINI_API_KEY` from the `.env` file.
- It configures the Google generative API client via `google.generativeai` and selects a model (for example `gemini-2.5-flash`).

2) Utilities

- `last_message_sender(chat_text)` — a simple helper that extracts the sender name from the last line of the copied chat text. It assumes chat lines are of the form `[time] Sender: message` or similar. The function splits the last line at `]` then at `:` to find the sender's name. This is simple parsing and might need adjustments for different chat formats.

3) UI automation and main loop

- The script uses `pyautogui` to:
  - Click to focus Chrome chat window (initial `pyautogui.click(1008, 1055)`).
  - Enter a loop (sleep 5s each iteration) where it:
    - Moves the mouse to the chat region and drags to select the chat text (example coordinates `672, 239` to `1893, 941`).
    - Copies the selected text with `ctrl+c`, waits briefly and reads the clipboard using `pyperclip.paste()`.
    - Parses the last sender using `last_message_sender`.
    - If the last sender matches the target name (example `Rehan Qaari Saab`) and the chat history differs from the last replied message (avoid duplicates), it creates a prompt and asks Gemini to generate a reply.
    - The generated reply is copied to the clipboard, then pasted into the chat input (click coordinates `794, 984`) and submitted with `enter`.

4) Prompting and persona

- The script builds a multi-line prompt that instructs Gemini to reply as a persona called "Tony" in Hinglish. The prompt includes rules (short, punchy, no metadata) and inserts the chat history so the model has context.

5) Simple memory

- `last_replied` stores the last chat text the bot replied to (in memory only) and prevents repeated replies to the same content. This is ephemeral and resets when the script restarts.

## Important notes, safety & troubleshooting

- Automation coordinates: The script uses fixed screen coordinates. If your screen resolution or window placement differs, update the coordinates in `bot.py`:
  - The initial click to focus the browser.
  - The drag coordinates used to select chat text.
  - The coordinates for the chat input box where the bot clicks before pasting.

- Be mindful that while `pyautogui` is running, it will take control of the mouse and keyboard. Keep a way to stop the script (Alt+Tab away and move the mouse or use Ctrl+C in the terminal to stop execution).

- API usage & costs: Calls to Gemini may incur usage charges depending on your Google Cloud / Gemini billing arrangement. Monitor usage and quotas.

- Parsing chat text: The `last_message_sender` function uses a basic heuristic for parsing. If your chat format differs, update the parsing logic accordingly.

## Suggested small improvements (next steps)

- Persist memory to disk to avoid replying again after restarts (e.g., JSON store of recent message IDs).
- Use OCR for chats that cannot be selected/copied.
- Replace fixed coordinates with a small calibration routine or image recognition (e.g., `pyautogui.locateOnScreen`) to find chat regions dynamically.

## License

This README is provided as part of the project. Apply your preferred license if you plan to publish this repo.

---

If you'd like, I can also:
- Add a `requirements.txt` file with pinned versions.
- Add a small calibration helper to capture and store correct coordinates for your screen.

Happy to continue — tell me if you want a `requirements.txt` or a coordinates calibration script next.
