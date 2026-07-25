"""
CivilFlow AI - Company Analyzer

This module analyses a researched company profile and generates
high-level business intelligence for use by the AI Intelligence Engine.

Author: Pushpak Nandurkar
Project: CivilFlow AI
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class CompanyAnalysis:
    """
    Stores the results of company analysis.
    """
    company_name: str
    overview: str
    industry_analysis: str
    market_position: str
    technology_maturity: str
    service_profile: str


class CompanyAnalyzer:
    """
    Analyses structured company information and generates
    a business summary.
    """

    def __init__(self, company_data: Dict):
        self.company = company_data

    def generate_overview(self) -> str:
        """Generate a brief company overview."""

        name = self.company.get("company_name", "Unknown Company")
        industry = self.company.get("industry", "Unknown Industry")
        location = self.company.get("location", "Unknown Location")

        return (
            f"{name} operates in the {industry} industry "
            f"with operations based in {location}."
        )

    def industry_analysis(self) -> str:
        """Analyse the company's industry."""

        industry = self.company.get("industry", "").lower()

        if industry == "construction":
            return (
                "The company operates in a highly competitive construction "
                "sector where digital engineering, BIM, planning, and "
                "project collaboration are becoming industry standards."
            )

        return (
            "Industry-specific analysis is currently unavailable."
        )

    def market_position(self) -> str:
        """Estimate market position."""

        employees = self.company.get("employees", 0)

        if employees >= 10000:
            return "Global Industry Leader"

        if employees >= 3000:
            return "Large Enterprise"

        if employees >= 500:
            return "Growing Company"

        return "Small or Medium Enterprise"

    def technology_maturity(self) -> str:
        """Evaluate technology adoption."""

        technologies: List[str] = self.company.get("technology", [])

        if len(technologies) >= 5:
            return "Advanced Digital Engineering"

        if len(technologies) >= 3:
            return "Digitally Mature"

        if len(technologies) >= 1:
            return "Moderate Technology Adoption"

        return "Traditional Workflow"

    def service_profile(self) -> str:
        """Summarise services."""

        services = self.company.get("services", [])

        if not services:
            return "Service information unavailable."

        return ", ".join(services)

    def analyse(self) -> CompanyAnalysis:
        """
        Execute complete company analysis.
        """

        return CompanyAnalysis(
            company_name=self.company.get("company_name", "Unknown"),
            overview=self.generate_overview(),
            industry_analysis=self.industry_analysis(),
            market_position=self.market_position(),
            technology_maturity=self.technology_maturity(),
            service_profile=self.service_profile(),
        )