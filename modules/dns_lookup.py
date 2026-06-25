import dns.resolver


def get_dns_records(domain):

    results = {
        "A": [],
        "MX": [],
        "NS": []
    }

    try:
        answers = dns.resolver.resolve(domain, "A")

        for record in answers:
            results["A"].append(str(record))

    except:
        pass

    try:
        answers = dns.resolver.resolve(domain, "MX")

        for record in answers:
            results["MX"].append(str(record.exchange))

    except:
        pass

    try:
        answers = dns.resolver.resolve(domain, "NS")

        for record in answers:
            results["NS"].append(str(record))

    except:
        pass

    return results