User_A= int(input("Enter the first digit:"))
User_B= int(input("Enter the second digit:"))
N= User_A + User_B
print(N)

if(N==7):
    print("Special Number")

elif(N%7==0):
    print("Special Number")

elif(User_A==7 or User_B==7):
    print("Special Number")

else:
    print("Normal Number")



