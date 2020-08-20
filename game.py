# ABOUT THIS PROGRAM
# This is a game written for a Computer Science project.
# It is NOT intended, guaranteed or assured that its simulation will be accurate, and should not be used for any such purpose.
# Program and any accompanying materials (c) Conor Eager 2020.

# IMPORT STATEMENTS
import datetime


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
    supp = 0
    test = 0
    comp = 50
    happ = 50
    econ = 50


class CoronaStats:
    # This class describes a time period's COVID statistics (cases/deaths/recoveries).
    c = 0
    d = 0
    r = 0


class Country:
    # This class represents the player (as the country they are governing). It stores the player's information.
    def __init__(self, n, l):
        self.country = n
        self.leader = l
    measures = Measures([])
    statistics = [CoronaStats()]


class Save:
    # This class represents a save file. Creating and loading save files is done/processed through these objects.
    def __init__(self, n, d):
        timestamp = datetime.datetime.now()
        name = n
        data = player

