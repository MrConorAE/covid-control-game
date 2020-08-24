# ABOUT THIS PROGRAM
# This is a game written for a Computer Science project.
# It is NOT intended, guaranteed or assured that its simulation will be accurate, and should not be used for any such purpose.
# Program, code, output, assets and any accompanying materials (c) Conor Eager 2020. All rights reserved.

# IMPORT STATEMENTS
# Import the 'datetime' module - for managing dates and times.
import datetime
# Import the 'time' module - for managing times (e.g. delays).
import time
# Import the 'random' module - for generating random numbers.
import random

# NOTE ABOUT NUMBERS/VALUES:
# To avoid ZeroDivisionErrors, anywhere the value 0 may be used, 0.001 may be used instead. As the display is only to 2dp, it makes a neglegible difference.
# The code has been modified to also account for this.

# DATA STRUCTURES


class Option:
    # This class describes an option the player can "activate" (start enforcing).
    def __init__(self, n, d, s, t, c, h, e):
        self.name = n
        self.desc = d
        self.supp = s
        self.test = t
        self.comp = c
        self.happ = h
        self.econ = e


class Measures:
    # This class describes the total/sum of all the players' chosen Options.
    def __init__(self, a):
        active = a
    inft = 1
    supp = 0.001
    test = 0.001
    comp = 50
    happ = 50
    econ = 50


class CoronaStats:
    # This class describes a time period's COVID statistics (cases/deaths/recoveries).
    def __init__(self, c, d, r, a):
        self.case = c
        self.dead = d
        self.recv = r
        self.actv = a


class Country:
    # This class represents the player (as the country they are governing). It stores the player's information.
    def __init__(self, n, l):
        self.ctry = n
        self.name = l
    msrs = [Measures([]), Measures([])]
    stat = [CoronaStats(1, 1, 1, 1), CoronaStats(1, 1, 1, 1)]
    turn = 0
    date = datetime.datetime(2020, 1, 1)


class SaveFile:
    # This class represents a save file. Creating and loading save files is done/processed through these objects.
    def __init__(self, n, d):
        time = datetime.datetime.now()
        name = n
        data = d

# VARIABLES


player = None
options = []

# FUNCTIONS


def display(c):
    try:
        # This function is based on the development prototype found in display.py. It has been modified (singnificantly) to
        # operate with the new data structure used in this version (see above).
        #
        #
        # Add some padding to make it more readable.
        print("\n\n")
        # Print the turn number, date and player name.
        print(
            f"TURN {c.turn:>3} - DATE {c.date.day:02}/{c.date.month:02}/{c.date.year:03} - Prime Minister of {c.ctry}, {c.name}")
        print("-------------------------------------------------------------------------------------------------------------")
        # Print the COVID-19 statistics.
        print(f"CORONAVIRUS STATISTICS                THIS TURN                 TOTAL")
        print(
            f"                 Cases               {c.stat[1].case:>+10}            {c.stat[0].case:>10}")
        print(
            f"                Deaths               {c.stat[1].dead:>+10}            {c.stat[0].dead:>10}     ({(c.stat[0].dead/c.stat[0].case)*100:>5.2f}% Death Rate)")
        print(
            f"            Recoveries               {c.stat[1].recv:>+10}            {c.stat[0].recv:>10}     ({(c.stat[0].recv/c.stat[0].case)*100:>5.2f}% Recovery Rate)")
        print(
            f"                Active               {c.stat[1].actv:>+10}                   ---     ({(c.stat[1].actv/c.stat[0].case)*100:>5.2f}% Active)")
        print("")
        print("-------------------------------------------------------------------------------------------------------------")
        # Print the Ratings (transmission, testing, suppression, happiness, compliance, economy)
        print(f"        RATINGS/STATUS                THIS TURN                CHANGE        as %")
        print(
            f"     Transmission Rate               {c.msrs[0].inft:>10.2f}            {(c.msrs[0].inft-c.msrs[1].inft):>+10.2f} {((c.msrs[0].inft-c.msrs[1].inft)/c.msrs[1].inft)*100:>+10.2f}%")
        print(
            f"          Testing Rate               {c.msrs[0].test:>10.2f}            {(c.msrs[0].test-c.msrs[1].test):>+10.2f} {((c.msrs[0].test-c.msrs[1].test)/c.msrs[1].test)*100:>+10.2f}%")
        print(
            f"    Suppression Rating               {c.msrs[0].supp:>10.2f}%           {(c.msrs[0].supp-c.msrs[1].supp):>+10.2f} {((c.msrs[0].supp-c.msrs[1].supp)/c.msrs[1].supp)*100:>+10.2f}%")
        print(
            f"     Citizen Happiness               {c.msrs[0].happ:>10.2f}%           {(c.msrs[0].happ-c.msrs[1].happ):>+10.2f} {((c.msrs[0].happ-c.msrs[1].happ)/c.msrs[1].happ)*100:>+10.2f}%")
        print(
            f"            Compliance               {c.msrs[0].comp:>10.2f}%           {(c.msrs[0].comp-c.msrs[1].comp):>+10.2f} {((c.msrs[0].comp-c.msrs[1].comp)/c.msrs[1].comp)*100:>+10.2f}%")
        print(
            f"       Economic Rating               {c.msrs[0].econ:>10.2f}%           {(c.msrs[0].econ-c.msrs[1].econ):>+10.2f} {((c.msrs[0].econ-c.msrs[1].econ)/c.msrs[1].econ)*100:>+10.2f}%")
    except (ZeroDivisionError):
        pass

# SETUP
# This function initialises all the variables in the game, and sets up their data (such as username and age).


def init():
    print("""
======================================================================# WELCOME TO #===================================================================

      ::::::::    ::::::::   :::     :::  :::::::::::  :::::::::          ::::::::    ::::::::   ::::    :::  :::::::::::  :::::::::    ::::::::   :::  
    :+:    :+:  :+:    :+:  :+:     :+:      :+:      :+:    :+:        :+:    :+:  :+:    :+:  :+:+:   :+:      :+:      :+:    :+:  :+:    :+:  :+:   
   +:+    +:+  +:+    +:+  +:+     +:+      +:+      +:+    +:+        +:+    +:+  +:+    +:+  :+:+:+  +:+      +:+      +:+    +:+  +:+    +:+  +:+    
  +#+         +#+    +:+  +#+     +:+      +#+      +#+    +:+        +#+         +#+    +:+  +#+ +:+ +#+      +#+      +#++:++#:   +#+    +:+  +#+     
 +#+    +#+  +#+    +#+   +#+   +#+       +#+      +#+    +#+        +#+    +#+  +#+    +#+  +#+  +#+#+#      +#+      +#+  +#+    +#+    +#+  +#+      
#+#    #+#  #+#    #+#    #+#+#+#        #+#      #+#    #+#        #+#    #+#  #+#    #+#  #+#   #+#+#      #+#      #+#   #+#   #+#    #+#  #+#       
########    ########       ###      ###########  #########          ########    ########   ###    ####      ###      ###    ###   ########   ##########
 
=======================================================================================================================================================

It's the year 2019, on the planet Earth.

Somewhere in Wuhan, China, someone buys a bat from a wet market. 
Unknowingly, they have just released a deadly virus upon the world - SARS COVID-19.

Fast-forward 6 months...
...and the world is scrambling to contain the outbreak. Hundreds of thousands have died. Tens of millions are infected.
Hospitals are overflowing. Medical professionals are pleading with their already-stretched governments for more funding and equipment.

That's where you come in.

Last night, in a suprise press conference, the leader of your country resigned. In the middle of a global pandemic. Oh well...
Oh wait - you, as their second-in-command, need to step up to fill the role.

Only problem is, YOU now have to control this deadly infection, and keep your country running...

                                                                     - * # * -

You wake up. It's 6:30am on the 1st of March, 2020 - your first day as leader.
""")
    input("Press [ENTER] to continue... ")
    # Padding
    print("-----------------------------------------------------------------------------------")
    print("Right: now that we've got the backstory out of the way, let's get started!")
    print("")  # Padding
    print("First things first: Do you want to create a new game, or load an existing one?")
    print("(Note: if you've never played before, you want to select New Game.)")
    print("")  # Padding
    neworload = input("New Game ('new') or Load Save ('load')? ")
    while True:
        if ("NEW" in neworload.upper()):
            # The user wants to make a new game.
            print("All right! Let's get started!")
            # Let's get the user's chosen name.
            name = input(
                "First of all, let's get your leader's name (or leave blank for a random one): ")
            if (name == ""):
                print("Random name coming right up. Your name is...")
                name = random.choice(names)
                print(f"{name}!")
            else:
                print(f"OK, welcome {name}!")
            # Now let's get the user's country.
            ctry = input(
                "Next, pick a country to 'lead' (or, again, leave blank for a random one): ")
            if (ctry == ""):
                print("Random country coming right up. Your nation is...")
                ctry = random.choice(countries)
                print(f"{ctry}!")
            else:
                print(f"OK, {ctry} it is!")
            # Generate a profile.
            print("Generating your game...")

        elif ("LOAD" in neworload.upper()):
            # The user wants to load an existing save.
            print("Not Implemented - Coming Soon!")


# MAIN GAME LOOP
# This is the main loop of the game; where player input is recieved and processed. All the other functions are called from here.


def run():
    while True:
        pass


# STARTER
# This line starts the init() program, which in turn starts everything else.
init()
display(Country("New Zealand", "Conor"))
