def validate_project(data):

    errors = []

    required_columns = [
        "Project Name",
        "Client",
        "Location",
        "Start Date",
        "End Date"
    ]

    for column in required_columns:
        if column not in data.columns:
            errors.append(f"Missing column: {column}")

    return errors
