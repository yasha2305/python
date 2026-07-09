import re

password = input("Enter Password: ")

score = 0

if len(password) >= 8:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"\d", password):
    score += 1

if re.search(r"[!@#$%^&*]", password):
    score += 1

levels = {
    1: "Very Weak",
    2: "Weak",
    3: "Medium",
    4: "Strong",
    5: "Very Strong"
}

print("Strength:", levels.get(score, "Very Weak"))