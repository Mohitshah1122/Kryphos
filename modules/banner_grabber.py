import socket

def grab_banner(host, port):

    try:

        sock = socket.socket()

        sock.settimeout(2)

        sock.connect((host, port))

        banner = sock.recv(1024)

        sock.close()

        return banner.decode(
            errors="ignore"
        )

    except:

        return "Banner not available"