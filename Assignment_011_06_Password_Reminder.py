
'''

Task : Let's say; you left a message in the past that prints a password you need. To see the password you wrote, you need to enter your name and the program should recognize you.
Write a program that 

Takes the first name from the user and compares it to yours,
Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! The password is : W@12",
If the name the user entered is not the same as yours, print out such as : "Hello, Amina! See you later."

'''


name_1 = str("crazy")
name_2 = str(input("Please enter your account name:"))
if name_1 == name_2:
  print("Hello, {acc_name}! The password is : W@12".format(acc_name=name_2))
else:
  print("Hello, {wrong_name}! See you later.".format(wrong_name=name_2)) 
