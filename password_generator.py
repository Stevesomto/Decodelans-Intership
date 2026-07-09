import secrets, string

length = 12

selected_characters = input("Create a password with the following character types (lowercase, uppercase, digits, punctuation): ").split(',')

characters = {
    'lowercase': string.ascii_lowercase,
    'uppercase': string.ascii_uppercase,
    'digits': string.digits,
    'punctuation': string.punctuation
}

def generate_password(length=length, use_lowercase=True, use_uppercase=True, use_digits=True, use_punctuation=True):
    if not any([use_lowercase, use_uppercase, use_digits, use_punctuation]):
        raise ValueError("At least one character type must be selected.")

    selected_characters = ''
    if use_lowercase:
        selected_characters += characters['lowercase']
    if use_uppercase:
        selected_characters += characters['uppercase']
    if use_digits:
        selected_characters += characters['digits']
    if use_punctuation:
        selected_characters += characters['punctuation']

    password = ''.join(secrets.choice(selected_characters) for _ in range(length))
    return password

print("Generated password:", generate_password())