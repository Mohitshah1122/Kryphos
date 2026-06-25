import os
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors


# -----------------------------
# Footer Function
# -----------------------------

def add_page_number(canvas, doc):

    canvas.saveState()

    canvas.setFont(
        "Helvetica",
        8
    )

    canvas.drawString(
        40,
        20,
        "Kryphos Security Assessment Report | Confidential"
    )

    canvas.drawRightString(
        550,
        20,
        f"Page {doc.page}"
    )

    canvas.restoreState()



# -----------------------------
# Risk Calculation
# -----------------------------

def calculate_risk(risks):

    if len(risks) == 0:
        return "LOW"

    elif len(risks) <= 2:
        return "MEDIUM"

    elif len(risks) <= 5:
        return "HIGH"

    else:
        return "CRITICAL"



# -----------------------------
# Main Report Generator
# -----------------------------

def generate_report(
        domain,
        subdomains,
        ports,
        technologies,
        risks
):


    # Create reports directory

    os.makedirs(
        "reports",
        exist_ok=True
    )


    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    filename = (
        f"reports/Kryphos_{domain}_{timestamp}.pdf"
    )


    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=50,
        bottomMargin=50
    )


    styles = getSampleStyleSheet()



    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=26,
        spaceAfter=20
    )


    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Heading2"],
        alignment=TA_CENTER,
        fontSize=14
    )


    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10
    )


    normal_style = styles["BodyText"]



    content = []



    # ==================================
    # COVER PAGE
    # ==================================


    content.append(
        Spacer(1,80)
    )


    content.append(
        Paragraph(
            "KRYPHOS",
            title_style
        )
    )


    content.append(
        Paragraph(
            "Cyber Asset Intelligence & Attack Surface Management Platform",
            subtitle_style
        )
    )


    content.append(
        Spacer(1,50)
    )


    cover_data = [

        [
            "Document Type",
            "Security Assessment Report"
        ],

        [
            "Target",
            domain
        ],

        [
            "Assessment Type",
            "External Reconnaissance"
        ],

        [
            "Generated",
            str(datetime.now())
        ],

        [
            "Classification",
            "Confidential"
        ]

    ]


    cover_table = Table(
        cover_data,
        colWidths=[150,250]
    )


    cover_table.setStyle(
        TableStyle([

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.grey
            ),

            (
                "VALIGN",
                (0,0),
                (-1,-1),
                "MIDDLE"
            )

        ])
    )


    content.append(
        cover_table
    )


    content.append(
        PageBreak()
    )



    # ==================================
    # EXECUTIVE SUMMARY
    # ==================================


    risk_level = calculate_risk(risks)


    content.append(
        Paragraph(
            "1. Executive Summary",
            heading_style
        )
    )


    summary = f"""

    Kryphos performed automated external reconnaissance
    against <b>{domain}</b>.

    The assessment identified:

    <br/>
    • Subdomains discovered: {len(subdomains)}

    <br/>
    • Open ports identified: {len(ports)}

    <br/>
    • Technologies detected: {len(technologies)}

    <br/>
    • Security findings: {len(risks)}

    <br/><br/>

    Overall Risk Rating:
    <b>{risk_level}</b>

    """


    content.append(
        Paragraph(
            summary,
            normal_style
        )
    )



    # ==================================
    # TARGET INFORMATION
    # ==================================


    content.append(
        Paragraph(
            "2. Target Information",
            heading_style
        )
    )


    target_table = Table(

        [
            [
                "Domain",
                domain
            ],

            [
                "Framework",
                "Kryphos"
            ],

            [
                "Methodology",
                "Black Box Reconnaissance"
            ]

        ],

        colWidths=[150,250]

    )


    target_table.setStyle(
        TableStyle([

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.grey
            )

        ])
    )


    content.append(
        target_table
    )



    # ==================================
    # SUBDOMAINS
    # ==================================


    content.append(
        Paragraph(
            "3. Attack Surface Discovery",
            heading_style
        )
    )


    sub_data = [
        [
            "No",
            "Subdomain"
        ]
    ]


    for index, sub in enumerate(subdomains,1):

        sub_data.append(
            [
                index,
                sub
            ]
        )


    table = Table(
        sub_data
    )


    table.setStyle(
        TableStyle([

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.grey
            )

        ])
    )


    content.append(table)



    # ==================================
    # PORTS
    # ==================================


    content.append(
        Paragraph(
            "4. Network Exposure Analysis",
            heading_style
        )
    )


    port_data = [

        [
            "Port",
            "Service",
            "Status"
        ]

    ]


    for port in ports:

        service = "HTTPS" if str(port)=="443" else "HTTP"

        port_data.append(
            [
                str(port),
                service,
                "Open"
            ]
        )


    port_table = Table(
        port_data
    )


    port_table.setStyle(
        TableStyle([

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.grey
            )

        ])
    )


    content.append(
        port_table
    )



    # ==================================
    # TECHNOLOGY
    # ==================================


    content.append(
        Paragraph(
            "5. Technology Fingerprinting",
            heading_style
        )
    )


    for tech in technologies:

        content.append(
            Paragraph(
                "• " + tech,
                normal_style
            )
        )



    # ==================================
    # FINDINGS
    # ==================================


    content.append(
        Paragraph(
            "6. Security Findings",
            heading_style
        )
    )


    finding_id = 1


    for severity, finding in risks:


        finding_text = f"""

        <b>Finding ID:</b> KRY-{finding_id:03}

        <br/>

        <b>Severity:</b> {severity}

        <br/>

        <b>Issue:</b> {finding}

        <br/>

        <b>Recommendation:</b>
        Review and implement appropriate security controls.

        """


        content.append(
            Paragraph(
                finding_text,
                normal_style
            )
        )


        content.append(
            Spacer(1,15)
        )


        finding_id += 1



    # ==================================
    # CONCLUSION
    # ==================================


    content.append(
        Paragraph(
            "7. Conclusion",
            heading_style
        )
    )


    conclusion = """

    Kryphos successfully completed attack surface
    discovery and identified security observations.
    The findings should be reviewed and remediated
    according to organizational security policies.

    """


    content.append(
        Paragraph(
            conclusion,
            normal_style
        )
    )



    doc.build(
        content,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )


    return filename