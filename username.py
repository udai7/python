username = input("Enter your Username:")

character= len(username )
digit= username.isdigit()


if character >= 7:
 print("Not a valid username too many characters")
elif not username.find(" ") == -1:
 print("Not a valid username contains space")
elif not username.isdigit() == True:
 print("Not a valid username contains numbers")
elif digit:
 print("Not a valid username contains digits")
else:
 print("Valid username")