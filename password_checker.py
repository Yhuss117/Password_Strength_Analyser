import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    return score, feedback


def main():
    print("=== Password Strength Analyzer ===")

    while True:
        password = input("\nEnter a password to evaluate (or type 'exit' to quit): ")

        if password.lower() == "exit":
            print("Exiting program.")
            break

        score, feedback = check_password_strength(password)

        if score <= 2:
            strength = "Weak"
        elif score == 3:
            strength = "Fair"
        elif score == 4:
            strength = "Good"
        else:
            strength = "Strong"

        print(f"\nPassword Strength: {strength}")

        if feedback:
            print("Suggestions:")
            for item in feedback:
                print(f"- {item}")
        else:
            print("Great job! Your password meets all security criteria.")
            
if __name__ == "__main__":
    main()