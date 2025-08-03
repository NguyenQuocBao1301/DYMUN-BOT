class Country:
    def __init__(self, name, budget, eo, mo, asat):
        self.name = name
        self.budget = budget
        self.eo = eo
        self.mo = mo
        self.asat = asat

def main():
    # Define fixed abbreviations for each country
    abbr = {
        "Pakistan": "pk",
        "Japan": "jp",
        "Canada": "ca",
        "France": "fr",
        "Russia": "ru",
        "United States": "us",
        "China": "cn",
        "India": "in",
        "Germany": "de",
        "Italy": "it",
        "North Korea": "kp",
        "Iran": "ir",
        "Testland": "test"
    }

    with open("log/country_data_1753419339.txt", "r") as f:
        lines = f.readlines()

    print("countries = {")
    for line in lines:
        if not line.strip():
            continue
        parts = line.strip().split()
        name = " ".join(parts[:-4])
        try:
            budget = int(float(parts[-4]))
        except ValueError:
            print(f"# Error parsing budget for: {line.strip()}")
            continue
        eo = int(parts[-3])
        mo = int(parts[-2])
        asat = int(parts[-1])
        code = abbr.get(name)
        if code:
            print(f'    "{code}": Country("{name}", {budget:_}, {eo}, {mo}, {asat}),')
        else:
            print(f"# Warning: No abbreviation for '{name}'")
    print("}")

if __name__ == "__main__":
    main()
