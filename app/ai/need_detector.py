"""
CivilFlow AI
Requirement Detection Engine
"""


class RequirementDetector:
    """
    Detects possible engineering requirements
    based on company research information.
    """

    def detect(self, company: dict) -> list:
        requirements = []

        technologies = [t.lower() for t in company.get("technology", [])]
        projects = [p.lower() for p in company.get("projects", [])]
        industry = company.get("industry", "").lower()
        digital = company.get("digital_maturity", "").lower()

        # BIM Detection
        if "bim" in technologies or "revit" in technologies:
            requirements.append({
                "requirement": "BIM Coordination Support",
                "priority": "High",
                "reason": "Company already uses BIM technologies."
            })

        # Civil 3D Detection
        if "infrastructure" in industry or "rail" in " ".join(projects):
            requirements.append({
                "requirement": "Civil 3D Drafting",
                "priority": "High",
                "reason": "Infrastructure projects require detailed civil documentation."
            })

        # Documentation
        if industry == "construction":
            requirements.append({
                "requirement": "Documentation Support",
                "priority": "Medium",
                "reason": "Construction companies require technical drawings and documentation."
            })

        # Quantity Takeoff
        if any(p in ["hospital", "hospitals", "commercial", "rail"] for p in projects):
            requirements.append({
                "requirement": "Quantity Takeoff",
                "priority": "Medium",
                "reason": "Large-scale projects require material estimation and BOQ preparation."
            })

        # Remote Engineering
        if digital == "high":
            requirements.append({
                "requirement": "Remote Engineering Support",
                "priority": "Medium",
                "reason": "High digital maturity enables remote collaboration."
            })

        return requirements