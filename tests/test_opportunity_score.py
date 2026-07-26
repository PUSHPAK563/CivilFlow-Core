from app.ai.opportunity_score import OpportunityScorer


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


    requirements = [
        {
            "requirement":
            "BIM Coordination Support"
        },
        {
            "requirement":
            "Civil 3D Drafting"
        },
        {
            "requirement":
            "Documentation Support"
        }
    ]


    scorer = OpportunityScorer()

    result = scorer.calculate(
        company,
        requirements
    )


    print("="*60)
    print("OPPORTUNITY SCORE REPORT")
    print("="*60)

    print(
        f"Score: {result['score']}/100"
    )

    print(
        f"Priority: {result['priority']}"
    )

    print("\nReasons:")

    for reason in result["reasons"]:
        print("-", reason)


if __name__ == "__main__":
    main()