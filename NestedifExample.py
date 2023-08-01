user=input("Enter the username:")
password=input("Enter the password:")

if user=='python':
    if password=='welcome':
        print("Login Success")
    else:
        print("Invalid password")
else:
    print("Invalid Username")
