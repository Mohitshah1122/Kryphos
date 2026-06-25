import ssl
import socket
from datetime import datetime

def get_ssl_info(domain):

    results = {}

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (domain, 443),
            timeout=5
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=domain
            ) as secure_sock:

                cert = secure_sock.getpeercert()

        results["issuer"] = str(
            cert.get("issuer")
        )

        results["subject"] = str(
            cert.get("subject")
        )

        results["version"] = str(
            cert.get("version")
        )

        results["serial_number"] = str(
            cert.get("serialNumber")
        )

        expiry = cert.get("notAfter")

        results["expiry_date"] = expiry

        expiry_date = datetime.strptime(
            expiry,
            "%b %d %H:%M:%S %Y %Z"
        )

        days_left = (
            expiry_date - datetime.utcnow()
        ).days

        results["days_remaining"] = str(
            days_left
        )

    except Exception as e:

        results["error"] = str(e)

    return results