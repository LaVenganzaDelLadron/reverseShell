import getopt
import os
import socket
import subprocess
import sys
import threading
from vidstream import ScreenShareClient, StreamingServer
import pyaudio

asciiArt = """

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

"""

# Global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0
stream = False
audio = False
current_dir = "/"

# For audio calling
CHUNK = 10*1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
BUFF_SIZE = 65536




def usage():
    print("\033[38;2;255;165;0mCODEGO TOOLS FOR KODIGO SA HANDS-ON NATO\033[0m")
    print("\033[38;2;255;165;0mUsage: codego.py -t target_host -p port\033[0m")
    print("\033[96m-l --listen                  - listen on [host]:[port] for incoming connections\033[0m")
    print("\033[96m-e --execute=file_to_run     - execute the given file upon receiving connections\033[0m")
    print("\033[96m-c --command                 - initialize a command shell\033[0m")
    print("\033[96m-u --upload=destination      - upon receiving connection upload a file and write to [destination]\033[0m")
    print("\033[96m-s --stream                  - start screen sharing\033[0m")
    print("\033[96m-a --audio			        - voice call\033[0m")
    print("\033[38;2;255;165;0mExamples:\033[0m")
    print("\033[96mpython3 codego.py -t 192.168.1.0 -p 4444 -l -c")
    print("\033[96mpython3 codego.py -l -p 4444 -c\033[0m")
    print("\033[96mpython3 codego.py -t 192.168.1.0 -p 4444 -l -u=/target/file.txt\033[0m")
    print("\033[96mecho 'hello' | python3 codego.py -t 192.168.1.0 -p 4444\033[0m")
    print("\033[96mpython3 codego.py -t 192.168.1.0 -p 4444 -e /bin/bash\033[0m")
    print("\033[96mpython3 codego.py -l -p 8080 -s\033[0m")
    print("\033[96mpython3 codego.py -t 127.0.0.1 -p 8080 -s\033[0m")
    print("\033[96mpython3 codego.py -l -p 4444 -a\033[0m")
    print("\033[96mpytohn3 codego.py -t 192.168.1.0 -p 4444 -a\033[0m")
    print("\033[31mpython3 codego.py -l -p 4444 -a")
    print("\033[31mpython3 codego.py -t 192.168.1.0 -p 4444 -a")
    print()
    print(f"\033[31m{asciiArt}\033[0m")


def main():
    global listen, port, execute, command, upload_destination, target, stream, audio

    if not len(sys.argv[1:]):
        usage()
        sys.exit(0)

    try:
        opts, _ = getopt.getopt(
            sys.argv[1:], "hle:t:p:cusa",
            ["help", "listen", "execute=", "target=", "port=", "command", "upload=", "stream", "audio"]
        )
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(1)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--command"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-s", "--stream"):
            stream = True
        elif o in ("-a", "--audio"):
            audio = True
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)

    if audio:
        print(f"\033[31m{asciiArt}\033[0m")
        start_calling()
        sys.exit(0)

    if stream:
        print(f"\033[31m{asciiArt}\033[0m")
        start_streaming()
        sys.exit(0)

    if not listen and target and port > 0:
        try:
            buffer = sys.stdin.read()
        except:
            buffer = ""
        print(f"\033[31m{asciiArt}\033[0m")
        client_sender(buffer)

    if listen:
        print(f"\033[31m{asciiArt}\033[0m")
        server_loop()




def receive_call():
    p = pyaudio.PyAudio()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    print(f"[+] Listening for audio connection on port {port}...")
    conn, addr = server_socket.accept()
    print(f"[+] Connected by {addr}")

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)

    try:
        while True:
            data = conn.recv(CHUNK)
            if not data:
                break
            stream.write(data)
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        conn.close()

def send_call():
    p = pyaudio.PyAudio()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target, port))
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

    try:
        while True:
            data = stream.read(CHUNK)
            client_socket.sendall(data)
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        client_socket.close()

def start_calling():
    if listen:
        threading.Thread(target=receive_call(), args=()).start()
        threading.Thread(target=send_call(), args=()).start()
    else:
        threading.Thread(target=send_call(), args=()).start()
        threading.Thread(target=receive_call(), args=()).start()



def start_streaming():
    if listen:
        receiver = StreamingServer('0.0.0.0', port)
        t = threading.Thread(target=receiver.start_server)
        t.start()
        print(f"[+] Screen share server started on port {port}.")

        while input("[*] Press 'q' to stop streaming...\n") != "q":
            pass

        receiver.stop_server()
        print("[+] Screen share server stopped.")
    else:
        sender = ScreenShareClient(target, port)
        t = threading.Thread(target=sender.start_stream)
        t.start()
        print(f"[+] Screen sharing to {target}:{port}...")

        while input("[*] Press 'q' to stop sharing...\n") != "q":
            pass

        sender.stop_stream()
        print("[+] Screen sharing stopped.")

def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(f"[>] Connecting to {target}:{port}")
        client.connect((target, port))
        print("[$] Connected")

        if buffer:
            client.send(buffer.encode())

        while True:
            response = b""
            while True:
                data = client.recv(4096)
                if not data:
                    break
                response += data
                if len(data) < 4096:
                    break

            if response:
                print(response.decode(), end="")

            try:
                buffer = input("")
            except EOFError:
                break

            buffer += "\n"
            client.send(buffer.encode())

    except Exception as e:
        print(f"[!] Exception during client send: {e}")
    finally:
        client.close()


def server_loop():
    global target

    if not target:
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((target, port))
    server.listen(5)
    print(f"[$] Listening on {target}:{port}...")

    while True:
        client_socket, addr = server.accept()
        print(f"[$] Accepted connection from {addr[0]}:{addr[1]}")
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()


def run_command(command):
    global current_dir
    command = command.rstrip()

    if command.startswith("cd "):
        path = command[3:].strip()
        if path == "..":
            current_dir = '/'.join(current_dir.rstrip('/').split('/')[:-1]) or '/'
        else:
            if path.startswith('/'):
                current_dir = path
            else:
                current_dir = current_dir.rstrip('/') + '/' + path
        return f"[+] Changed directory to {current_dir}\n".encode()

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, cwd=current_dir)
    except Exception as e:
        output = f"Failed to execute command.\r\n{e}\r\n".encode()
    return output


def client_handler(client_socket):
    global upload_destination, execute, command

    if upload_destination:
        file_buffer = b""

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file_buffer += data

        try:
            with open(upload_destination, "wb") as f:
                f.write(file_buffer)
            client_socket.send(f"Successfully saved file to {upload_destination}\r\n".encode())
        except:
            client_socket.send(f"Failed to save file to {upload_destination}\r\n".encode())

    if execute:
        output = run_command(execute)
        client_socket.send(output)

    if command:
        while True:
            try:
                client_socket.send(b"<Command:> ")
                cmd_buffer = ""
                while "\n" not in cmd_buffer:
                    data = client_socket.recv(1024).decode()
                    if not data:
                        break
                    cmd_buffer += data

                response = run_command(cmd_buffer)
                client_socket.send(response)
            except Exception as e:
                print(f"[!] Exception in command loop: {e}")
                break


if __name__ == "__main__":
    main()