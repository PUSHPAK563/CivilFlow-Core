import webbrowser


def search_company(company_name):
    """
    Opens a Google search for the company's official website.
    """
    query = f"{company_name} official website"
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

    print(f"\nSearching for: {company_name}")
    print(url)

    webbrowser.open(url)

    return url