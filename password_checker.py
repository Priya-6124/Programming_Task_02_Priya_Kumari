password = input("Enter Password: ")

has_upper = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.isdigit():
        has_digit = True

if len(password) < 8:
    print("Weak Password")

elif has_upper and has_digit:
    print("Strong Password")

else:
    print("Moderate Password")
