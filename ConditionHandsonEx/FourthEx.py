PlayerA = int(input("Enter the score of A"))
PlayerB = int(input("Enter the score of B"))
Sum = PlayerA + PlayerB

if (PlayerA >300 or PlayerB >300 and Sum<500):
    print("Can team up")

else:
    print("Cannot team up")


