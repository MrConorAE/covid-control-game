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

# NOTE ABOUT THE NUMBER 0/0.001:
# To avoid ZeroDivisionErrors, anywhere the value 0 may be used, 0.001 may be used instead. As the display is only to 2dp, it makes a neglegible difference.
# The code has been modified to also account for this (i.e. doing calculations with 0, but replacing with 0.001 if the result is 0).

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
    actv = False


class Measures:
    # This class describes the total/sum of all the players' chosen Options.
    def __init__(self, a, i, s, t, c, h, e):
        self.optn = a
        self.inft = i
        self.supp = s
        self.test = t
        self.comp = c
        self.happ = h
        self.econ = e


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
    msrs = [Measures([Option("Test Option", "this is a test option", 10, 0, -0.1, 0.1, -0.1)], 1, 0.001, 0.001, 50, 50, 50),
            Measures([], 1, 0.001, 0.001, 50, 50, 50)]
    stat = [CoronaStats(1, 0, 0, 1), CoronaStats(1, 0, 0, 1)]
    turn = 0
    date = datetime.datetime(2020, 1, 1)


class SaveFile:
    # This class represents a save file. Creating and loading save files is done/processed through these objects.
    def __init__(self, n, d):
        time = datetime.datetime.now()
        name = n
        data = d

# VARIABLES
# These are the instances of the classes defined above.


# The player (and all their data) is stored in this ONE variable...
player = None
# This array holds Option objects, representing the options the user can activate/deactivate.
options = []
# Names (generated randomly) for when the user doesn't enter one.
names = ["Lewis", "Mark", "Tim", "Chris", "Theodore", "Charlie", "Alexander", "Brian", "Carl",
         "Peter", "Lydia", "Addie", "Alexandra", "Annie", "Victoria", "Julia", "Harriet", "Sadie"]
# Countries (generated randomly, fictitious) for when the user doesn't want to pick one.
countries = ["Tacxoem", "Guitu", "Markuin Isles", "Alza",
             "Befolk", "North Hongland", "Ofmai", "Pagrice", "Stanri"]

# FUNCTIONS


def calculateMeasures(m):
    # This function calculates new values for the metrics used in this game from the measures currently active.
    #
    i = 0  # Infection rate
    s = 0  # Suppression
    t = 0  # Testing
    c = 0  # Compliance
    h = 0  # Happiness
    e = 0  # Economy
    for o in m[0].optn:
        s = s + o.supp
        t = t + o.test
        c = c + o.comp
        h = h + o.happ
        e = e + o.econ
    # Return a new Measures object containing the new values
    # From L to R: options, infection, suppression, testing, compliance, happiness, and economy
    return Measures(m[0].optn, (i if i != 0 else 0.001), (s if s != 0 else 0.001), (t if t != 0 else 0.001), (m[0].comp - c), (m[0].happ - h), (m[0].econ - e))


def display(c):
    try:
        # This function is based on the development prototype found in display.py. It has been modified (singnificantly) to
        # operate with the new data structure used in this version (see above).
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
    global player
    global options
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
    while True:
        neworload = input("New Game ('new') or Load Save ('load')? ")
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
                print(f"Hello, {name}!")
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
            player = Country(ctry, name)
            print("Done!")
            input("Press [ENTER] to continue... ")
            break
        elif ("LOAD" in neworload.upper()):
            # The user wants to load an existing save.
            raise NotImplementedError
        else:
            print("Hrm, that doesn't look like a valid option.")
            print("Please type one of the options.")


# STARTER
# This line starts the init() program, which in turn starts everything else.
init()

# MAIN GAME LOOP
# This is the main loop of the game; where player input is recieved and processed. All the other functions are called from here.
while True:
    player.msrs.insert(0, calculateMeasures(player.msrs))
    display(player)
    input("next turn...")
    player.turn = player.turn + 1
