from app.ai.skill_recommender import SkillRecommender


def main():

    requirements = [

        {"requirement": "BIM Coordination Support"},

        {"requirement": "Civil 3D Drafting"},

        {"requirement": "Documentation Support"},

        {"requirement": "Quantity Takeoff"},

        {"requirement": "Remote Engineering Support"}

    ]

    recommender = SkillRecommender()

    recommendations = recommender.recommend(requirements)

    print("=" * 60)
    print("SKILL RECOMMENDATION REPORT")
    print("=" * 60)

    for item in recommendations:

        print(f"\nRequirement : {item['requirement']}")
        print(f"Service     : {item['service']}")
        print("Skills:")

        for skill in item["skills"]:
            print(f"  - {skill}")


if __name__ == "__main__":
    main()