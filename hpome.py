import secrets
import string

class PasswordGenerator:
    def __init__(self, length=16, use_upper=True, use_digits=True, use_special=True):
        self.length = length
        self.use_upper = use_upper
        self.use_digits = use_digits
        self.use_special = use_special
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase if use_upper else ''
        self.digits = string.digits if use_digits else ''
        self.special = string.punctuation if use_special else ''
        self.all_chars = self.lowercase + self.uppercase + self.digits + self.special

    def generate(self):
        if not self.all_chars:
            return None

        password = []
        if self.use_upper:
            password.append(secrets.choice(self.uppercase))
        if self.use_digits:
            password.append(secrets.choice(self.digits))
        if self.use_special:
            password.append(secrets.choice(self.special))

        while len(password) < self.length:
            password.append(secrets.choice(self.all_chars))

        secrets.SystemRandom().shuffle(password)
        return ''.join(password)

def password_strength(pwd):
    score = 0
    length = len(pwd)
    
    if length >= 12:
        score += 1
    if any(c.islower() for c in pwd):
        score += 1
    if any(c.isupper() for c in pwd):
        score += 1
    if any(c.isdigit() for c in pwd):
        score += 1
    if any(c in string.punctuation for c in pwd):
        score += 1

    return {
        5: "Very Strong 💪",
        4: "Strong 👍",
        3: "Good 🙂",
        2: "Weak ⚠️",
        1: "Very Weak ❌",
        0: "Useless ❌"
    }[score]

# Generate + Evaluate
gen = PasswordGenerator(length=18, use_upper=True, use_digits=True, use_special=True)
password = gen.generate()
strength = password_strength(password)

print(password)
print(strength)
