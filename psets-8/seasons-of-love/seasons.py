from datetime import date
import re, sys
import inflect

p = inflect.engine()

def main():
    DoB = input("Date of Birth: ")
    try:
        year, month, day = check(DoB)
    except:
        sys.exit("Invalid Date")
    date_of_birth = date(int(year), int(month), int(day))
    today = date.today()
    diff = today - date_of_birth
    minutes = diff.days * 24 * 60
    display = f"{p.number_to_words(minutes, andword='').capitalize()} minutes"
    print(display)

def check(birth_date):
    pattern = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
    if re.search(pattern, birth_date):
        year, month, date = birth_date.split("-")
        return year, month,date

if __name__ == "__main__":
    main()
