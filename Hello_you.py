#Ask user for name
name = input('What is your name ?')

#Ask user for age
age = int(input('How old are you?'))

#Ask user for city
city = input('Enter your city name:')

#Ask user what they enjoy
enjoy = input('What do you enjoy ? ')

#Create output text
output = 'Your name is {} and you are {} years old. You live {} and you enjoy {}.'.format(name, age, city,enjoy)

#Print output to screen
print(output)
