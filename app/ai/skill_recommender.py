"""
CivilFlow AI
Skill Recommendation Engine
"""


class SkillRecommender:
    """
    Maps detected company requirements
    to CivilFlow services and engineering skills.
    """

    def recommend(self, requirements: list) -> list:

        recommendations = []

        skill_map = {

            "BIM Coordination Support": {
                "service": "BIM Coordination",
                "skills": [
                    "Autodesk Revit",
                    "Navisworks",
                    "Clash Detection",
                    "BIM Execution Planning"
                ]
            },

            "Civil 3D Drafting": {
                "service": "Civil Infrastructure Drafting",
                "skills": [
                    "AutoCAD Civil 3D",
                    "Surface Modelling",
                    "Corridor Design",
                    "Infrastructure Documentation"
                ]
            },

            "Documentation Support": {
                "service": "Technical Documentation",
                "skills": [
                    "AutoCAD",
                    "CAD Standards",
                    "Drawing Preparation",
                    "Technical Documentation"
                ]
            },

            "Quantity Takeoff": {
                "service": "Quantity Estimation",
                "skills": [
                    "BOQ Preparation",
                    "Quantity Surveying",
                    "Microsoft Excel",
                    "Material Estimation"
                ]
            },

            "Remote Engineering Support": {
                "service": "Remote Engineering Services",
                "skills": [
                    "BIM Collaboration",
                    "Cloud Coordination",
                    "Project Communication",
                    "Digital Engineering"
                ]
            }
        }

        for item in requirements:

            requirement = item["requirement"]

            if requirement in skill_map:

                recommendations.append({

                    "requirement": requirement,

                    "service": skill_map[requirement]["service"],

                    "skills": skill_map[requirement]["skills"]

                })

        return recommendations