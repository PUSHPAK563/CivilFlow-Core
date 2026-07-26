"""
CivilFlow AI
Opportunity Scoring Engine
"""


class OpportunityScorer:
    """
    Calculates company opportunity score
    based on AI analysis.
    """

    def calculate(self, company: dict, requirements: list) -> dict:

        score = 0
        reasons = []

        industry = company.get("industry", "").lower()
        technology = [
            t.lower()
            for t in company.get("technology", [])
        ]

        projects = [
            p.lower()
            for p in company.get("projects", [])
        ]

        digital = company.get(
            "digital_maturity",
            ""
        ).lower()


        # Industry Match
        if "construction" in industry:
            score += 20
            reasons.append(
                "Construction industry alignment"
            )


        # BIM Adoption
        if "bim" in technology or "revit" in technology:
            score += 25
            reasons.append(
                "Strong BIM technology adoption"
            )


        # Infrastructure Projects
        if (
            "rail" in " ".join(projects)
            or "infrastructure" in industry
        ):
            score += 20
            reasons.append(
                "Large infrastructure project activity"
            )


        # Digital Maturity
        if digital == "high":
            score += 15
            reasons.append(
                "High digital engineering maturity"
            )


        # Service Match
        if len(requirements) >= 3:
            score += 20
            reasons.append(
                "Multiple CivilFlow service opportunities detected"
            )


        # Classification

        if score >= 85:
            priority = "Hot Lead"

        elif score >= 70:
            priority = "High Potential"

        elif score >= 50:
            priority = "Medium"

        else:
            priority = "Low"


        return {
            "score": score,
            "priority": priority,
            "reasons": reasons
        }