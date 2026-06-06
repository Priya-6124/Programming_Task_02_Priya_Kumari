username = "admin"
password = "pass123"

input_user = input("Enter Username: ")
input_pass = input("Enter Password: ")

if input_user == username and input_pass == password:
    print("Login Successful")
else:
    print("Invalid Credentials")
