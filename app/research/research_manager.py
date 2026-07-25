from app.research.company_search import search_company
from app.research.decision_maker import DecisionMakerIntel


class ResearchManager:

    def __init__(self, company_name):
        self.company_name = company_name

    def generate_research_profile(self):

        website_search = search_company(self.company_name)

        decision_maker = DecisionMakerIntel(
            self.company_name
        )

        decision_profile = decision_maker.create_profile()

        research_profile = {
            "company": self.company_name,
            "website_search": website_search,
            "decision_maker": decision_profile
        }

        return research_profile
    