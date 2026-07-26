"""
CivilFlow AI
Complete AI Intelligence Workflow
"""

from app.ai.company_summary import CompanySummaryGenerator
from app.ai.need_detector import RequirementDetector
from app.ai.skill_recommender import SkillRecommender
from app.ai.opportunity_score import OpportunityScorer
from app.ai.email_generator import EmailGenerator


class AIWorkflow:
    """
    Controls the complete CivilFlow AI pipeline.
    """

    def __init__(self):

        self.summary_generator = CompanySummaryGenerator()

        self.requirement_detector = RequirementDetector()

        self.skill_recommender = SkillRecommender()

        self.opportunity_scorer = OpportunityScorer()

        self.email_generator = EmailGenerator()


    def run(
        self,
        company: dict,
        decision_maker: dict = None
    ) -> dict:
        """
        Execute complete AI analysis.

        Flow:

        Company Data
              ↓
        Summary
              ↓
        Requirements
              ↓
        Skills
              ↓
        Opportunity Score
              ↓
        Email Draft
        """


        # Company Summary

        summary = self.summary_generator.generate(
            company
        )


        # Requirement Detection

        requirements = self.requirement_detector.detect(
            company
        )


        # Skill Recommendation

        recommendations = self.skill_recommender.recommend(
            requirements
        )


        # Opportunity Score

        score = self.opportunity_scorer.calculate(
            company,
            requirements
        )


        # Email Generation

        email = self.email_generator.generate(
            company,
            requirements,
            score,
            decision_maker
        )


        return {

            "summary": summary,

            "requirements": requirements,

            "recommendations": recommendations,

            "score": score,

            "email": email

        }
    