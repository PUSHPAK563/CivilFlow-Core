from app.ai.email_generator import EmailGenerator


def main():

    company = {
        "company_name": "Lendlease Australia",
        "industry": "Construction"
    }


    requirements = [
        {
            "requirement":
            "BIM Coordination Support"
        },
        {
            "requirement":
            "Civil 3D Drafting"
        }
    ]


    score = {
        "score": 100,
        "priority": "Hot Lead"
    }


    generator = EmailGenerator()

    result = generator.generate(
        company,
        requirements,
        score
    )


    print("="*60)
    print("AI EMAIL DRAFT")
    print("="*60)

    print("\nSubject:")
    print(result["subject"])

    print("\nEmail:")
    print(result["email"])

    print("\nFollow Up:")
    print(result["follow_up"])

    print("\nStrategy:")
    print(result["strategy"])


if __name__ == "__main__":
    main()