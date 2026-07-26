from app.ai.need_detector import RequirementDetector


def main():
    company = {
        "company_name": "Lendlease Australia",
        "industry": "Construction",
        "technology": [
            "BIM",
            "Revit",
            "Digital Engineering"
        ],
        "projects": [
            "Hospitals",
            "Rail",
            "Commercial"
        ],
        "digital_maturity": "High"
    }

    detector = RequirementDetector()
    requirements = detector.detect(company)

    print("=" * 60)
    print("REQUIREMENT DETECTION REPORT")
    print("=" * 60)

    for index, item in enumerate(requirements, start=1):
        print(f"\n{index}. {item['requirement']}")
        print(f"Priority : {item['priority']}")
        print(f"Reason   : {item['reason']}")


if __name__ == "__main__":
    main()