from random import randint, seed, choice


# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma.\n")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Solution 1:
random_person = randint(0, len(names) -1)
person_paying = names[random_person]
print(f"{person_paying} is the person paying the bill.")

print("")
# Solution 2:

paying_person = choice(names)
print(f"{paying_person} is the person paying the bill.")
