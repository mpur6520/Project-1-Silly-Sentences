# Maru Puran
# September 20, 2023
# user inputs a set of words according to the printed requests, program then uses those words in a paragraph and outputs sentences w/ them

print("Let's play Silly Sentences! \n") #print intro sentence

name = str(input("Enter a name: ")) #ask user to enter name, save input
adj1 = str(input("Enter an adjective: ")) #ask user to enter adj, save input
adj2 = str(input("Enter an adjective: ")) #ask user for another adj, save input
adv = str(input("Enter an adverb: ")) #ask user for an adv, save input
food1 = str(input("Enter an food: ")) #ask user for a food, save input
food2 = str(input("Enter an food: ")) #ask user for another food, save input
noun = str(input("Enter a noun: ")) #ask user for a noun, save input
place = str(input("Enter a place: ")) #ask user for a place, save input
verb = str(input("Enter a verb: ")) #ask user for a verb, save input

print(" ") #line break

#below, use inputs saved in variables to construct sentences; variables change depending on what user inputs into computer
print(name + " was planning a dream vacation to " + place + ".")
print(name + " was especially looking forward to trying the local\ncuisine, including "  + adj1 + " " + food1 + " and " + food2 + ".")
print(" ")
print(name + " will have to practice the language " + adv + " to\nmake it easier to " + verb + " with people.")
print(" ")
print(name + " has a long list of sights to see, including the\n" + noun + " museum and the " + adj2 + " park.")