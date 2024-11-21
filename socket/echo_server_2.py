import socket


def main():
    HOST = "127.0.0.1"  # only local connection enabled
    #HOST = "0.0.0.0"    # outside connection enabled
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # allows a single server process to reuse the port quickly after it has been closed, 
        # especially if it is stuck in the TIME_WAIT state
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # (Linux Only): The SO_REUSEPORT, multiple server processes can listen on the same port, 
        # and the kernel will distribute incoming connections among them.
        # This is often used for load balancing.
        # but both(or multiple) processes must be started with SO_REUSEPORT
        ###s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        s.bind((HOST, PORT))
        s.listen()
        while True: # accept forever, otherwise only one
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    print(f'{data} from {addr}')
                    if not data:
                        break
                    conn.sendall(data)


if __name__ == "__main__":
    main()