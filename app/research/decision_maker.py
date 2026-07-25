class DecisionMakerIntel:

    def __init__(self, company_name):
        self.company_name = company_name

    def create_profile(self):
        decision_maker = {
            "company": self.company_name,
            "name": "To be collected",
            "role": "Digital Engineering Manager",
            "department": "BIM / Digital Engineering",
            "linkedin": "To be collected",
            "importance": "High"
        }

        return decision_maker