'''
Problem :

Task : Estimating the risk of death from coronavirus.

Consider the following questions in terms of True/False regarding anyone else.

Are you a cigarette addict older than 75 years old? Variable → age

Do you have a severe chronic disease? Variable → chronic

Is your immune system too weak? Variable → immune

Set a logical algorithm using boolean logic operators (and/or) and the given variables in order to give us True (there is a risk of death) or False (there is not a risk of death) as a result.
'''
'''
age =  # can be assigned only True/False
chronic =  # can be assigned only True/False
immune =  # can be assigned only True/False
risk = ? (True or False)
'''


# 3-Assignment - 010/03 (Covid - 19 Risk)



is_older_than_75 = True

have_chronic_disease = True

is_immune_weak = True

risk = (is_immune_weak or have_chronic_disease) and is_older_than_75 

print(risk)

if risk == True  :

     print("There is a risk of death")

else : 

     print("There is not a risk of death" )


# Second Solution

print("Please Answer The Question 'Yes' or 'No'")

age = str.lower(input("Are you a cigarette addict older than 75 years old? :"))

if age == "yes":

    age = True

else:

    age = False 



chronic = str.lower(input("Do you have a severe chronic disease? : ")) 

if chronic == "yes":

    chronic = True

else:

    chronic = False



immune = str.lower(input("Is your immune system too weak? : ")) 

if immune == "yes":

    immune = True

else:

    immune = False



risk = (age and chronic) or immune

if risk == True :

    print("You are in risky group")

else:

    print("You are not in risky group")



