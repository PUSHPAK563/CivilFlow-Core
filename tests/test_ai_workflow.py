from app.ai.workflow import AIWorkflow


def main():
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

    workflow = AIWorkflow()
    report = workflow.run(company)

    print("=" * 70)
    print("CIVILFLOW AI INTELLIGENCE REPORT")
    print("=" * 70)

    print("\nCOMPANY SUMMARY")
    print("-" * 70)
    for key, value in report["summary"].items():
        print(f"{key}: {value}")

    print("\nDETECTED REQUIREMENTS")
    print("-" * 70)
    for req in report["requirements"]:
        print(f"- {req['requirement']} ({req['priority']})")
        print(f"  Reason: {req['reason']}")

    print("\nRECOMMENDED SERVICES & SKILLS")
    print("-" * 70)
    for rec in report["recommendations"]:
        print(f"\nRequirement: {rec['requirement']}")
        print(f"Service: {rec['service']}")
        print("Skills:")
        for skill in rec["skills"]:
            print(f"  • {skill}")


if __name__ == "__main__":
    main()