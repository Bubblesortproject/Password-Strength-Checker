import re
import random
import string

def generate_passkey(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()?"
    return ''.join(random.choice(chars) for _ in range(length))

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


print("=== Password Security System ===")
password = input("Enter your password: ")

strength, feedback = check_password_strength(password)

print(f"\nPassword Strength: {strength}")

if feedback:
    print("Suggestions:")
    for item in feedback:
        print("-", item)

    print("\nSuggested Secure Passkey:", generate_passkey())

print("\nEnable Biometric Security:")
print("1. Face ID")
print("2. Fingerprint")
choice = input("Choose option (1/2): ")

if choice == "1":
    print("Face ID Enabled Successfully (Demo Mode)")
elif choice == "2":
    print("Fingerprint Enabled Successfully (Demo Mode)")
else:
    print("No biometric option selected.")
