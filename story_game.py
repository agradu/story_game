# STORY GAME (advanced version)

print ("""You are by the driving test.
You are behind the wheel and the policeman is on your right. 
What do you do first?""")

# Level 1
level = "failed"
while level != "done":
    print("""1. You start the car with the key
2. Check the mirrors
3. Turn on the radio.""")
    choice = input ("Enter your choice:")
    if choice == "1":
        print()
        print ("""Damn it . You failed. You should have checked something first.
Let's try again.""")
    elif choice == "2":
        print()
        print ("Very wise man! Now let's go to the next step.")
        level = "done"
    else:
        print()
        print ("""No man! You don't need it in exam!
Let's try again.""")

# Level 2
level = "failed"
while level != "done":
    print ("""What do you do next?
1. You start the car with the key
2. Put the car in 1st gear
3. You put on your seat belt""")
    choice = input ("Enter your choice:")
    if choice == "1":
        print()
        print ("""Damn it. You had to do something else. You can fail it!
Let's try again.""")
    elif choice == "2":
        print()
        print ("""No man! You sould do this later!
Let's try again.""" )  
    else:
        print()
        print ("Very wise man! You finished the check list!")
        level = "done"