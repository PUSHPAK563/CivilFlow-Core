from app.research.research_manager import ResearchManager


def test_research_manager():

    company = "Lendlease Australia"

    manager = ResearchManager(company)

    profile = manager.generate_research_profile()

    print("\n===== COMPLETE RESEARCH PROFILE =====")

    print("Company:", profile["company"])

    print("\nWebsite Search:")
    print(profile["website_search"])

    print("\nDecision Maker Intelligence:")

    decision = profile["decision_maker"]

    print("Role:", decision["role"])
    print("Department:", decision["department"])
    print("Importance:", decision["importance"])


if __name__ == "__main__":
    test_research_manager()