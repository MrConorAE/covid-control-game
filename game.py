# ABOUT THIS PROGRAM ##############################################################################
# This is a game written for a Computer Science project.
# It is NOT intended, guaranteed or assured that its simulation will be accurate, and should not be used for any such purpose.
# Program, code, output, assets and any accompanying materials (c) Conor Eager 2020. All rights reserved.

# IMPORT STATEMENTS ###############################################################################
# Import the 'datetime' module - for managing dates and times.
import datetime
# Import the 'time' module - for managing times (e.g. delays).
import time
# Import the 'random' module - for generating random numbers.
import random
# Import the 'math' module - for doing advanced mathematics.
import math
# Import the 're' module - for regular expressions.
import re
# Import the 'sys' module - for interacting with the system.
import sys

# NOTE ABOUT THE NUMBER 0/0.001: ##################################################################
# To avoid ZeroDivisionErrors, anywhere the value 0 may be used, 0.001 may be used instead. As the display is only to 2dp, it makes a neglegible difference.
# The code has been modified to also account for this (i.e. doing calculations with 0, but replacing with 0.001 if the result is 0).

# DATA STRUCTURES #################################################################################
# This section defines the various data structures/classes used to store and manage data in this program.


class Option:
    # This class describes an option the player can "activate" (start enforcing).
    def __init__(self, C, n, d, s, t, c, h, e):
        self.catg = C
        self.name = n
        self.desc = d
        self.supp = s
        self.test = t
        self.comp = c
        self.happ = h
        self.econ = e
    actv = False


class OptionCategory:
    # This class describes a category of options the player can choose from.
    def __init__(self, k, t, o: Option):
        self.key = k
        self.title = t
        self.list = o


class Measures:
    # This class describes the total/sum of all the players' chosen Options.
    def __init__(self, a, s, t, c, h, e):
        self.optn = a
        self.supp = s
        self.test = t
        self.comp = c
        self.happ = h
        self.econ = e


class CoronaStats:
    # This class describes a time period's COVID statistics (cases/deaths/recoveries).
    def __init__(self, c, t, d, r, a, i):
        self.dcse = c
        self.tcse = t
        self.dead = d
        self.recv = r
        self.actv = a
        self.inft = i


class Country:
    # This class represents the player (as the country they are governing). It stores the player's information.
    def __init__(self, n, l):
        self.ctry = n
        self.name = l
    msrs = [Measures([Option("R", "None", "No restrictions at all.",
                             0, 0, 0, -0.1, 0),
                      Option("E", "None", "No economic policies in effect.",
                             0, 0, 0, -0.1, 0),
                      Option("T", "None", "No testing at all.",
                             0, 0, 0, -0.1, 0),
                      Option("M", "None", "No mandates enforced.",
                             0, 0, 0, -0.1, 0),
                      Option("H", "None", "No happiness measures.",
                             0, 0, 0, -0.1, 0)],
                     0, 0, 90, 50, 50),
            Measures([Option("R", "None", "No restrictions at all.",
                             0, 0, 0, -0.1, 0),
                      Option("E", "None", "No economic policies in effect.",
                             0, 0, 0, -0.1, 0),
                      Option("T", "None", "No testing at all.",
                             0, 0, 0, -0.1, 0),
                      Option("M", "None", "No mandates enforced.",
                             0, 0, 0, -0.1, 0),
                      Option("H", "None", "No happiness measures.",
                             0, 0, 0, -0.1, 0)],
                     0, 0, 90, 50, 50),
            Measures([Option("R", "None", "No restrictions at all.",
                             0, 0, 0, -0.1, 0),
                      Option("E", "None", "No economic policies in effect.",
                             0, 0, 0, -0.1, 0),
                      Option("T", "None", "No testing at all.",
                             0, 0, 0, -0.1, 0),
                      Option("M", "None", "No mandates enforced.",
                             0, 0, 0, -0.1, 0),
                      Option("H", "None", "No happiness measures.",
                             0, 0, 0, -0.1, 0)],
                     0, 0, 90, 50, 50)]
    # The first item in this array is the totals.
    stat = [CoronaStats(1, 100, 0, 0, 1, 1),
            CoronaStats(1, 100, 0, 0, 1, 1),
            CoronaStats(0, 0, 0, 0, 1, 1)]
    turn = 0
    date = datetime.datetime(2020, 1, 1)


class SaveFile:
    # This class represents a save file. Creating and loading save files is done/processed through these objects.
    def __init__(self, n, d):
        time = datetime.datetime.now()
        name = n
        data = d

# VARIABLES #######################################################################################
# These are (mainly) the instances of the classes defined above.


# The player (and all their data) is stored in this ONE variable... (._.)
player = None
# This array holds OptionCategory objects, representing the options the user can activate/deactivate.
# All the available options to the user are hard-coded here.
options = [
    OptionCategory("R", "Restrictions", [
        Option("R", "None", "No restrictions at all.",
               0, 0, 0, -0.1, 0),
        Option("R", "Gathering Limit 100", "No events can be held with >100 people.",
               10, 0, -0.05, 0, -0.1),
        Option("R", "Gathering Limit 10", "No events can be held with >10 people.",
               20, 0, -0.05, +0.1, -0.2),
        Option("R", "Social Distancing Compulsory", "Social distancing must be observed at all times.",
               30, 0, -0.1, +0.5, -0.5),
        Option("R", "Masks Compulsory", "A mask or face covering must be worn at all times.",
               40, 0, -0.2, +0.2, -1),
        Option("R", "Schools and Workplaces Closed", "All those who can work or learn from home must do so.",
               50, 0, -0.5, +0.1, -2),
        Option("R", "Businesses Closed", "All businesses' physical premises must close, excepting essentials.",
               60, 0, -1, -0.2, -4),
        Option("R", "Isolation of Vulnerable Population", "Vulnerable persons (over 70, immunocompromised) must stay home.",
               70, -2, -2, -0.5, -6),
        Option("R", "Martial Law and Curfews", "The military is brought in to enforce measures.",
               80, -15, -1, -5, -8),
        Option("R", "Full Lockdown", "Nobody can leave their property for any reason (execpt for food/supplies).",
               95, -25, 5, -10, -10)
    ]),
    OptionCategory("E", "Economy", [
        Option("E", "None", "No economic policies.",
               0, 0, 0, -0.1, 0),
        Option("E", "Single Handout", "One-off handout of $1,000.",
               0, 0, 0, 1, 2),
        Option("E", "Single Large Handout", "One-off handout of $2,500.",
               0, 0, 0, 1.1, 2),
        Option("E", "Small Loans", "Interest-free loan of $5,000.",
               0, 0, 0, 1.2, 5),
        Option("E", "Large Loans", "Interest-free loan of $8,000.",
               0, 0, 0, 1.5, 5.5),
        Option("E", "50% Subsidy", "Wage subsidy for businesses that have lost 50% or more.",
               0, 0, 0, 2, 5.75),
        Option("E", "30% Subsidy", "Wage subsidy for businesses that have lost 30% or more.",
               0, 0, 0, 2.5, 3),
        Option("E", "Full Subsidy", "Wage subsidy for businesses that have lost any amount.",
               0, 0, 0, 3, 1)
    ]),
    OptionCategory("T", "Testing & Tracing", [
        Option("T", "None", "No testing at all.",
               0, 0, 0, -0.1, 0),
        Option("T", "Contact Tracing", "Contacts of positive cases are tested.",
               0, 5, -0.01, 0, -0.2),
        Option("T", "Symptomatic Citizens", "Any symptomatic citizen can get tested.",
               0, 15, -0.05, 0.5, -0.5),
        Option("T", "Medical Staff", "All medical and healthcare workers are tested.",
               0, 20, -0.1, 0.7, -0.7),
        Option("T", "New Arrivals", "All new arrivals to the country are tested on entry.",
               0, 40, -0.5, 1, -1),
        Option("T", "Border Staff", "Border staff/workers are tested.",
               0, 50, -0.5, 1.2, -1.2),
        Option("T", "Random Testing", "Random population testing in confirmed case regions.",
               0, 60, -1, 1.5, -1.5),
        Option("T", "Broad Random Testing", "Random population testing everywhere.",
               0, 65, -1, 1, -1.7),
        Option("T", "Everyone", "Everybody is eligible to get a test.",
               0, 75, -2, 0.5, -2),
    ]),
    OptionCategory("M", "Mandates", [
        Option("M", "None", "No mandates in effect.",
               0, 0, 0, -0.1, 0),
        Option("M", "Contact Tracing App", "Develop a contact tracing app for your citizens to use.",
               0, 10, 0.1, 0.1, 0),
        Option("M", "Mandatory Contact Tracing App", "All citizens must use the contact tracing app.",
               0, 15, 0, 0, 0),
        Option("M", "Start Vaccine Development", "Start developing a vaccine.",
               0, 0, 0, 5, -1)
    ]),
    OptionCategory("H", "Happiness", [
        Option("H", "None", "No happiness measures.",
               0, 0, 0, -0.1, 0),
        Option("H", "Small Advertising Campaign", "Run a small advertising campaign to inform.",
               0, 0, 0, 1, -0.01),
        Option("H", "Large Advertising Campaign", "Run a large advertising campaign to inform people.",
               0, 0, 0, 2, -0.02),
        Option("H", "Social Media Updates", "Send out updates on official social media channels.",
               0, 0, 0, 4, -0.03),
        Option("H", "Frequent Social Media Updates", "Send out updates on official social media channels daily.",
               0, 0, 0, 6, -0.04),
        Option("H", "Weekly Press Conferences", "Run weekly press conferences, shown live on state TV.",
               0, 0, 0, 8, -0.05),
        Option("H", "Daily Press Conferences", "Run daily press conferences, shown live on state TV.",
               0, 0, 0, 10, -0.06),
    ])]
# Names (generated randomly) for when the user doesn't enter one.
names = ["Lewis", "Mark", "Tim", "Chris", "Theodore", "Charlie", "Alexander", "Brian", "Carl",
         "Peter", "Lydia", "Addie", "Alexandra", "Annie", "Victoria", "Julia", "Harriet", "Sadie"]
# Countries (generated randomly, fictitious) for when the user doesn't want to pick one.
countries = ["Tacxoem", "Guitu", "Markuin Isles", "Alza",
             "Befolk", "North Hongland", "Ofmai", "Pagrice", "Stanri"]

# FUNCTIONS #######################################################################################
# These are functions that do things! (Wow! Who knew?)


def calculateMeasures(m):
    # This function calculates new values for the metrics used in this game from the measures currently active.
    #
    # This function expects an array of Measures objects to be passed to it (m), containing at least 3 items.
    #
    # This function returns a new Measures object, to replace the original item in a Measures array.
    #
    s = 0  # Suppression
    t = 0  # Testing
    c = m[1].happ  # Compliance (is happiness with a 1 week lag)
    h = m[0].happ  # Happiness
    e = m[0].econ  # Economy
    for o in m[0].optn:
        s = s + o.supp
        t = t + o.test
        c = c + o.comp
        h = h + o.happ
        e = e + o.econ
    # Apply a +/- multiplier to Happiness if Economy is high/low, respectively
    if (e < 25):
        h = h * 0.9
    elif (e > 75):
        h = h * 1.1
    # For each metric, if it's higher than 100 or lower than 0, "level" it
    s = s if s > 0 else 0.001
    s = s if s < 100 else 100
    t = t if t > 0 else 0.001
    t = t if t < 100 else 100
    c = c if c > 0 else 0.001
    c = c if c < 100 else 100
    h = h if h > 0 else 0.001
    h = h if h < 100 else 100
    e = e if e > 0 else 0.001
    e = e if e < 100 else 100
    # Return a new Measures object containing the new values
    # From L to R: options, suppression, testing, compliance, happiness, and economy
    return Measures(m[0].optn, s, t, c, h, e)


def calculateCOVID(m, s):
    # This function calculates the country's new COVID-19 statistics, based on 3 metrics -
    # Suppression, Testing and Compliance. They are used to calculate a new Infection rate, which then is used to
    # generate dcse/death/recovery numbers.
    #
    # This function expects an array of Measures objects (m) to be passed, with at least one item (totals),
    # and an array of CoronaStats objects (s) to be passed, with at least two items (totals and last turn).
    #
    # This function returns a new CoronaStats object, to be appended to a Country.stat array.
    #
    # Make "shortcuts" to the last Measures and last CovidStats objects:
    # Using the Measures from 2 turns (weeks) back, to account for the "lag time"
    totalCovid = s[0]
    lastCovid = s[1]
    # Get the last turn's numbers (we're using these):
    discoveredCases = lastCovid.dcse
    actualCases = lastCovid.tcse
    deaths = lastCovid.dead
    recoveries = lastCovid.recv
    active = lastCovid.actv
    # This is the maximum multiplier. Adjust as neccesary for difficulty or tuning.
    maxR = 2.5
    # Calculate a case multiplier.
    # 5 - (Suppression * (Compliance / 100)) / 20
    multiplier = maxR - (m[2].supp *
                         (m[2].comp / 100)) / (100/maxR)
    # Calculate the number of new cases (last * multiplier).
    newActualCases = math.ceil(actualCases * multiplier)
    # Calculate the number of discovered cases (actual * testing).
    newDiscoveredCases = math.ceil(newActualCases * (m[1].test / 100))
    # Calculate the number of new deaths (last * mortality (0.01 - 0.05))
    newDeaths = math.ceil(actualCases * random.uniform(0.01, 0.05))
    # Calculate the number of new recoveries (last * recovery (0.5 - 0.8))
    newRecoveries = math.ceil(discoveredCases * random.uniform(0.5, 0.8))
    # Calculate a transmission rate, checking for 0 (ZeroDivisionError)!
    try:
        newTransmission = (newDiscoveredCases /
                           discoveredCases) if (discoveredCases == 0) else 0.001
    except ZeroDivisionError:
        newTransmission = 0.001
    # Return all of these new numbers in a new CovidStats object.
    return CoronaStats(newDiscoveredCases, newActualCases, newDeaths, newRecoveries, 0, newTransmission)


def calculateCOVIDTotal(s):
    # This function calculates the country's TOTAL COVID-19 statistics (for use in displays and calculations).
    #
    # This function expects an array of CoronaStats objects (s) to be passed, with at least 2 items, and the old Totals object
    # (index 0) to be removed.
    #
    # This function returns a new CoronaStats object, to replace the first item in a Country.stat array.
    #
    # Make variables to keep track of sums.
    discoveredCases = 0
    actualCases = 0
    deaths = 0
    recoveries = 0
    active = 0
    # Go through each CoronaStats object and add up the items.
    for time in s:
        # Skip the first one!
        if time == s[0]:
            continue
        discoveredCases = discoveredCases + time.dcse
        deaths = deaths + time.dead
        recoveries = recoveries + time.recv
    active = discoveredCases - (recoveries + deaths)
    # We return an infection rate of 0 in this object because infection rates don't have totals.
    return CoronaStats(discoveredCases, actualCases, deaths, recoveries, active, 0)


def optionChanges(o, m):
    # This function allows the player to make changes to their activated measures, by browsing and selecting available options.
    #
    # This function expects an array of OptionCategory objects (o) to be passed, and an array of Measures objects (m) with at least one item.
    #
    # This function returns a new Measures object with totals, based on the player's selections.
    #
    oldMeasures = m[0]
    newMeasures = m[0]
    while True:
        print("\n\n")
        print("- MEASURE SELECTION ------------------------------------------------------------------------------------------")
        print("Categories:")
        for c in o:
            print(f"({c.key}) {c.title} - {len(c.list)} option(s)")
        print("")
        print("You can:")
        print(
            "- Enter a Category ID (e.g. 'T') to browse the options in that category,")
        print("- Type an Option ID (e.g. 'T1') to quickly activate that option,")
        print("- or type 'B' to exit Measure Selection and go back.")
        print("")
        selection = input("Category or ID: ")
        print("\n")
        if selection.lower() == "b":
            print("Exiting measure selection.")
            break
        elif (re.search("^([A-Z][0-9]+)$", selection, re.IGNORECASE) != None):
            # This regular expression searches for Option IDs only (letter and a number).
            catNo = 0
            for c in o:
                # Get category first
                if c.key == selection[0].upper():
                    # Check if there are any items in the category
                    if (len(c.list) > 0):
                        # If yes, check if the item specified exists
                        if (len(c.list) > int(selection[1:])):
                            print(
                                f"({selection.upper()}) {c.list[int(selection[1:])].name}\n     {c.list[int(selection[1:])].desc}")
                            print("Is this the measure you want to activate?")
                            while True:
                                confirm = input("Confirm selection (Y/N): ")
                                if (confirm.upper() == "Y"):
                                    print(
                                        f"{c.list[int(selection[1:])].name} activated!")
                                    for item in c.list:
                                        item.actv = False
                                    c.list[int(selection[1:])].actv = True
                                    newMeasures.optn[catNo] = c.list[int(
                                        selection[1:])]
                                    break
                                else:
                                    print(
                                        f"Cancelled. {c.list[int(selection[1:])].name} was not activated.")
                                    input(
                                        "Press ENTER to go back to the categories list.")
                                    break
                        else:
                            print(
                                f"That option ({selection.upper()}) does not exist. Please try again.")
                            input(
                                "Press ENTER to go back to the categories list.")
                            break
                    else:
                        # If no, say so
                        print(
                            f"There are no options in the {c.title} category.")
                        input("Press ENTER to go back to the categories list.")
                        break
                else:
                    catNo = catNo + 1
                    continue
        elif (re.search("^([A-Z])$", selection, re.IGNORECASE) != None):
            # This regular expression searches for Category keys only (letter)
            found = False
            for c in o:
                # Get category first
                if c.key == selection.upper():
                    found = True
                    n = 0
                    # Check if there are any items in the category
                    if (len(c.list) > 0):
                        # If yes, list them
                        print(f"Options in {c.title} category:\n")
                        for i in c.list:
                            print(
                                f"({selection.upper()}{n}) {i.name} {'[ACTIVE]' if i.actv else ''}\n     {i.desc}")
                            n = n + 1
                        input("Press ENTER to go back to the categories list.")
                        break
                    else:
                        # If no, say so
                        print(
                            f"There are no options in the {c.title} category.")
                        input("Press ENTER to go back to the categories list.")
                        break
            if not found:
                print(f"That category ({selection.upper()}) does not exist.")
                input("Press ENTER to go back to the categories list.")
        else:
            print(
                f"'{selection}' doesn't look like a valid ID. Please try again.")
            input("Press ENTER to go back to the categories list.")
            break
    # Calculate the new totals and return.
    return newMeasures


def display(c):
    # This function is based on the development prototype found in display.py. It has been modified (singnificantly) to
    # operate with the new data structure used in this version.
    #
    # This function prints out a human-readable "summary" of information (statistics, metrics) for the player to use.
    #
    # This function expects a Country object to be passed (c).
    #
    try:
        # Add some padding to make it more readable.
        print("\n\n")
        # Print the turn number, date and player name.
        print(
            f"TURN {c.turn:>3} - DATE {c.date.day:02}/{c.date.month:02}/{c.date.year:04} - Prime Minister of {c.ctry}, {c.name}")
        print("- CORONAVIRUS STATISTICS -------------------------------------------------------------------------------------")
        # Print the COVID-19 statistics.
        # WARNING: Item 0 is the totals, Item 1+ are the biweekly values!
        print(f"              STATISTIC                THIS TURN                 TOTAL")
        print(
            f"                 Cases               {c.stat[1].dcse:>+10}            {c.stat[0].dcse:>10}")
        print(
            f"                Deaths               {c.stat[1].dead:>+10}            {c.stat[0].dead:>10}     ({(c.stat[0].dead/c.stat[0].dcse)*100:>5.2f}% Death Rate)")
        print(
            f"            Recoveries               {c.stat[1].recv:>+10}            {c.stat[0].recv:>10}     ({(c.stat[0].recv/c.stat[0].dcse)*100:>5.2f}% Recovery Rate)")
        if ((c.stat[0].actv / c.stat[0].dcse) * 100 < 0):
            # If the Active count is negative (because of low testing and high cases), display something else (the negative values are confusing, according to stakeholder feedback).
            print(
                f"                Active               ---                          ???     (Testing too low to determine!)")
        else:
            print(
                f"                Active               ---                   {c.stat[0].actv:>10}     ({(c.stat[0].actv/c.stat[0].dcse)*100:>5.2f}% Active)")
        print("")
        print("- RATINGS/STATUS ---------------------------------------------------------------------------------------------")
        # Print the Ratings (transmission, testing, suppression, happiness, compliance, economy)
        # WARNING: Item 0+ are the biweekly values!
        print(f"                METRIC                THIS TURN                CHANGE        as %")
        print(
            f"     Transmission Rate               {c.stat[1].inft:>10.2f}            {(c.stat[1].inft-c.stat[2].inft):>+10.2f} {((c.stat[1].inft-c.stat[2].inft)/c.stat[2].inft)*100:>+10.2f}%")
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

# SETUP ###########################################################################################
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
    print("--------------------------------------------------------------------------------------------------------------")
    print("Right. Now that we've got the backstory out of the way, let's get this game started!")
    print("")  # Padding
    print("First things first: Do you want to create a new game, or load an existing one?")
    print("(Note: if you've never played before, you want to select New Game.)")
    print("")  # Padding
    while True:
        neworload = input("New Game ('new') or Load Save ('load')? ")
        if ("N" in neworload.upper()):
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
            print("\n")
            print("- HOW TO PLAY ----------------------------------------------------------------------------------- IMPORTANT! -")
            print("""
In this game, you take on the role of a government trying to control COVID-19. 
You do this (or not) by implementing 'measures' - restrictions, economic policies, etc. - that will influence the 5 core statistics:
Suppression, Testing, Compliance, Happiness and Economy.

You lose if:
 - your let too many get infected (over 10 million),
 - your Economy reaches 0 (economic collapse), or
 - your Happiness reaches 0 (violent revolution).

You win if:
 - you keep your country running long enough to get a vaccine (between 2 and 10 years, depending on difficulty).

Every turn, you have a choice of what to do. The main two options you'll use are Measures ('M') and Next Turn (ENTER).
Each turn is 1 week, so decide wisely - a week can make a BIG difference.
In the Measures screen, you can select which measures to implement/start enforcing. Each measure will have different effects on
the 5 metrics, for better or for worse!

Good luck!""")
            input("Press [ENTER] to start! ")
            break
        elif ("L" in neworload.upper()):
            # The user wants to load an existing save.
            raise NotImplementedError
        else:
            print("Hrm, that doesn't look like a valid option.")
            print("Please type one of the options.")


# STARTER #########################################################################################
# This line starts the init() program, which initialises the variables and does the introduction.
init()

# MAIN GAME LOOP ##################################################################################
# This is the main loop of the game; where player input is recieved and processed. All the other functions are called from here.
while True:
    # Increment the turn counter and date
    player.turn = player.turn + 1
    player.date = player.date + datetime.timedelta(days=7)

    # Display information to the user.
    display(player)

    print("")
    # Give the user the option of changing measures.
    ochanges = None
    while True:
        print("What would you like to do?")
        change = input(
            "Modify Measures ('M'), Save ('S'), Quit ('Q') or Next Turn (ENTER): ")
        if ("m" in change.lower()):
            ochanges = optionChanges(options, player.msrs)
        elif ("s" in change.lower()):
            print("Saving not available yet.")
        elif ("q" in change.lower()):
            print("Are you sure you want to quit?")
            bye = input("Yes or No: ")
            if ("y" in bye.lower()):
                print("OK, bye!")
                sys.exit()
        elif (change.lower() == ""):
            print(f"Starting Turn {player.turn + 1}...")
            break
        else:
            print("Please select an option.")

    # Apply changes.
    try:
        if (ochanges != None):
            player.msrs.insert(0, ochanges)
        else:
            player.msrs.insert(0, player.msrs[0])
    except NameError:
        # If there were no changes, do nothing.
        player.msrs.insert(0, player.msrs[0])

    # Calculate new totals.
    player.msrs[0] = calculateMeasures(player.msrs)

    # Generate new detected case/total case/death/recovery/active numbers.
    player.stat.insert(1, calculateCOVID(player.msrs, player.stat))

    # Replace the first CovidStats object (the totals) with newly calculated ones.
    player.stat[0] = calculateCOVIDTotal(player.stat)

    # Check for win or lose conditions.
    # Win: Survive until year 2022
    # Lose: Economy or Happiness are 0
    if (player.msrs[0].happ <= 0.001):
        # Lose (Happiness)
        print("- GAME OVER -------------------------------------------------------------------------------------- YOU LOSE! -")
        print("""
In a suprise attack, the citizens of your country stormed your residence and violently overthrew you.
You have been exiled for your country, for leading them to ruin.

Game over! You lost because your Happiness reached 0.""")
        print("Thanks for playing!")
        input("Press ENTER to exit. ")
        sys.exit()
    elif (player.msrs[0].econ <= 0.001):
        # Lose (Economy)
        print("- GAME OVER -------------------------------------------------------------------------------------- YOU LOSE! -")
        print("""
After months of economic downturn, the economy of your country has collapsed. Famine and poverty are rife.
You have been exiled for your country, for leading them to ruin.

Game over! You lost because your Economy reached 0.""")
        print("Thanks for playing!")
        input("Press ENTER to exit. ")
        sys.exit()
    elif (player.date.year == 2022):
        # Win
        print("- GAME OVER --------------------------------------------------------------------------------------- YOU WIN! -")
        print("""
After years of research, a vaccine for COVID-19 is finally discovered. Your government starts a massive vaccination campaign.
You have finally overcome this terrible disease, and will probably go down in history!

Game over! You won because you survived long enough to discover a vaccine.""")
        print("Thanks for playing!")
        input("Press ENTER to exit. ")
        sys.exit()
