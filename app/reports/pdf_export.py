from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def export_pdf(company, result, filename="Company_Report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "CivilFlow AI Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))


    content.append(
        Paragraph(
            f"Company: {company['company_name']}",
            styles["Heading2"]
        )
    )


    content.append(
        Paragraph(
            str(result["summary"]),
            styles["BodyText"]
        )
    )


    content.append(
        Paragraph(
            "Requirements",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            str(result["requirements"]),
            styles["BodyText"]
        )
    )


    content.append(
        Paragraph(
            "Opportunity Score",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            str(result["score"]),
            styles["BodyText"]
        )
    )


    content.append(
        Paragraph(
            "Email Draft",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            str(result["email"]),
            styles["BodyText"]
        )
    )


    doc.build(content)