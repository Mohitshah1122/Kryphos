from flask import Flask, render_template, request

from modules.subdomain_enum import enumerate_subdomains
from modules.dns_lookup import get_dns_records
from modules.whois_lookup import get_whois_info
from modules.port_scanner import scan_ports
from modules.banner_grabber import grab_banner
from modules.header_analyzer import analyze_headers
from modules.ssl_checker import get_ssl_info
from modules.tech_fingerprint import detect_technology
from modules.risk_engine import classify_risk
from modules.pdf_report import generate_report

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    subdomains = []
    dns_records = {}
    whois_data = {}
    ports = []
    banners = {}
    headers = {}
    ssl_data = {}
    technologies = []
    risks = []

    if request.method == "POST":

        domain = request.form["domain"]

        subdomains = enumerate_subdomains(domain)

        dns_records = get_dns_records(domain)

        whois_data = get_whois_info(domain)

        ports = scan_ports(domain)

        for port in ports:
            banners[port] = grab_banner(
                domain,
                port
            )

        headers = analyze_headers(domain)

        ssl_data = get_ssl_info(domain)

        technologies = detect_technology(domain)

        risks = classify_risk(
            headers,
            ports,
            ssl_data
        )

        generate_report(
            domain,
            subdomains,
            ports,
            technologies,
            risks
        )

    return render_template(
        "index.html",
        subdomains=subdomains,
        dns_records=dns_records,
        whois_data=whois_data,
        ports=ports,
        banners=banners,
        headers=headers,
        ssl_data=ssl_data,
        technologies=technologies,
        risks=risks
    )

if __name__ == "__main__":
    app.run(debug=True)