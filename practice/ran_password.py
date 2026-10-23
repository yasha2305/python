import random
import string

chars = string.ascii_letters + string.digits + "@#$!"
password = ''.join(random.choices(chars, k=10))

print("Random Password:", password)