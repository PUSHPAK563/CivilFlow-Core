from excel.importer import load_excel
from validation.validator import validate_project
from research.company_search import search_company


def main():

    file_path = "data/sample/project.xlsx"

    # Step 1: Load Excel
    project_data = load_excel(file_path)

    # Step 2: Validate Data
    errors = validate_project(project_data)

    # Step 3: Display Result
    if errors:
        print("Validation Failed:")
        for error in errors:
            print("-", error)
    else:
        print("Validation Successful!")
        print("Project data is ready.")

        # Day 3 - Research Engine
        company = input("\nEnter company name to research: ")
        search_company(company)


if __name__ == "__main__":
    main()