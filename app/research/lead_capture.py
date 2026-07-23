from pathlib import Path


LEADS_FILE = Path("leads.txt")


def add_lead(name, business, city, need):
    lead = f"{name} | {business} | {city} | {need}\n"

    with LEADS_FILE.open("a", encoding="utf-8") as file:
        file.write(lead)

    print("\nLead saved successfully.")


def show_leads():
    if not LEADS_FILE.exists():
        print("\nNo leads saved yet.")
        return

    print("\n--- CivilFlow LEAD: Saved Leads ---")
    print(LEADS_FILE.read_text(encoding="utf-8"))


def main():
    print("Welcome to CivilFlow LEAD")

    name = input("Lead name: ").strip()
    business = input("Business name: ").strip()
    city = input("City: ").strip()
    need = input("What does the lead need? ").strip()

    add_lead(name, business, city, need)
    show_leads()


if __name__ == "__main__":
    main()