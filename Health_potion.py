import random

health = 50 #Initial health 

#Creating a variable called difficulty and setting with easy(1) Mode
# Easy: 1, Midium:2 and Hard: 3 are difficulty levels
difficulty = 1 

#By this we can generate a randome number between tha range of 25 to 50.
#Dividing it with difficulty level
#Using int() it will converted into the whole number

potion_health = int(random.randint(25,50)/ difficulty) 
health += potion_health

#printing the new health
print(health)
