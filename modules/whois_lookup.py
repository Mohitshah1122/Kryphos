import whois

def format_date(date_value):

    if isinstance(date_value, list):
        return str(date_value[0])

    return str(date_value)


def get_whois_info(domain):

    results = {}

    try:

        w = whois.whois(domain)

        results["domain_name"] = str(w.domain_name)
        results["registrar"] = str(w.registrar)

        results["creation_date"] = format_date(w.creation_date)
        results["expiration_date"] = format_date(w.expiration_date)
        results["updated_date"] = format_date(w.updated_date)

    except Exception as e:

        results["error"] = str(e)

    return results