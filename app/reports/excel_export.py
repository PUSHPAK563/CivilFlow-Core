from openpyxl import Workbook


def export_excel(company, result, filename="CivilFlow_Leads.xlsx"):

    workbook = Workbook()

    sheet = workbook.active
    sheet.title = "Leads"


    sheet.append(
        [
            "Company",
            "Industry",
            "Score",
            "Priority",
            "Contact",
            "Status"
        ]
    )


    sheet.append(
        [
            company["company_name"],
            company["industry"],
            result["score"]["score"],
            result["score"]["priority"],
            "Digital Engineering Manager",
            "New"
        ]
    )


    workbook.save(filename)
    