from app.research.decision_maker import DecisionMakerIntel


def test_decision_maker():

    company = "Lendlease Australia"

    intel = DecisionMakerIntel(company)

    profile = intel.create_profile()

    print("\n===== DECISION MAKER INTELLIGENCE =====")

    print("Company:", profile["company"])
    print("Name:", profile["name"])
    print("Role:", profile["role"])
    print("Department:", profile["department"])
    print("LinkedIn:", profile["linkedin"])
    print("Importance:", profile["importance"])


if __name__ == "__main__":
    test_decision_maker()