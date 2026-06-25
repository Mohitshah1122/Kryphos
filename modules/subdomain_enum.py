import socket

COMMON_SUBDOMAINS = [
    "www",
    "mail",
    "ftp",
    "blog",
    "api",
    "dev",
    "test",
    "admin",
    "portal",
    "vpn"
]

def enumerate_subdomains(domain):
    found = []

    for sub in COMMON_SUBDOMAINS:
        subdomain = f"{sub}.{domain}"

        try:
            socket.gethostbyname(subdomain)
            found.append(subdomain)

        except:
            pass

    return found