from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QMessageBox,
    QProgressBar,
)

from app.ai.workflow import AIWorkflow

from app.reports.pdf_export import export_pdf
from app.reports.excel_export import export_excel


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.workflow = AIWorkflow()

        # Store latest analysis
        self.latest_company = None
        self.latest_result = None


        layout = QVBoxLayout()


        heading = QLabel("Company Analysis Dashboard")
        heading.setStyleSheet(
            "font-size:20px; font-weight:bold;"
        )


        self.company_input = QLineEdit()
        self.company_input.setPlaceholderText(
            "Enter Company Name"
        )


        self.analyze_button = QPushButton(
            "Analyze Company"
        )

        self.analyze_button.clicked.connect(
            self.run_analysis
        )


        self.status = QLabel(
            "Status: Ready"
        )


        self.progress = QProgressBar()

        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.setValue(0)



        self.results = QTextEdit()
        self.results.setReadOnly(True)



        # Export Buttons

        self.pdf_button = QPushButton(
            "Export PDF"
        )

        self.excel_button = QPushButton(
            "Export Excel"
        )


        self.pdf_button.clicked.connect(
            self.export_pdf_report
        )


        self.excel_button.clicked.connect(
            self.export_excel_report
        )



        # Add widgets

        layout.addWidget(heading)

        layout.addWidget(
            self.company_input
        )

        layout.addWidget(
            self.analyze_button
        )

        layout.addWidget(
            self.status
        )

        layout.addWidget(
            self.progress
        )

        layout.addWidget(
            self.results
        )


        layout.addWidget(
            self.pdf_button
        )

        layout.addWidget(
            self.excel_button
        )


        self.setLayout(layout)



    def run_analysis(self):

        company_name = (
            self.company_input.text()
            .strip()
        )


        if not company_name:

            QMessageBox.warning(
                self,
                "Input Required",
                "Please enter a company name."
            )

            return



        self.progress.setValue(10)

        self.status.setText(
            "Status: Researching Company..."
        )



        company = {

            "company_name": company_name,

            "industry": "Construction",

            "services": [
                "Construction",
                "Infrastructure"
            ],

            "technology": [
                "BIM",
                "Revit"
            ],

            "projects": [
                "Commercial",
                "Hospitals"
            ],

            "employees": 12000,

            "location": "Australia"

        }



        self.progress.setValue(40)


        self.status.setText(
            "Status: AI Processing..."
        )



        result = self.workflow.run(
            company
        )


        # Save latest data

        self.latest_company = company

        self.latest_result = result



        self.progress.setValue(80)



        output = f"""

==============================
COMPANY SUMMARY
==============================

{result['summary']}


==============================
REQUIREMENTS
==============================

{result['requirements']}


==============================
RECOMMENDED SKILLS
==============================

{result['recommendations']}


==============================
OPPORTUNITY SCORE
==============================

{result['score']}


==============================
EMAIL DRAFT
==============================

{result['email']}

"""


        self.results.setPlainText(
            output
        )


        self.progress.setValue(
            100
        )


        self.status.setText(
            "Status: Analysis Complete"
        )




    def export_pdf_report(self):

        if not self.latest_result:

            QMessageBox.warning(
                self,
                "No Report",
                "Please analyse a company first."
            )

            return



        export_pdf(
            self.latest_company,
            self.latest_result
        )


        QMessageBox.information(
            self,
            "Success",
            "PDF Report Generated Successfully"
        )




    def export_excel_report(self):

        if not self.latest_result:

            QMessageBox.warning(
                self,
                "No Report",
                "Please analyse a company first."
            )

            return



        export_excel(
            self.latest_company,
            self.latest_result
        )


        QMessageBox.information(
            self,
            "Success",
            "Excel Report Generated Successfully"
        )