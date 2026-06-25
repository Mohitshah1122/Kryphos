import socket

COMMON_PORTS = [
    21,
    22,
    25,
    53,
    80,
    110,
    143,
    443,
    3306,
    3389
]

def scan_ports(host):

    results = []

    for port in COMMON_PORTS:

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(1)

            result = sock.connect_ex((host, port))

            if result == 0:

                results.append(port)

            sock.close()

        except:
            pass

    return results