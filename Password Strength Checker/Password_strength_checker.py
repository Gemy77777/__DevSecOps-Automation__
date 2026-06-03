import string
password = input("Enter your password: ")   
if len(password) < 8 or len(password) > 32:
    print("Error: Password must be between 8 and 32 characters long.")
    print("Strength Level: WEAK")
elif any(c.isspace() for c in password):
    print("Error: Password must not contain spaces.")
    print("Strength Level: WEAK")
elif password.lower() in ["password", "123456", "12345678", "qwerty", "abc123"]:
    print("Error: Password is too common / blacklisted.")
    print("Strength Level: WEAK")
else:
    has_lowercase = any(c in string.ascii_lowercase for c in password)
    has_uppercase = any(c in string.ascii_uppercase for c in password)
    has_digit     = any(c in string.digits for c in password)
    has_symbol    = any(not c.isalnum() for c in password)

    if not has_lowercase: print("-> Feedback: Consider adding a lowercase letter [a-z].")
    if not has_uppercase: print("-> Feedback: Consider adding an uppercase letter [A-Z].")
    if not has_digit:     print("-> Feedback: Consider adding a number [0-9].")
    if not has_symbol:    print("-> Feedback: Consider adding a special character / symbol.")
    
    criteria_score = sum([has_lowercase, has_uppercase, has_digit, has_symbol])
    print("\n")
    if criteria_score == 4:
        print("Valid password.")
        print("Strength Level: STRONG and SECURE")
    elif criteria_score == 3:
        print("Valid password.")
        print("Strength Level: MEDIUM")
    else:
        print("Strength Level: WEAK")