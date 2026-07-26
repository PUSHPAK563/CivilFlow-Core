from app.ai.company_summary import CompanySummaryGenerator


def main():
    # Sample company data (simulates output from the Research Engine)
    company = {
        "company_name": "Lendlease Australia",
        "industry": "Construction",
        "location": "Australia",
        "services": [
            "Construction",
            "Infrastructure",
            "Property Development"
        ],
        "technology": [
            "BIM",
            "Revit",
            "Digital Engineering"
        ],
        "projects": [
            "Hospitals",
            "Rail",
            "Commercial Buildings"
        ],
        "digital_maturity": "High"
    }

    generator = CompanySummaryGenerator()
    summary = generator.generate(company)

    print("=" * 60)
    print("COMPANY SUMMARY")
    print("=" * 60)

    for key, value in summary.items():
        print(f"{key}:")
        print(f"  {value}")
        print()


if __name__ == "__main__":
    main()
    