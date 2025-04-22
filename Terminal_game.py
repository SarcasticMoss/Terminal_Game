#Eldridge: the game
#imports

#variables

#code
print("""Hello Adventurer!
Welcome to the fantastical world of Eldridge!""")
start = (int(input('Are you ready for your adventure to begin? 1. Yes, or 2. No? ')))

while start == 2:
    print('Prepare yourself!')
    start = int(input('Are you ready? 1. Yes, or 2. No:  '))
if start == 1:
    shop = (int(input("""Then we shall begin our story in the small town of Goatstadt... 
                    Would you like to go to the shop? 1. Yes, to the shop. or 2. No, stay home. """))) 
    
if shop == 1:
    shopping = (int(input("""What would you like to buy...? 
    1. Potions, 2. Weapons, 3. Clothes, or 4. Nothing? """)))
    if shopping == 1:
        print('You bought a health potion!')
    if shopping == 2:
        print('You bought a long sword!')
    if shopping == 3:
        print ('You bought a cape!')
    if shopping == 4:
        print('Forgot your wallet, did you?')

elif shop == 2:
    homebody = (int(input("""What would you like to do? 
    1. Clean the house, 2. Take a nap, or 3. Sit in the garden? """)))
    if homebody == 1:
        clean = (int(input("""What would you like to clean? 
                            1. Kitchen, 2. Bedroom, or 3, Living Room? """)))
        if clean == 1:
            print("The kitchen is sparkling! Time to make some bread!")
        elif clean == 2:
            print('Fresh sheets and no laundry? Time for a well deserved nap!')
        elif clean == 3:
            print('A clean living room, perfect for guest. What about having some over for dinner?')
        
    if homebody == 2:
        sleep = (int(input("""You feel well rested, would you like to go out? 
            1. Shopping, 2. Adventure, 3. No, stay home. """)))
        if sleep == 1:
            shopping = (int(input("""What would you like to buy...? 
            1. Potions, 2. Weapons, 3. Clothes, or 4. Nothing? """)))
            if shopping == 1:
                print('You bought a health potion!')
            elif shopping == 2:
                print('You bought a long sword!')
            elif shopping == 3:
                print ('You bought a cape!')
            elif shopping == 4:
                print('Forgot your wallet did you?')
        if sleep == 2:
            adventure = (int(input("""Which sounds like a good adventure?
            1. Save a town from goblins, 2. Find a rare dagger, or 3. Rescue a child from a troll? """)))
            if adventure == 1:
                print('After a long battle with Boblin the Goblins horde, you successfully save the town, earning 100 gold!')
            elif adventure == 2:
                print('You searched far and wide, to come up empty handed. The dagger was not in reach to you.')
            elif adventure == 3:
                print('The child was actually the trolls, and you particpated in a kidnapping. The town is a bit disappointed.')
        if sleep == 3:
            print('Youre just a pile of lazy bones, huh?')
            
    if homebody == 3:
        garden = (int(input("""The flowers sway in the breeze. What flora do you have in the garden? '
            1. Lavender, 2. Daisies, 3. Sunflowers. """)))
        if garden == 1:
            print('The scent of lavender brings you a peaceful day.')
        elif garden == 2:
            print('The daisies remind you of times as a child. You make a flower crown.')
        elif garden == 3 :
            print('The sunflowers radiant yellow bring out a joy you hadn'\t realized you lost.')
