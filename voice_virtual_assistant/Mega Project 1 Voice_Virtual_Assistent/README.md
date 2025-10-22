# Jarvis Virtual Assistant

A Python-based virtual assistant that can perform various tasks through voice commands, including web browsing, playing music, fetching news, and providing AI-powered responses using Google's Gemini model.

## Features

- 🗣️ Voice Command Recognition
- 🔊 Text-to-Speech Output
- 🌐 Web Browsing Commands
- 📰 News Updates
- 🤖 AI-Powered Responses (using Gemini 2.5 Flash)
- 🎵 Music Playback Control

## Prerequisites

Before running this project, you'll need:

### Required Software
- Python 3.8 or higher
- pip (Python package installer)

### API Keys
- News API Key (from [newsapi.org](https://newsapi.org))
- Google Gemini API Key

### Required Python Packages
```
speech_recognition
pyttsx3
requests
google-generativeai
webbrowser
```

## Installation

1. Clone or download this repository to your local machine.

2. Create a virtual environment (recommended):
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows PowerShell:
.\.venv\Scripts\Activate.ps1
```

3. Install required packages:
```powershell
pip install speech_recognition pyttsx3 requests google-generativeai
```

4. Update API Keys:
   - Open `main.py`
   - Replace the existing API keys with your own:
     ```python
     news_api_key = "your_news_api_key_here"
     genai.configure(api_key="your_gemini_api_key_here")
     ```

## Usage

1. Run the assistant:
```powershell
python main.py
```

2. Available Commands:
   - "Open Google" - Opens Google in your default web browser
   - "Get news" - Fetches and reads the latest news
   - Ask any question - Gets an AI-powered response using Gemini

## Voice Engine Configuration

The assistant uses different speech engines based on your operating system:
- Windows: 'sapi5'
- macOS: 'nsss'
- Linux: 'espeak'

Current configuration in the code uses 'sapi5' for Windows. If you're using a different OS, modify the `speak` function accordingly:
```python
engine = pyttsx3.init(driverName='sapi5')  # Change to 'nsss' for Mac or 'espeak' for Linux
```

## Troubleshooting

### Common Issues:

1. **Microphone not working:**
   - Ensure your microphone is properly connected
   - Check if it's set as the default input device
   - Verify microphone permissions for Python

2. **API Key Errors:**
   - Verify your API keys are correctly entered
   - Check if you have remaining API quota
   - Ensure internet connectivity

3. **Package Installation Issues:**
   - Try upgrading pip: `python -m pip install --upgrade pip`
   - Install packages individually if batch install fails
   - Check Python version compatibility

### Error Messages:

If you see:
- "Error talking to Gemini": Check your Gemini API key and internet connection
- "No microphone found": Verify your microphone setup
- "API key invalid": Double-check your News API key

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. You can also open issues for bugs or feature requests.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Code with Harry for the project tutorial and inspiration
- OpenAI and Google for AI capabilities
- NewsAPI for news integration