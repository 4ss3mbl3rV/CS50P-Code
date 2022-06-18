from validator_collection import validators, checkers, errors

def main():
    print(validator_checker(input("What's your email address? ")))

def validator_checker(email):
    try:
        email_addr = validators.email(email)
        return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"
if __name__ == "__main__":
    main()
