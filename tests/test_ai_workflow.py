"""
CivilFlow AI
Complete AI Workflow Test
"""

from app.ai.workflow import AIWorkflow


def main():

    company = {

        "company_name": "Lendlease Australia",

        "industry": "Construction",

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

        "employees": 12000,

        "location": "Australia",

        "digital_maturity": "High"
    }


    decision_maker = {

        "name": "Digital Engineering Manager",

        "role": "BIM / Digital Engineering"

    }


    workflow = AIWorkflow()


    result = workflow.run(
        company,
        decision_maker
    )


    print("=" * 70)

    print(
        "CIVILFLOW AI INTELLIGENCE REPORT"
    )

    print("=" * 70)



    # COMPANY SUMMARY

    print("\nCOMPANY SUMMARY")

    print("-" * 70)


    summary = result["summary"]


    for key, value in summary.items():

        print(
            f"{key}: {value}"
        )



    # REQUIREMENTS

    print("\n\nDETECTED REQUIREMENTS")

    print("-" * 70)


    requirements = result["requirements"]


    for item in requirements:

        print(
            f"- {item['requirement']} ({item['priority']})"
        )

        print(
            f"  Reason: {item['reason']}"
        )



    # SKILL RECOMMENDATIONS

    print("\n\nRECOMMENDED SERVICES & SKILLS")

    print("-" * 70)


    recommendations = result["recommendations"]


    for item in recommendations:

        print(
            f"\nRequirement: {item['requirement']}"
        )

        print(
            f"Service: {item['service']}"
        )

        print("Skills:")


        for skill in item["skills"]:

            print(
                f"  • {skill}"
            )



    # OPPORTUNITY SCORE

    print("\n\nOPPORTUNITY SCORE")

    print("-" * 70)


    score = result["score"]


    print(
        f"Score: {score['score']}/100"
    )


    print(
        f"Priority: {score['priority']}"
    )


    print("\nReasons:")


    for reason in score["reasons"]:

        print(
            f"- {reason}"
        )



    # EMAIL GENERATION

    print("\n\nAI COLD EMAIL DRAFT")

    print("-" * 70)


    email = result["email"]


    print("\nSubject:")

    print(
        email["subject"]
    )


    print("\nEmail:")

    print(
        email["email"]
    )


    print("\nFollow Up:")

    print(
        email["follow_up"]
    )


    print("\nOutreach Strategy:")

    print(
        email["strategy"]
    )



if __name__ == "__main__":

    main()