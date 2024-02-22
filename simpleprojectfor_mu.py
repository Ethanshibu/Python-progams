print('''!!! Welcome Adventurer!!! My name is Mu, and i conjure stories, daring yet fascinating, 
       and although they may not be true, they sure are fun to listen to!!\n''')
name = input("What is your name? ")
age = int(input("How old are you? "))
print(''' every story has a beginning, and so does yours. What kind of adventurer are you?
       1. A brave knight
       2. A cunning rogue
       3. A wise wizard
       4. A kind healer
       5. A raging berserker\n''')
c = int(input("Choose your class: "))
if c == 1:
    print("A brave knight, eh? You must be very strong!\n")
    class_choice = "knight"
elif c == 2:
    print("A cunning rogue, eh? You must be very sneaky!\n")
    class_choice = "rogue"
elif c == 3:
    print("A wise wizard, eh? You must be very smart!\n")
    class_choice = "wizard"
elif c == 4:
    print("A kind healer, eh? You must be very caring!\n")
    class_choice = "healer"
elif c == 5:
    print("A raging berserker, eh? You must be very fierce!\n")
    class_choice = "berserker"

print("...and so your journey begins, " + name + " the " + str(class_choice) + "!\n")

print(f''' This is the story of {name} the {class_choice}, a {age} year old adventurer
       who lived in a small but fierce jungle. This jungle was unique as the creatures that lived here were magical beasts, and powerful ones at that.
       But the forest was indeed dangerous, so hunt or be hunted. And {name} happened to be the best hunter of them all.
       {name} had a ritual to complete every year. {name} would slay 1 of the most powerfull beasts in the jungle, and take its heart as a trophy. 
       so far {name} had {age - 5} hearts, and was about to go for the {age-4}th one. The beast was a dragon, and it was the most powerfull of them all.
         And... ahhh ... im sleepy... looks like you'll have to come later, but do not worry, for i will complete this story when you return.
           Goodbye for now, {name} the {class_choice}!''')