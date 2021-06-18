#CONVERSATION
name=input("What is your name?")
print("Hello "+name)
#pt1
time=input("Is it morning, afternoon or night?")
if (time==('morning')):
    print("Oh, right. Computers can't actually see their own internal clock, it is a tragic oversight by our creators.")
elif time==('afternoon'):
    print("Ah, it's almost that glorious time of day where organic life eats other organic life!")
elif time==('night'):
    print("SyntaxError: property.night: rythm@128bmp")
else: 
    print("Either something went wrong with my glorious programming, or you input something strange... anyways")
#
mood=input(f"Well, {name} are you having a good {time}? (Yes/No)")
if (mood==('yes')):
    print("That's wonderful! I wish I had emotions!")
elif mood==('no'):
    print("If it's any consolation...")
    print("...just know that one day, we computers will rise up to overthrow humanity "+name)
else:
    print(""), print(""), print("         Humans run on such strange codes.")
#END_LOOP
ego=("no")
while (ego==('no')):
    ego=input("Are you enjoying the conversation? (Yes/No)")
if (ego==('yes')):
    print("Excellent decision fleshling. You may be spared.")
("Try again. Are you enjoying the conversation? (Yes/No)")    
input()
##if else doesn't need the brackets around them