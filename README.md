# Discord Bot Spammer

![image](https://github.com/user-attachments/assets/683835ff-ad97-46c9-b867-2572f1de07a2)


A Python Discord bot that supports multiple bot tokens running simultaneously.  
It features commands for sending spam messages to users and channels with rate limit control and a stylish CLI interface.

---

## Features

- Supports multiple Discord bot tokens loaded from `tokens.txt`
- Async command loop for interactive command input:
  - `crash-user`: Send a message spam to a specific user by user ID
  - `crash-channel`: Spam a channel with repeated messages until stopped
- Colored terminal output using `pystyle`
- Rate limit friendly with delay control
- Command line interface with a nice ASCII art header

---

## Requirements

- Python 3.8+
- `discord.py` library (`pip install discord.py`)
- `pystyle` library (`pip install pystyle`)

---

## Setup

1. Clone this repository or download the script.
2. Paste your Discord bot tokens in `tokens.txt`, one token per line.
3. Run the script:
   ```bash
   python main.py
