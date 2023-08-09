#################################
# Deathbringer.py 1.1           #
# By Chris Stoddard, March 2023 #
# Based on the Deathbringer RPG #
# by Professor Dungeon Master   #
# This code is licensed under   #
# the Creative Commons          #
# Attribution-NonCommercial     #
# 4.0 License.                  #
#################################

#################################
# Import needed libraries
import random

#################################
# Define functions
def Spend_Points():
    global Build_Points
    Temp = input ("? ")
    if Build_Points == 0:
        Temp = "0"
    if int(Temp) > 6:
        Temp = "6"
    if int(Temp) < 0:
        Temp = "0"
    if int(Temp) > Build_Points:
        Temp = str(Build_Points)
    Build_Points = (Build_Points - int(Temp))
    print ("You Have " + str(Build_Points) + " build points to spend.")
    return (Temp)

#################################
# Print Legal Statement.
print ("------------------------------------------------------------")
print ("Legal Statement:")
print ("This Deathbringer Character Generator is an independent")
print ("product and is not affiliated with Professor Dungeon Master.")
print ("Deathbringer RPG © 2023 by Professor Dungeon Master.")
print ("------------------------------------------------------------")

#################################
# Assign ability scores
print ('\n')
print ("You have 8 build points to distribute between your 6 ability scores.")
print ("Strength, Dexerity, Constitution, Intellegence, Wisdom and Charisma.")
print ("No single ability score can exceed +6")
print ('\n')

Build_Points = 8

print ("You Have " + str(Build_Points) + " build points to spend.")

counter = range(6)
for count in counter:
    if count == 0:
        print ("How many build points do you want to assign to Strength:")
        Strength = Spend_Points()
    if count == 1:
        print ("How many build points do you want to assign to Dexterity:")
        Dexterity = Spend_Points()
    if count == 2:
        print ("How many build points do you want to assign to Constitution:")
        Constitution = Spend_Points()
    if count == 3:
        print ("How many build points do you want to assign to Intellegence:")
        Intellegence = Spend_Points()
    if count == 4:
        print ("How many build points do you want to assign to Wisdom:")
        Wisdom = Spend_Points()
    if count == 5:
        print ("How many build points do you want to assign to Charisma:")
        Charisma = Spend_Points()

#################################
# Print Ability scores to screen
print ('\n')
print ("STR: " + "+" + str(Strength))
print ("DEX: " + "+" + str(Dexterity))
print ("CON: " + "+" + str(Constitution))
print ("INT: " + "+" + str(Intellegence))
print ("WIS: " + "+" + str(Wisdom))
print ("CHR: " + "+" + str(Charisma))

#################################
# Class Section
print ('\n')
print ("Choose a Class for your character:")
print (" 1 Deathbringer")
print (" 2 Grimscribe")
print (" 3 Scoundrel")
print (" 4 Witch Hunter")
print (" 5 Plague Doctor")
Choose_Class = input ("? ")

if Choose_Class == "1":
    Class = "Deathbringer"
    HITPOINTS = random.randint(1, 10)
    ClassFeature1 = "Hit Dice: d10. Use any armor or weapons."
    ClassFeature2 = "Spend a Deathbringer Die to make one extra attack."
    ClassFeature3 = "Second attack at 5th level."
    ClassFeature4 = " "
    ClassFeature5 = " "
    Equipment_List = "waterskin, doublet, shield, 2 weapons"
    
if Choose_Class == "2":
    Class = "Grimscribe"
    HITPOINTS = random.randint(1, 6)
    ClassFeature1 = "Hit Dice: d6. Cannot wear armor, simple weapons."
    ClassFeature2 = "No spell slots. Roll to cast, DC 10."
    ClassFeature3 = "On a roll of Natural 1 gain 1 Corruption and roll on the Miscast Table."
    ClassFeature4 = "Gains spells by finding scrolls, spell books, or by having a friendly higher-level magic user teach them to you."
    ClassFeature5 = "You are a living grimoire, must tattoo all spells on your skin."
    Equipment_List = "waterskin, four cantrips, two first-level spells, dagger"

if Choose_Class == "3":
    Class = "Scoundrel"
    HITPOINTS = random.randint(1, 8)
    ClassFeature1 = "Hit Dice: d8. Light armor only, simple weapons."
    ClassFeature2 = "Advantage when attempting stealth, climbing, listening, lockpicking, searching, etc."
    ClassFeature3 = "+4 to hit and double damage from behind."
    ClassFeature4 = " "
    ClassFeature5 = " "
    Equipment_List = "waterskin, leather jacket, club or dagger, thieves' tools, rope, grappling hook, lucky charm."

if Choose_Class == "4":
    Class = "Witch Hunter"
    HITPOINTS = random.randint(1, 8)
    ClassFeature1 = "Hit Dice: d8. Light armor, martial and simple weapons."
    ClassFeature2 = "Cast Detect Evil and Protection from Evil 1x per day"
    ClassFeature3 = "Turn Undead at will."
    ClassFeature4 = " "
    ClassFeature5 = " "
    Equipment_List = "waterskin, leather coat, club, crossbow, holy symbol, 6 torches."
    
if Choose_Class == "5":
    Class = "Plague Doctor"
    HITPOINTS = random.randint(1, 6)
    ClassFeature1 = "Hit Dice: d6. Leather armor only, simple weapons."
    ClassFeature2 = "Cure Wounds once per patient per day, Cure Disease & Cure Poison 1x per day."
    ClassFeature3 = "Create 1d4 potions a day (1) acid splash (2) sleep (3) poison spray (4) bomb [d10] (5) healing [d6] (6) hallucinations"
    ClassFeature4 = " "
    ClassFeature5 = " "
    Equipment_List = "waterskin, Leather beak mask and coat, meat cleaver, medical kit, very suspicious diploma"

#################################
# Randomly chooses background
Random_Backgrounds = ["Bounty Hunter", "Courtesan", "Duelist", "Executioner", "Farmer", "Grave Robber", "Leech Collector", "Mercenary", "Minor Noble", "Outlaw", "Performer", "Pit Fighter", "Pirate/Sailor", "Priest/nun/monk", "Rat Catcher", "Servant", "Student/Scholar", "Swineherd", "Soldier", "Urchin"]
Background = random.choice(Random_Backgrounds)

#################################
# Randomly chooses misery
Random_Misery = ["Abandoned at birth", "Banished from home", "Betrayed by a loved one", "Cursed by vengeful witch", "Disinherited or disowned", "Escaped bondage or prison", "Fled a scandal", "Framed for a crime", "Killed someone important", "Left for dead", "Locusts ate your crops", "Owe someone money", "Pursued by the law", "Raised in the streets", "Reduced to poverty", "Rejected by society", "Ruined by vice", "Suffering from amnesia", "Survived a massacre", "Town ravaged by plague"]
Misery = random.choice(Random_Misery)

#################################
# Generate Starting gold and rations
Gold = random.randint(1, 6)
Rations = random.randint(1, 4)
    
#################################
# Prints out the finished character to the screen
print ('\n')
Character_name = input ("What is your characters name? ")
print ('\n')
print ("Deathbringer Character Sheet 1.1")
print ("------------------------------")
print ("Character Name: " + Character_name)
print ("Background: " + Background)
print ("Misery: " + Misery)
print ("Character Class: " + Class)
print ("XP:    _____")
print ("Level: _____")
print ("------------------------------")
print ("STR: " + "+" + str(Strength))
print ("DEX: " + "+" + str(Dexterity))
print ("CON: " + "+" + str(Constitution))
print ("INT: " + "+" + str(Intellegence))
print ("WIS: " + "+" + str(Wisdom))
print ("CHR: " + "+" + str(Charisma))
print ('\n')
print ("Hit Points: " + str(HITPOINTS))
print ('\n')
print ("------------------------------")
print (ClassFeature1)
print (ClassFeature2)
print (ClassFeature3)
print (ClassFeature4)
print (ClassFeature5)
print ("------------------------------")
print ("EQUIPMENT:")
print (str(Gold) + " GP")
print (str(Rations) + " days of rations")
print (Equipment_List)

#################################
# Write character to a text file using the character name
YN = input ("Do you want to save this character to a text file, Y or N? ")
if YN == "N" or YN == "n":
    exit()

with open(Character_name + '.txt', 'w') as f:
    f.write ('\n')
    f.write ("Deathbringer Character Sheet 1.1" +'\n')
    f.write ("------------------------------" +'\n')
    f.write ("Character Name: " + Character_name +'\n')
    f.write ("Background: " + Background +'\n')
    f.write ("Misery: " + Misery +'\n')
    f.write ("Character Class: " + Class +'\n')
    f.write ("XP:    _____" +'\n')
    f.write ("Level: _____" +'\n')
    f.write ("------------------------------" +'\n')
    f.write ("STR: " + "+" + str(Strength) +'\n')
    f.write ("DEX: " + "+" + str(Dexterity) +'\n')
    f.write ("CON: " + "+" + str(Constitution) +'\n')
    f.write ("INT: " + "+" + str(Intellegence) +'\n')
    f.write ("WIS: " + "+" + str(Wisdom) +'\n')
    f.write ("CHR: " + "+" + str(Charisma) +'\n')
    f.write ('\n')
    f.write ("Hit Points: " + str(HITPOINTS) +'\n')
    f.write ('\n')
    f.write ("------------------------------" +'\n')
    f.write (ClassFeature1 +'\n')
    f.write (ClassFeature2 +'\n')
    f.write (ClassFeature3 +'\n')
    f.write (ClassFeature4 +'\n')
    f.write (ClassFeature5 +'\n')
    f.write ("------------------------------" +'\n')
    f.write ("EQUIPMENT:" +'\n')
    f.write (str(Gold) + " GP" +'\n')
    f.write (str(Rations) + " days of rations" +'\n')
    f.write (Equipment_List +'\n')

exit()