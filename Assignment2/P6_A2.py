Planet_name = ['Mercury', 'Venus', 'Earth', 'Mars',
               'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print(Planet_name)

Planet_inp = input("Please enter a planets name  ")

if Planet_inp in Planet_name[0:2]:
    print("You're in the inner planet.")

elif Planet_inp == Planet_name[2]:
    print("You're on Planet Earth.")

else:
    print("You're in the outer planet")
