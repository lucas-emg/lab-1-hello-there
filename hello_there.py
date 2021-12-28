#This code should gather the user name, their birth year and calculate their age.
#Then, tell them how many years are left for them to turn 100 years old.
#It also should ask them where they are from (city and country) and give them a messagem about it.

#Iteration 1 - 
# 1 Ask user their name 
# 2 Store their name in a variable
# 3 Give them a message saying hello after that, like "Hey there, John! Glad to meet you!" (use string concatenation for it)
# Your code goes below this line

print("what is your name?")
name = input()
print("Hello there, " + name + "! Glad to meet you.")

#Interation 2 -
# 1 Ask the user what year their were born (from now one, you should always refer to them by their name)
# 2 Store their age in a variable
# 3 Create a variable that calculates how many years are left for them to become 100 year old.
# 4 Give them a message about their age and how many years are left for them to become 100 years old.
# Your code goes below this line

print("In what year were you born, " + name + "?")
birth_year = input()
age = 2021 - int(birth_year)
years_to_be_100 = 100 - int(age)
print("It's nice to be " + str(age) + "! You'll be 100 in " + str(years_to_be_100) 
+ " years.")

#Interation 3 -
# 1 Ask the user which city they are from
# 2 Store the city in a variable
# 3 Ask the user which country is this city in
# 4 Store the country in a variable
# 5 Give the user a message about how you would love to visit their city and country one day
# Your code goes below this line

print("In which city were you born, " + name + "?")
birth_city = input()
print("In which country is " + birth_city + " located?")
country = input()
print("Nice! I would love to visit " + country + ", specially " + birth_city)

#Interation 4 - 
# 1 Ask the user how do they call Santa Claus in their native language
# 2 Store it in a variable
# 3 Give them a final message saying you wish them a Merry Xmas and that Santa Claus (use the one in their native language) brings them a lot of presents
# Your code goes below this line

print("How do you call Santa Claus in your native language, " + name + "?")
santa_claus = input()
print("Cool! Merry Christmas and I hope that " + santa_claus + " brings you a lot of presents.")
