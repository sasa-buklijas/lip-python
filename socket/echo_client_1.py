import socket
import time


def main():
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        time.sleep(5)
        data = s.recv(1024)
        #s.close()   # even with close, still TIME-WAIT persist for some time

    print(f"Received {data!r}")


if __name__ == "__main__":
    main()