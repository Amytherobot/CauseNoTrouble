import random as r
import sys
from time import sleep
from colorama import Fore, init
init()



#every time you ask them something, timer goes up
#But what does the timer represent???
#maybe, at least 5 people on the list need to get into the building, otherwise there's a penalty
#not feasible bc random generation

#Maybe if you take too long they start getting mad?
#And then you have to deploy security on them and kill them. Costing you points

#

def firstRun():

    input("Welcome to your new job as a security officer")
    input("Part of your job here is to ensure that every person entering the building is, in fact, who they say they are.")

    print()
    input("There are four types of people who will try to enter.")
    input("Company spies, Civilians, Employees and...others.")

    print()
    input("Company spies are always trying to infiltrate this building, but sometimes civilians get curious and try to get inside.")
    input("Whether or not you let civilians in, I'll leave to you. Just make sure they're...reasonable.")
    input("And...though I shouldn't have to say it, I will. Don't kill any civillians during your time here.")
    input("We can clean up a spy, but a civilian looks bad on all of us. Obviously.")

    print()
    input("As for the others...")
    input("As soon as you think that you're talking to one, don't hesitate. Dispose of them immediately. Don't let them leave.")
    
    print()
    input("Only fifteen people are expected to enter the building during a day. But exceptions can always be made at your disclosure.")
    input("Check their identification against the records, ask follow up questions, and turn them away if you suspect they're lying.")
    input("The safety of our company relies on you. Please do your best.")

def showStats(stats,empKilled,empRefused,empIn,spyKilled,spyRefused,spyIn,CivKilled,CivRefused,badCivIn,goodCivIn,AltsKilled,AltsRefused,AltsIn):
    print(f"{Fore.CYAN}People met:") #< -- blue
    for i in stats:
        print(i) #< -- blue
    print("Stats:") #blue
    print(f"(statistics in red cause you to lose points, green cause you to gain points, and blue don't change your point total.){Fore.WHITE}")
    print()
    print(f'{Fore.RED}Employees Killed: {empKilled}') #red
    print(f'{Fore.RED}Employees Refused: {empRefused}') #red
    print(f'{Fore.GREEN}Employees Let in: {empIn}') #green
    print()
    print(f'{Fore.GREEN}Spies Killed: {spyKilled}') #green
    print(f'{Fore.BLUE}Spies Refused: {spyRefused}') #blue
    print(f'{Fore.RED}Spies Let in: {spyIn}') #red
    print()
    print(f'{Fore.RED}Civilians Killed: {CivKilled}') #red       
    print(f'{Fore.BLUE}Civilians Refused: {CivRefused}') #blue
    print(f'{Fore.RED}Unreasonable Civilians Let in: {badCivIn}') #red
    print(f'{Fore.GREEN}Reasonable Civilians Let in: {goodCivIn}') #green
    print()
    print(f'{Fore.GREEN}Non-humans Killed: {AltsKilled}') #green
    print(f'{Fore.BLUE}Non-humans Refused: {AltsRefused}') #blue
    print(f'{Fore.RED}Non-humans Let in: {AltsIn}') #red
    print()
    gain = empIn + spyKilled + goodCivIn + AltsKilled
    loss = empKilled + spyIn + CivKilled + AltsIn*3
    total = gain - loss

    if total < 0:
        print(f'{Fore.RED}Total score: {total}{Fore.WHITE}') #red
    else:
        print(f"{Fore.GREEN}Total score: {total}{Fore.WHITE}") #green
        
    input("Press Enter to exit...")

def generateEmployee():
    gend = r.randint(1,3)
    fname = ""
    sname = ""

    if gend == 1: #male
        gend = "M"
        with open("BoyNames.txt", "r") as infile:
            boy_names = infile.readlines()
            fname = boy_names[r.randint(0, len(boy_names)-1)].strip()

    elif gend == 2: #female
        gend = "F"
        with open("GirlNames.txt", "r") as infile:
            girl_names = infile.readlines()
            fname = girl_names[r.randint(0, len(girl_names)-1)].strip()

    elif gend == 3: #other
        # \/ this is for the gender on their ID
        temp = coinFlip()
        if temp == True:
            gend = "F"
        else:
            gend = "M"
        
        with open("GenderNames.txt", "r") as infile:
            gender_names = infile.readlines()
            fname = gender_names[r.randint(0, len(gender_names)-1)].strip()

    with open("Surnames.txt", "r") as infile:
        surnames = infile.readlines()
        sname = surnames[r.randint(0, len(surnames) - 1)].strip()

    emp = [fname,sname,gend]

    return emp

def employ(text,speed=0.05,nxt= True):
    print()
    Text = list(text)
    Text.append("\0")
    #this creates the text scrolling effect
    for char in Text:
       sleep(speed)
       if nxt == True:
           if char ==  "\0":
               input()
           else:
               print(f"{Fore.GREEN}{char}{Fore.WHITE}", end="")
               sys.stdout.flush()
       else:
           print(f'{Fore.GREEN}{char}{Fore.WHITE}',end = "")

def generateRecords():
    records = []

    for i in range(15):
        records.append(generateEmployee())

    records = tuple(records)

    return records

def coinFlip():
    yn = r.randint(1,2)
    
    if yn == 1:
        return True
    else:
        return False

def whyAreYouHere(rec,reason,c):

    #maybe twos sets of answers for each reason
    #one if they're a civilian, one if they're a spy.
    #eventually probably put like, ten or so answers per, but to start just have two responses a reason
    
    if reason == "Routine Maintenance": #green light to let in if not lying
        
        employ("I'm here to change out the air filters. On the air conditioning?")
        employ("Is that okay? Can I go in now?")
        
    elif reason == "Visiting Family": #green light
        
        employ("I'm visiting my brother, he works here.")
        employ("He said he'd show me his office today.")
        
    elif reason == "Official meeting": #green light
        
        employ("I'm visiting from overseas. I have a meeting with your boss in fifteen minutes.")
        
    elif reason == "Cleaning crew": #green light
        
        employ("Someone messed up on one of the sublevels.")
        employ("They called me to uh...clean it up.")
        
    elif reason == "Mail delivery": #green light
        index = r.randint(0,len(rec)-1)
        emp = rec[index]

        #you could make this a specific name, then make an easter egg for if that specific person shows up
        employ(f"I have a package for {emp}. I was told to hand it right to em.")
        
    elif reason == "Forgot something": #green light
        
        employ("I was here yesterday, I know I'm not scheduled for today but I forgot something.")
        employ("Can you please let me through?")
        
    elif reason == "Filing a Complaint": #red light
        
        employ("Yes, I'm here to talk to whoever's in charge here.")
        employ("My sister went missing a week ago and the last I heard from her she was coming HERE.")
        employ("So I'd like to know where she is, THANK YOU.")
        
    elif reason == "Contracted Worker": #green light
        
        employ("I'm a police officer. Your bosses hired me to work down in the basement?")
        employ("Something about sublevel 13 or something?")
        
    elif reason == "Previously escaped": # either or
        
        employ("I... I'm supposed to be here.")
        employ("I'm sorry I...didn't mean to cause any trouble.")
        employ("Please just let me back in!")
        
    elif reason == "Refused to disclose": # red light

        employ("I don't know. I've never been in this building before.")
        employ("It looked kind of cool. Can I see inside?")
        
    elif reason == "Reporting for work": # green light
        employ("I work here. I'm supposed to clock in a few minutes.")

def appearance(isAlt,coin,coin2,coin3):
    look = "none"
    
    while look != "0":
        print()
        print("Are there any features you want to look over more closely?")
        print()
        print("1: Face")
        print("2: Arms")
        print("3: Torso")
        print("0: Ask something else")
        look = input()

        if look == "1":
            if isAlt == True:
                if coin == True:
                    input("Their face is long, you can't tell if its in an unnatural way or not.")
                    input("Their eyes look sunken in and dead.")
                    input("And their nose is incredibly small.")
                    input("They haven't broken eye contact.")
                else:
                    input("Their chin is incredibly small, and their face is short, almost unnaturally so.")
                    input("Their eyes are bright and large, and darting about the floor.")
                    input("They are avoiding eye contact.")
                
            else:
                if coin == True:
                    input("Their face is round and small, the light in their eyes are dulled, and their nose is quite long.")
                    input("You don't notice anything out of the ordinary.")
                else:
                    input("Their face is long, and thin. Their eyes are beady and small, and their nose is quite wide.")
                    input("You don't notice anything out of the ordinary.")
                
        elif look == "2":
            if isAlt == True:
                if coin2 == True:
                    input("Their arms stretch beyond what you can feasibly see.")
                    input("You can't see their hands. Their shoulders hang too low.")
                else:
                    input("Their elbows stop at the center of their chest.")
                    input("Their hands are passively squeezing an imaginary ball at their side.")
                    input("The sight disturbs you.")
                
            else:
                if coin2 == True:
                    input("Their elbows stop at their waist, and they're fidgeting with their hands.")
                    input("Their hands are calloused, and the cuticles have been ripped at.")
                else:
                    input("Their elbows stop at their waist, and their arms are folded.")
                    input("Their hands are tucked away in the nooks of their arms. You can't see them.")
                
                
        elif look == "3":
            if isAlt == True:
                if coin3 == 1:
                    input("Their torso looks to be stretched upwards, forcing them to lean down to fit inside the building foyer.")
                    input("Their face looms over you, their shoulders set squarely against the ceiling.")
                    
                elif coin3 == 2:
                    input("Their torso is unproportionally short compared to their limbs and head.")
                    input("Its as though their body was squashed down by an industrial juicer. ")
                elif coin3 == 3:
                    input("Their torso looks to be of average size. You don't notice anything strange.")
                
            else:
                input("Their torso looks to be of average size. You don't notice anything strange.")

def question(c,emp,reason,isOnList,isAlt,isLying,exp,rec,coin,coin2,coin3):
    R = {1 :"Routine Maintenance", 2 :"Visiting Family",3 :"Official meeting",4 :"Cleaning crew",5 :"Mail delivery", 6 :"Forgot something",7 :"Filing a Complaint",8 :"Contracted Worker",9 :"Previously escaped",10 :"Refused to disclose", 11 :"Reporting for work"}
    user = "none"
    Flag = False
    FaceFlag = True

    while user != "0":
        print()
        print("What would you like to ask about?")
        print()
        print("1: Their ID")
        print("2: Their reason for entering")
        print("3: The Records")
        print("4: Their Appearance")
        print("5: Something doesn't make sense [CONFRONT]")
        print("0: End questioning")
        user = input()

        if user == "1":
            if exp == True:
                employ("Is something wrong with my ID? I only got it yesterday.")
            else:
                employ("What's wrong with my ID? It can't be expired yet.")
        elif user == "2":
            employ("Why am I here?")
            if isLying == False:
                whyAreYouHere(rec,reason,c)

            else:
                diceroll = r.randint(1,11)
                Lreason = R[diceroll]
                whyAreYouHere(rec,Lreason,c)
                    
        elif user == "3":
            if isOnList == True:
                employ("The records?")
                employ("I'm scheduled to work today. I should be on that list.")
            else:
                if isLying == True:
                    employ("What are you talking about?")
                    employ("Today's my first day, I don't know anything about any list.")
                else:
                    employ("List? I don't know anything about any list.")
                    employ("Listen, can you just let me through? I don't have all day.")
                
        elif user == "4":
            if isAlt == True and isLying == True:
                if coin == True:
                    input("Their photo matches their face pretty well.")
                    input("Even so, something feels off about the way they're staring at you. You can't put it into words.")
                    employ("Is everything all right?", 0.09)
                    Flag = True
                else:
                    input("The photo on their ID matches with their face")
                    input("They look nervous and keep trying to look past you.")
            elif isLying == True and not isAlt == True:
                if coin == True:
                    input("The photo on their ID matches with their face")
                    input("They look nervous and keep trying to look past you.")
                else:
                    input("The photo on their ID doesn't match with their face.")
                    input("It isn't even close.")
                    FaceFlag = False
                    
            elif isLying == False:
                input("The photo on their ID matches with their face.")
                input("They look nervous and keep trying to look past you.")

            appearance(isAlt,coin,coin2,coin3) 


        elif user == "5":
            employ("What? What do you mean?")
            user2 = "none"
            while user2 != "done":
                print()
                print("1: The date on your ID is incorrect.")
                print("2: Your reason for being here doesnt make sense.")
                print("3: Your name isn't on the records.")
                print("4: Your ID photo doesn't look like you.")
                if Flag == True:
                    print("5: The way you're staring at me.")
                print("0: Never mind")
                user2 = input()

                if user2 == "1":
                    if exp == True and isLying == True:                    
                        employ("No it's not! You're seriously trying to pull one over on me?",speed=0.01)
                        if c == "civ":
                            employ("...")
                            employ("Oh well, maybe it is.")
                            employ("My mistake.")
                        elif c == "spy":
                            employ("The absolute nerve, I swear.")
                            employ("I only got it yesterday and you expect me to believe its expired?")
                            
                    elif exp == True and isLying == False:
                        employ("What? It's expired already?")
                        employ("Shit. I had no idea. That ones on me I guess.")
                        
                    elif exp == False:
                        if c == "emp":
                            employ("What the hell are you talking about?")
                            employ("Is this some kind of new test I don't know about?")
                            employ("If it is, you'll need to come up with something better to fool anyone around here.")
                        elif c == "civ":
                            employ("It's expired? No, I don't think so.")
                            employ("Well, it could be, but I'm pretty sure I'd know by now if it wasn't.")
                        elif c == "spy":
                            employ("Expired? Are you serious? Is that the best you could come up with?")
                            employ("I really don't have time for this, just hit the button and let me in already.")

                        
                elif user2 == "2":
                    if isLying == True:
                        #if what they said matches up with whats written on the entrance pass
                        if reason == Lreason:
                            if c == "civ":
                                employ("What? No, I'm pretty sure I said the right thing.")
                                employ("I mean, what doesn't make sense about it? It's pretty straightforward right?")
                            elif c == "spy":
                                employ("Are you calling me a liar?" )
                                employ("You can't seriously think your job is THAT secure." )
                                employ("My reason for being here is sound.")
                        else:
                            if c == "civ":
                                employ("What? No, I'm pretty sure I said the right thing." )
                                employ("Did I...? Wait, hold on uhm...")
                                employ("Well, shit I guess I didn't. My bad.")
                            elif c == "spy":
                                employ("One little inconsistency and suddenly I'm lying?" )
                                employ("I got a little mixed up, thats all." )
                                employ("Anyway, the door.")
                    elif isLying == False:
                        if c == "civ":
                            employ("What do you mean it doesn't make sense, I thought it was pretty straightforward." )
                            employ("Just, check the paper again. Maybe that'll help you out?")
                        elif c == "spy":
                            employ("I think it's pretty straight forward." )
                            employ("Maybe you should check the papers again just to be sure.")
                        elif c == "emp":
                            employ("What the hell are you on about" )
                            employ("I. WORK. HERE. Is that a good enough reason for you?")
                            employ("Jesus christ. I'll have you reported for this kind of harassment.")

                elif user2 == "3":
                    if isOnList == True:
                        if c == "civ":
                            employ("Um...I'm pretty sure it is." )
                            employ("I mean, I'm working today so... I'm probably on the list, right?")
                        elif c == "spy":
                            employ("Check again. My names on there." )
                            employ("What kind of people are they hiring here nowadays that you don't even know...?" )
                            employ("Just open the door already.")
                        elif c == "emp":
                            employ("You're kidding right? I'm here every wednesday of course I'm on the list." )
                            employ("Do you joke around like this a lot?")
                    else:
                        if c == "civ":
                            employ("Oh uh..." )
                            employ("shit I had no idea there was a list...",speed=0.01 )
                            employ("Maybe just...don't worry about it this time?" )
                            employ("I just, I really need to get inside, you know?")
                        elif c == "spy":
                            employ("What? There must be a mistake or something" )
                            employ("Check it again. I'm on the list." )
                            employ("...I grabbed the right name didn't I...?")
                    
                elif user2 == "4":
                    if FaceFlag == True: #the photo does match with their face
                        if c == "civ":
                            employ("What? Let me see," )
                            employ("...No that's definitely me in that photo." )
                            employ("Are you okay? Should I call somebody?")
                        elif c == "spy":
                            employ("Did you even check? Of course it looks like me it IS me." )
                            employ("I don't have time for this, just let me through already.")
                        elif c == "emp":
                            employ("What? Let me see that." )
                            employ("..." )
                            employ("You're serious?" )
                            employ("Thats me." )
                            employ("Maybe you should take a break or something.")
                    
                    elif FaceFlag == False: #the photo does not match with their face
                        if c == "civ":
                            employ("What? You're not serious, are you?" )
                            employ("Oh shit you are serious." )
                            employ("...Well fuck," )
                            employ("Guess I'll have to come back later, right?")
                        elif c == "spy":
                            employ("Yes it does." )
                            employ("Do you think I'm an idiot or something? Thats me on there." )
                            employ("Sure it was a couple of years ago, my hairs a bit different, but thats me." )
                            employ("Oh don't tell me you're going to turn me away for THIS.")
                        elif c == "emp":
                            employ("What?" )
                            employ("Oh shit. I grabbed the wrong ID.")
                            input("They sigh loudly")
                            employ("Just tell the boss what happened. I'll be in tomorrow.")
                        
                        
                elif user2 == "5" and Flag == True:
                    employ("...",speed = 0.07)
                    print()
                    input("They're just smiling at you.")
                    employ("Open the door please." ,speed = 0.07)
                    employ("I think we'll both be happier if you do.",speed = 0.07)

                elif user2 == "0":
                    if c == "civ":
                        employ("Oh uh, okay.")
                    elif c == "spy":
                        employ("Then why'd you even say anything?")
                    elif c == "empy":
                        employ("Good. Are you almost done?")
                    user2 = "done"



                

def entryTicket(isOnList,c):
    R = {1 :"Routine Maintenance",2 :"Official meeting",3 :"Cleaning crew",4 :"Mail delivery", 5 :"Contracted Worker",6 :"Visiting Family",7 :"Forgot something",8 :"Filing a Complaint",9 :"Previously escaped",10 :"Refused to disclose", 11 :"Reporting for work"}
    
    if isOnList == True:
        reason = R[11]
    else:
        if c == "emp":
            reason = R[r.randint(1,5)]
        elif c == "civ":
            reason = R[r.randint(6,10)]
        else:
            reason = R[r.randint(1,10)]

    return reason

def generateExpDate(c):
    m = r.randint(1,12)
    d = r.randint(1,31)

    exp = coinFlip()
    if exp == True and c != "emp":
        y = r.randint(2018,2019)
    elif exp == True and c == "emp":
        #specifically if todays date is may 2nd 2020
        y = 2020
        m = r.randint(1,4)
        d = r.randint(1,28)
    else:
        #specifically if todays date is may 2nd 2020
        y = r.randint(2020,2025)
        m = r.randint(5,12)
        d = r.randint(2,28)

    date = f"{m}/{d}/{y}"

    return date, exp

def whatClass(isOnList):
    if isOnList == True:
        c = coinFlip()
        if c == True:
            c = "emp"
            isLying = False
        else:
            c = "spy"
            isLying = True
    elif isOnList == False:
        c = r.randint(1,3)
        if c == 1:
            c = "emp"
            isLying = False
        elif c == 2:
            c = "spy"
            isLying = True
        elif c == 3:
            c = "civ"
            isLying = coinFlip()

    return c, isLying
    

def endRound(user,c,isLying,reason,emp,isAlt):
    user = int(user)
    if user == 4: #let them in
        input("You open the door.")
        if isAlt == True:
            employ("Thank you.")
            print()
            input("They step through the door.")
            user = f"Let in alt: {emp}"
            return user
        elif isAlt == False:
            if isLying == True:
                if c == "civ":
                    #point loss
                    employ("I appreciate it.")
                    print()
                    input("They step through the door.")
                    user = f"Let in civilian-bad: {emp}"
                    return user
                elif c == "spy":
                    #point loss
                    employ("Thank you. Finally")
                    print()
                    input("They step through the door.")
                    user = f"Let in spy: {emp}"
                    return user
            else:
                if c == "civ":
                    if reason != "Previously escaped" or reason != "Filing a Complaint" or reason != "Refused to disclose":
                        employ("Thanks")
                        print()
                        input("They step through the door.")
                        user = f"Let in civilian-good: {emp}"
                        return user
                    else:
                        #point loss
                        employ("THANK you.")
                        print()
                        input("They step through the door.")
                        user = f"Let in civilian-bad: {emp}"
                        return user
                elif c == "spy":
                    #point loss
                    employ("Thank you. Finally")
                    print()
                    input("They step through the door.")
                    user = f"Let in spy: {emp}"
                    return user
                elif c == "emp":
                    #point gain
                    employ("Thank you.")
                    print()
                    input("They step through the door.")
                    user = f"Let in employee: {emp}"
                    return user
                
    elif user == 5: #refuse entry
        input("You tell them they need to leave, or you'll call security.")
        if isAlt == True:
            if c == "civ":
                employ("Security?! Is THAT necessary?" )
                employ("No need to call anyone I'll just go.")
                print()
                input("They leave without another word.")
                user = f"Refused Alt: {emp}"
                return user
            elif c == "spy":
                employ("Are you serious?" )
                employ("I don't think you understand, I NEED to get inside." )
                employ("This isn't a game. There are lives on the line, do you understand that?")
                print()
                input("They're not moving.")
                print("Deploy security? (Y/N)")
                dep = input()
                dep.lower()
                if dep == "y":
                    input("You deploy security.")
                    employ("Wait- who are these people?")
                    employ("What are you-")
                    input("A horrifying, inhuman screech rings through your ears.")
                    input("You shut the window until it's done.")
                    user = f"Killed Alt: {emp}"
                    return user
                else:
                    input("...")
                    employ("Ugh, fine. Some people are just heartless.")
                    input("They leave.")
                    user = f"Refused Alt: {emp}"
                    return user
                
            elif c == "emp":
                employ("Are you fucking serious?" )
                employ("I work here! You can't just keep me out!" )
                employ("Check my ID again! I'm in the system just LOOK.")
                print()
                input("They're not moving.")
                print("Deploy security? (Y/N)")
                dep = input()
                dep.lower()
                if dep == "y":
                    input("You deploy security.")
                    employ("Wait what are you-")
                    input("A horrifying, inhuman screech rings through your ears.")
                    input("You shut the window until it's done.")
                    user = f"Alt killed: {emp}"
                    return user
                else:
                    employ("..." )
                    employ("You're really doing this. Fine." )
                    employ("See you tomorrow.")
                    print()
                    input("They leave.")
                    user = f"Alt refused: {emp}"
                    return user

        else:
            if c == "civ":
                employ("Security?! Is THAT necessary?" )
                employ("No need to call anyone I'll just go.")
                print("They leave without another word.")
                user = f"civilian refused: {emp}"
                return user
            elif c == "spy":
                employ("Are you serious?" )
                employ("I don't think you understand, I NEED to get inside." )
                employ("This isn't a game. There are lives on the line, do you understand that?")
                print()
                input("They're not moving.")
                print("Deploy security? (Y/N)")
                dep = input()
                dep = dep.lower()
                if dep == "y":
                    input("You deploy security.")
                    employ("Wait- who are these people?")
                    employ("What are you doing- YOU CANT-")
                    input("You shut the window until it's done.")
                    user = f"Killed spy: {emp}"
                    return user
                else:
                    input("...")
                    employ("Ugh, fine. Some people are just heartless.")
                    input("They leave.")
                    user = f"Refused spy: {emp}"
                    return user
                
            elif c == "emp":
                employ("Are you fucking serious?")
                employ("I work here! You can't just keep me out!")
                employ("Check my ID again! I'm in the system just LOOK.")
                print()
                input("They're not moving.")
                print("Deploy security? (Y/N)")
                dep = input()
                dep = dep.lower()
                if dep == "y":
                    input("You deploy security.")
                    employ("Wait what are you-")
                    employ("Theres been a mistake! Check my papers I'm-")
                    input("You shut the window until it's done.")
                    user = f"Employee killed: {emp}"
                    return user
                else:
                    employ("...")
                    employ("You're really doing this. Fine.")
                    employ("See you tomorrow.")
                    input("They leave.")
                    user = f"Employee refused: {emp}"
                    return user
            
    elif user == 6: #deploy security
        input("You deploy security. And shut the window.")

        if isAlt == True:
            input("You try not to listen to the sounds on the other side.")
            input("But the scream you hear is unlike any creature you've ever heard in your life.")
            user = f"Alt killed: {emp}"
            return user
            
        else:
            if c == "emp":
                employ("Wait what are you-")
                employ("Theres been a mistake! Check my papers I'm-")
                input("You plug in earbuds until it's done.")
                user = f"Employee killed: {emp}"
                return user
            elif c == "spy":
                employ("Wait- who are these people?")
                employ("What are you doing- YOU CANT-")
                input("You plug in earbuds until it's done.")
                user = f"Killed spy: {emp}"
                return user
            elif c == "civ":
                employ("Wait- what are you doing?")
                employ("HEY! I'M STILL IN HE-")
                input("You plug in earbuds until it's done.")
                user = f"Killed civilian: {emp}"
                return user


def game(rec):
    user = "none"
    print()
    input("Someone approaches your desk.")

    isOnList = coinFlip()
    if isOnList == True:
        index = r.randint(0,len(rec)-1)
        emp = rec[index]
    else:
        emp = generateEmployee()


    #3 classes of person: civ, emp, spy (Alts can be any of these)
    c,isLying = whatClass(isOnList)

    date,exp = generateExpDate(c)


    reason = entryTicket(isOnList,c)
    isAlt = coinFlip()
    coin = coinFlip()
    coin2 = coinFlip()
    coin3 = r.randint(1,3)

    employ("'Hello there.'")
    print("They slide their ID and Entrance Pass through the glass.",end=input())
    
    print()

##    #DEBUG
##    printc(red(f"Class = {c} Lying = {isLying} Alt = {isAlt} Written Reason = {reason} ExpiredID = {exp} OntheList = {isOnList}"))

    while user != "8":
        print()
        print("What do you want to do? Type the corresponding number to choose")
        print()
        print("1: Check records")
        print("2: Check documents")
        print("3: Question employee")
        print("4: Let them in")
        print("5: Refuse entry")
        print("6: Dispose of them")
        print("7: What day is it again?")
        print("8: Quit")
        user = input()

        if user == "1":
            print()
            count = 0
            for i in rec:
                for j in i:
                    print(j,end=" ")
                    count += 1
                    if count == 3:
                        print()
                        count = 0
                        break
        elif user == "2":
            print(f"ID: {emp} Expires: {date}")
            print(f"Reason for entering: {reason}")
        elif user == "3":
            question(c,emp,reason,isOnList,isAlt,isLying,exp,rec,coin,coin2,coin3)
        elif user == "4" or user == "5" or user == "6":
            user = endRound(user,c,isLying,reason,emp,isAlt)
            return user
        elif user == "7":
            print("Today is May 2nd, 2020.")
        elif user == "8":
            return user
    


def main():

    #Tutorial check
    tut = ""
    while tut == "":
        print("Do you want to play the tutorial?")
        print("Please type your answer below")
        tut = input()

    tut = tut.lower()
    if "y" in tut:
        print()
        firstRun()

    #stats stuff \/
    stats = []
    spyIn = 0
    spyRefused = 0
    spyKilled = 0
    
    badCivIn = 0
    goodCivIn = 0
    CivRefused = 0
    CivKilled = 0
    
    AltsKilled = 0
    AltsRefused = 0
    AltsIn = 0
    
    empIn = 0
    empRefused = 0
    empKilled = 0
    
    endstate = "success"

    print()
    print("Today is May 2nd, 2020.")
    rec = generateRecords()
    print("Your records for the day have come in.",end=input())
    print("The building has opened and you take your place at your desk.",end=input())

    #10 is the duration of the game
    for i in range(10):
        state = game(rec)

        if state == "8":
            exit()
            
        elif "alt" in state or "Alt" in state:
            if "Let in" in state:
                AltsIn += 1
                stats.append(state)
                endstate = "alt"
                break
            elif "refused" in state:
                AltsRefused += 1
                stats.append(state)
            elif "killed" in state:
                print()
                print("{Fore.BLUE}Alternate successfully terminated{Fore.WHITE}") #< -- blue
                AltsKilled += 1
                stats.append(state)
        
        elif "civilian" in state:
            if "Let in" in state:
                if "civilian-good" in state:
                    goodCivIn += 1
                    stats.append(state)
                elif "civilian-bad" in state:
                    badCivIn += 1
                    stats.append(state)
            elif "refused" in state:
                CivRefused += 1
                stats.append(state)
            elif "Killed" in state:
                CivKilled += 1
                stats.append(state)
        
        elif "spy:" in state:
            if "Let in" in state:
                spyIn += 1
                stats.append(state)
            elif "refused" in state:
                spyRefused += 1
                stats.append(state)
            elif "Killed" in state:
                spyKilled += 1
                stats.append(state)
            
        elif "employee" in state or "Employee" in state:
            if "Let in" in state:
                empIn += 1
                stats.append(state)
            elif "refused" in state:
                empRefused += 1
                stats.append(stats)
            elif "Killed" in state:
                empKilled += 1
                stats.append(state)

    if endstate == "success":
        print("A loud buzzer blares through the building.")
        print("The day shift has ended. Please come back promptly at 6am tomorrow.")
        print("Have a nice night.")
        print("Press enter for stats...",end=input())

        showStats(stats,empKilled,empRefused,empIn,spyKilled,spyRefused,spyIn,CivKilled,CivRefused,badCivIn,goodCivIn,AltsKilled,AltsRefused,AltsIn)

        exit()
        
    elif endstate == "alt":
        input("...")
        input("You hear a crunching sound somewhere in your booth.")
        input("Not the crunching of chips being chewed or glass beneath a shoe, but the crunching of bone turned to squelching of flesh and the gushing of blood.")
        input("You turn to the source of the noise and...")
        print()
        print("GAME OVER")
        print("Tip: Non-humans will pretend to be humans to try and enter. Letting them in will kill you.")
        input("Press enter for stats...")
        
        showStats(stats,empKilled,empRefused,empIn,spyKilled,spyRefused,spyIn,CivKilled,CivRefused,badCivIn,goodCivIn,AltsKilled,AltsRefused,AltsIn)

        exit()
    

main()
