import re

# Password strength assessment tool

# Criteria weights
def calculate_strength(password):
    score = 0
    feedback = []

    # Length check
    length = len(password)
    if length < 8:
        feedback.append("Password is too short; minimum 8 characters.")
    elif length <= 12:
        score += 1
        feedback.append("Consider using more than 12 characters for better security.")
    else:
        score += 2

    # Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include digits (0-9).")

    # Special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append("Include special characters (e.g., !@#$%^&*).")

    # Determine strength category
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback, score

# User menu
def show_menu():
    print("\n=== Password Strength Checker ===")
    print("1. Check a password")
    print("2. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            pwd = input("Enter the password to check: ")
            strength, feedback, score = calculate_strength(pwd)
            print(f"\nPassword Strength: {strength} (Score: {score}/6)")
            if feedback:
                print("Feedback:")
                for comment in feedback:
                    print(f" - {comment}")
            else:
                print("Great job! Your password meets all criteria.")

        elif choice == '2':
            print("Exiting tool. Stay secure!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == '__main__':
    main()
