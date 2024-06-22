import datetime

def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def main():
    print("""
    ****************************************************
    *                                                  *
    *                Welcome to the                    *
    *               Age Calculator!                    *
    *                                                  *
    *   This simple tool will help you calculate your  *
    *   age based on your birthdate. Please enter your *
    *   birthdate in the format YYYY-MM-DD to proceed. *
    *                                                  *
    ****************************************************
    """)
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        age = calculate_age(birthdate)
        print(f"Your age is: {age} years old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
