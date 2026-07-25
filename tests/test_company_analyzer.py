from app.ai.company_analyzer import CompanyAnalyzer

company = {
    "company_name": "Lendlease Australia",
    "industry": "Construction",
    "services": [
        "Construction",
        "Infrastructure",
        "Property",
    ],
    "technology": [
        "BIM",
        "Revit",
        "Digital Engineering",
    ],
    "projects": [
        "Hospitals",
        "Rail",
        "Commercial",
    ],
    "employees": 12000,
    "location": "Australia",
}

analyzer = CompanyAnalyzer(company)

report = analyzer.analyse()

print("\n===== COMPANY ANALYSIS =====")
print(f"Company: {report.company_name}")
print(f"Overview: {report.overview}")
print(f"Industry: {report.industry_analysis}")
print(f"Market Position: {report.market_position}")
print(f"Technology: {report.technology_maturity}")
print(f"Services: {report.service_profile}")