"""
CivilFlow AI
Company Summary Generator
"""


class CompanySummaryGenerator:
    """
    Generates a professional company summary
    from researched company information.
    """

    def generate(self, company: dict) -> dict:
        company_name = company.get("company_name", "Unknown Company")
        industry = company.get("industry", "Unknown Industry")
        location = company.get("location", "Unknown Location")

        services = company.get("services", [])
        technology = company.get("technology", [])
        projects = company.get("projects", [])

        digital_maturity = company.get("digital_maturity", "Medium")

        return {
            "company": company_name,
            "industry": industry,
            "location": location,
            "company_profile": (
                f"{company_name} operates in the {industry} industry and "
                f"provides {', '.join(services)} services."
            ),
            "industry_position":
                "Established organisation with strong construction capabilities.",
            "construction_relevance":
                f"Actively involved in {', '.join(projects)} projects.",
            "digital_relevance":
                f"Uses {', '.join(technology)} with {digital_maturity} digital maturity.",
            "collaboration_opportunity":
                "Strong potential for BIM coordination, Civil 3D drafting, "
                "documentation support and remote engineering collaboration."
        }