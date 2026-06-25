import requests

def detect_technology(domain):

    findings = []

    try:

        url = f"https://{domain}"

        response = requests.get(
            url,
            timeout=5,
            allow_redirects=True
        )

        headers = response.headers
        html = response.text.lower()

        server = headers.get("Server", "").lower()
        powered = headers.get("X-Powered-By", "").lower()

        # Server detection
        if "apache" in server:
            findings.append("Apache")

        if "nginx" in server:
            findings.append("Nginx")

        if "iis" in server:
            findings.append("Microsoft IIS")

        # Language detection
        if "php" in powered:
            findings.append("PHP")

        if "asp.net" in powered:
            findings.append("ASP.NET")

        # WordPress detection
        if "wp-content" in html:
            findings.append("WordPress")

        if "wp-includes" in html:
            findings.append("WordPress")

        # Bootstrap detection
        if "bootstrap" in html:
            findings.append("Bootstrap")

        # jQuery detection
        if "jquery" in html:
            findings.append("jQuery")

        # React detection
        if "__next" in html or "react" in html:
            findings.append("React/Next.js")

        findings = list(set(findings))

        if not findings:
            findings.append("Technology not detected")

    except Exception as e:

        findings.append(
            f"Error: {str(e)}"
        )

    return findings