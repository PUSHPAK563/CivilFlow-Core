"""
CivilFlow AI
AI Workflow Integration
"""

from app.ai.company_summary import CompanySummaryGenerator
from app.ai.need_detector import RequirementDetector
from app.ai.skill_recommender import SkillRecommender


class AIWorkflow:
    """
    Coordinates the AI Intelligence Engine.
    """

    def __init__(self):
        self.summary_generator = CompanySummaryGenerator()
        self.requirement_detector = RequirementDetector()
        self.skill_recommender = SkillRecommender()

    def run(self, company: dict) -> dict:
        """
        Execute the complete AI workflow.

        Parameters:
            company (dict)

        Returns:
            dict
        """

        summary = self.summary_generator.generate(company)

        requirements = self.requirement_detector.detect(company)

        recommendations = self.skill_recommender.recommend(requirements)

        return {
            "summary": summary,
            "requirements": requirements,
            "recommendations": recommendations
        }