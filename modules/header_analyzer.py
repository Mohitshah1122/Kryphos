import requests

def analyze_headers(domain):

    results = {}

    try:

        url = f"https://{domain}"

        response = requests.get(
            url,
            timeout=5,
            allow_redirects=True
        )

        headers = response.headers

        security_headers = {

            "Strict-Transport-Security":
                headers.get(
                    "Strict-Transport-Security"
                ),

            "Content-Security-Policy":
                headers.get(
                    "Content-Security-Policy"
                ),

            "X-Frame-Options":
                headers.get(
                    "X-Frame-Options"
                ),

            "X-XSS-Protection":
                headers.get(
                    "X-XSS-Protection"
                ),

            "X-Content-Type-Options":
                headers.get(
                    "X-Content-Type-Options"
                )

        }

        for header, value in security_headers.items():

            if value:

                results[header] = "Present"

            else:

                results[header] = "Missing"

    except Exception as e:

        results["Error"] = str(e)

    return results