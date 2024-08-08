import string


def check_pass(pswd):
    password_length = len(pswd)

    if password_length < 8:
        print("Password is too short, should be at least 8 characters long.")
    elif not any(c.isupper() for c in pswd):
        print("Password should include at least one uppercase letter.")
    elif not any(c.islower() for c in pswd):
        print("Password should include at least one lowercase letter.")
    elif not any(c in string.punctuation for c in pswd):
        print("Password should include at least one special character.")
    elif not any(c.isdigit() for c in pswd):
        print("Password should include at least one number.")
    else:
        print("Strong Password!")


def main():
    password = input("Enter your password: ")
    check_pass(password)


if __name__ == "__main__":
    main()
