def classify_risk(headers, ports, ssl_data):

    findings = []

    # Header checks

    for header, status in headers.items():

        if status == "Missing":

            if header == "Content-Security-Policy":

                findings.append(
                    ("Medium", f"{header} Missing")
                )

            else:

                findings.append(
                    ("Low", f"{header} Missing")
                )

    # Port checks

    if 3389 in ports:

        findings.append(
            ("High", "RDP Port 3389 Open")
        )

    if 22 in ports:

        findings.append(
            ("Medium", "SSH Port 22 Open")
        )

    if 21 in ports:

        findings.append(
            ("Medium", "FTP Port 21 Open")
        )

    # SSL checks

    try:

        days = int(
            ssl_data.get(
                "days_remaining",
                999
            )
        )

        if days < 30:

            findings.append(
                (
                    "High",
                    "SSL Certificate Expiring Soon"
                )
            )

    except:
        pass

    if not findings:

        findings.append(
            (
                "Low",
                "No major risks detected"
            )
        )

    return findings