'''

Task : Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.

A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a Q-keyboard and use of the ten-fingers standard).
The word will always be a string consisting of only letters from a to z.
Write a program which returns True if it's a comfortable word or False otherwise.


Given word		Desired Output (explanation)
tester			False (uses only left-hand fingers)*
polly			False (uses only right-hand fingers)*
clarusway		True (uses both hand fingers)*

'''


set_left = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'}
set_right = {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'}

word = str(input("Please enter a word: "))
word_set = set(word)
print(word_set)
A = word_set.issubset (set_left)
B = word_set.issubset(set_right)
# print(A)
# print(B)
if (A == True) and (B==False) :
  print("Your word is NOT a comfortable word.")
elif (A == False) and (B==True) : 
  print("Your word is NOT a comfortable word.")
elif (A == True) and (B==True) : 
  print("Your word is a comfortable word.")
else:
  print("Your word is  a comfortable word.")
