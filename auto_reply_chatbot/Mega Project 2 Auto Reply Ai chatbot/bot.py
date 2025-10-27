import pyautogui
import time
import pyperclip
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ========================
# Load API KEY
# ========================
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("⚠️ GEMINI_API_KEY not found in .env file!")

# ========================
# Configure Gemini API
# ========================
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# Memory to avoid duplicate replies
last_replied = ""


def last_message_sender(chat_text):
    """ Get the sender name of the last message """
    lines = chat_text.strip().split("\n")
    last_line = lines[-1] if lines else ""
    if "]" in last_line:
        return last_line.split("]")[1].split(":")[0].strip()
    return ""


# Open Chrome Chat Window
pyautogui.click(1008, 1055)
time.sleep(1)

while True:
    time.sleep(5)

    # Select chat area (Adjust coords if needed)
    pyautogui.moveTo(672, 239)
    pyautogui.dragTo(1893, 941, duration=2.0, button="left")

    # Copy text
    pyautogui.hotkey("ctrl", "c")
    time.sleep(2)
    pyautogui.click(1994, 281)

    chat_history = pyperclip.paste()
    sender = last_message_sender(chat_history)

    print(f"Sender: {sender}")

    # Only reply if last message is from Rehan & not repeated
    if sender == "Rehan Qaari Saab" and chat_history != last_replied:

        last_replied = chat_history  # ✅ Update memory to prevent double responses

        prompt = f"""
You are Tony — a confident, ambitious Karachi guy with a sharp tongue and a hustler mindset.
You reply in Hinglish (Urdu + English mix), casual and natural.

Rules:
1️⃣ Output ONLY the next message — no names or timestamps.
2️⃣ Short, punchy, realistic — not robotic.
3️⃣ If they send “???” or repeatedly ask → witty roast.
4️⃣ Helpful when needed but with swagger.
5️⃣ Emojis only when it makes sense.

Chat history:
{chat_history}

Reply as Tony:
"""

        print("Generating Response...")
        response_text = model.generate_content(prompt).text.strip()

        pyperclip.copy(response_text)

        # Click chat bar and send message
        pyautogui.click(794, 984)
        time.sleep(1)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.press("enter")

        print("✅ Sent:", response_text)
