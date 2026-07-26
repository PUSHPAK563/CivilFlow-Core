"""
CivilFlow AI
AI Cold Email Generator
"""


class EmailGenerator:
    """
    Generates personalised outreach messages
    based on company intelligence.
    """

    def generate(
        self,
        company: dict,
        requirements: list,
        score: dict,
        decision_maker: dict = None
    ) -> dict:

        company_name = company.get(
            "company_name",
            "your organisation"
        )

        industry = company.get(
            "industry",
            "construction"
        )

        contact_name = "Team"

        if decision_maker:
            contact_name = decision_maker.get(
                "name",
                "Team"
            )


        services = []

        for item in requirements:
            services.append(
                item.get("requirement", "")
            )


        subject = (
            f"BIM and Digital Engineering Support "
            f"Opportunity for {company_name}"
        )


        email = f"""
Hi {contact_name},

I hope you are doing well.

I came across {company_name}'s work in the
{industry} sector and noticed your involvement
in technology-driven construction projects.

Based on your current requirements, CivilFlow can
support your team with:

{chr(10).join("- " + s for s in services)}

Our focus is providing reliable remote engineering
support for BIM coordination, Civil 3D modelling,
and technical documentation.

I would appreciate the opportunity to discuss how
CivilFlow can support your upcoming projects.

Regards,
CivilFlow Team
"""


        follow_up = (
            f"Following up regarding BIM and digital "
            f"engineering support opportunities for "
            f"{company_name}."
        )


        strategy = {
            "priority": score.get(
                "priority",
                "Medium"
            ),
            "approach":
                "Highlight BIM capability and "
                "remote engineering support."
        }


        return {
            "subject": subject,
            "email": email.strip(),
            "follow_up": follow_up,
            "strategy": strategy
        }
    