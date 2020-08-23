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
    inft = 0
    supp = 0
    test = 0
    comp = 50
    happ = 50
    econ = 50


class CoronaStats:
    # This class describes a time period's COVID statistics (cases/deaths/recoveries).
    case = 0
    dead = 0
    recv = 0
    actv = 0


class Country:
    # This class represents the player (as the country they are governing). It stores the player's information.
    def __init__(self, n, l):
        self.ctry = n
        self.name = l
    msrs = [Measures([])]
    stat = [CoronaStats()]
    turn = 0
    date = datetime.datetime(2020, 1, 1)


class SaveFile:
    # This class represents a save file. Creating and loading save files is done/processed through these objects.
    def __init__(self, n, d):
        time = datetime.datetime.now()
        name = n
        data = player

# FUNCTIONS


def display(c):
    # This function is based on the development prototype found in display.py. It has been modified (singnificantly) to
    # operate with the new data structure used in this version (see above).
    print(
        f"TURN {c.turn:>3} - DATE {c.date.day:02}/{c.date.month:02}/{c.date.year:03} - Prime Minister of {c.ctry}, {c.name}")
    print("-------------------------------------------------------------------------------------------------------------")
    print(f"CORONAVIRUS STATISTICS                THIS TURN                 TOTAL")
    print(
        f"                 Cases               {c.stat[1].case:>+10}            {c.stat[0].case:>10}")
    print(
        f"                Deaths               {c.stat[1].dead:>+10}            {c.stat[0].dead:>10}     ({(c.stat[0].dead/c.stat[0].case)*100:>5.2f}% Mortality)")
    print(
        f"            Recoveries               {c.stat[1].recv:>+10}            {c.stat[0].recv:>10}     ({(c.stat[0].recv/c.stat[0].case)*100:>5.2f}% Recovery)")
    print(
        f"                Active               {c.stat[1].actv:>+10}                   ---     ({(c.stat[1].actv/c.stat[0].case)*100:>5.2f}% Active)")
    print("-------------------------------------------------------------------------------------------------------------")
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

# SETUP
# This function initialises all the variables in the game, and sets up their data (such as username and age).


def init():
    pass

# MAIN GAME LOOP
# This is the main loop of the game; where player input is recieved and processed. All the other functions are called from here.


def run():
    while True:
        pass


# STARTER
# This line starts the init() program, which in turn starts everything else.
init()
display(Country("New Zealand", "Conor"))
