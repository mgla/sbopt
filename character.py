# -*- coding: utf-8 -*-

from buffs import *

class character:

    def __init__(self,
                 level = 70,
                 wowClass = "Hexenmeister",
                 race = "Gnom",

                 buffs = buffs(),

                 strength = 0,
                 agility = 0,
                 intellect = 0,
                 stamina = 0,
                 spirit = 0,

                 spelldamage = 0,
                 spellhitrating = 0,
                 spellcritrating = 0,
                 spellhasterating = 0,


                 hitrating = 0,
                 critrating = 0,

                 specials = {},
                 skills = {},
                 ):
        self.level =  level = 70
        self.wowClass = wowClass
        self.race = race
        # buffs
        self.buffs = buffs
        #Basisdaten
        self.strength = strength
        self.agility = agility
        self.intellect = intellect
        self.stamina = stamina
        self.spirit = spirit

        #Casterzeug
        self.spelldamage = spelldamage
        self.spellhitrating = spellhitrating
        self.spellcritrating = spellcritrating
        self.spellhasterating = spellhasterating

        #meleezeug
        self.hitrating = hitrating
        self.critrating = critrating

        self.specials = {}
        self.skills = {}
        if self.wowClass == "Hexenmeister":
            self.skills["Verbesserter Schattenblitz"]   = 0
            self.skills["Dunkle Macht"]                 = 0
            self.skills["Verwüstung"]                   = 0
            self.skills["Schatten und Flamme"]          = 0
            self.skills["Heimzahlen"]                   = 0
            self.skills["Verderben"]                    = 0
            self.skills["Dämonische Umarmung"]          = 0
            self.skills["Teufelsintelligenz"]           = 0
            self.skills["Dämonische Ägide"]             = 0
            self.skills["Schattenbeherrschung"]         = 0
            self.skills["Dämonische Taktiken"]          = 0
            self.skills["Meister der Dämonologie"]      = 0
            self.skills["Dämonisches Wissen"]           = 0
            self.skills["Seelenverbindung"]             = 0
            self.specials["metagem"]                    = False

        for skill in skills:
            self.skills[skill] = skills[skill]
        for special in specials:
            self.specials[special] = specials[special]
