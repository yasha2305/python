import random
import string

def generate_password(length=12):
    if length < 6:
        return "Password length should be at least 6"

    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure password has at least one of each
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill remaining length
    all_chars = lower + upper + digits + special
    password += random.choices(all_chars, k=length - 4)

    # Shuffle password
    random.shuffle(password)

    return ''.join(password)

def check_strength(password):
    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if len(password) >= 12:
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

# Main
length = int(input("Enter password length: "))
pwd = generate_password(length)

print("Generated Password:", pwd)
print("Strength:", check_strength(pwd))