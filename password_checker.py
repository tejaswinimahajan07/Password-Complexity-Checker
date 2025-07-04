import re

def check_password_strength(password):
    strength = 0
    suggestions = []

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add uppercase letters (A-Z)")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add lowercase letters (a-z)")

    # Number Check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("Include numbers (0-9)")

    # Special Character Check
    if re.search(r"[\W_]", password):
        strength += 1
    else:
        suggestions.append("Include special characters (!@#$%^&*)")

    # Feedback
    if strength == 5:
        status = "Very Strong"
    elif strength == 4:
        status = "Strong"
    elif strength == 3:
        status = "Medium"
    elif strength == 2:
        status = "Weak"
    else:
        status = "Very Weak"

    return strength, status, suggestions


def main():
    print("\n🔐 Password Strength Checker with Suggestions 🔐\n")
    password = input("Enter your password: ")

    strength, status, tips = check_password_strength(password)

    print(f"\nStrength: {strength}/5")
    print(f"Rating: {status}")

    if tips:
        print("\nSuggestions to improve your password:")
        for tip in tips:
            print(f" - {tip}")
    else:
        print("\nGreat! Your password is strong and meets all criteria.")

if __name__ == "__main__":
    main()