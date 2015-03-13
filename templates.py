# -*- coding: utf-8 -*-


# This file contains templates for specific character, buff and debuffsets, etc.
from character import *
from buffs import *

def Zakharov(buffs):
    """ Zakharov of Eredar
        Stand: 3. September 2008"""
    spelldamage = 1240
    spellhitrating = 210
    spellcritrating = 250
    spellhasterating = 201
    intellect = 468
    spirit= 181
    strength = 52
    agility = 67
    stamina = 681
    lbuffs = buffs
    race="Gnom"
    specials = {"metagem": True}
    skills = {"Verbesserter Schattenblitz" : 5,
              "Dunkle Macht": 5,
              "Verwüstung" : 5,
              "Schatten und Flamme" : 5,
              "Heimzahlen" : 3,
              "Verderben" : 1,
              "Dämonische Umarmung" : 5,
              "Teufelsintelligenz" : 3,
              "Dämonische Ägide" : 3,
             }
    return character( spelldamage       = spelldamage,
                      spellhitrating    = spellhitrating,
                      spellcritrating   = spellcritrating,
                      spellhasterating  = spellhasterating,
                      intellect         = intellect,
                      spirit            = spirit,
                      strength          = strength,
                      agility           = agility,
                      stamina           = stamina,
                      buffs             = lbuffs,
                      race              = race,
                      skills            = skills,
                      specials          = specials)

def Aurian(buffs):
    """ Aurian of Eredar
        Stand: 29. Juli 2008"""
    wowClass = "Hexenmeister"
    level = 70
    spelldamage = 1213
    spellhitrating = 200
    spellcritrating = 250
    spellhasterating = 76
    intellect = 460
    spirit= 170
    strength = 57
    agility = 64
    stamina = 698
    lbuffs = buffs
    race="Mensch"
    specials = {"metagem": True}
    skills = {"Verbesserter Schattenblitz" : 5,
              "Dunkle Macht": 5,
              "Verwüstung" : 5,
              "Schatten und Flamme" : 5,
              "Heimzahlen" : 3,
              "Verderben" : 1,
              "Dämonische Umarmung" : 5,
              "Teufelsintelligenz" : 3,
              "Dämonische Ägide" : 3,
             }
    return character( spelldamage       = spelldamage,
                      spellhitrating    = spellhitrating,
                      spellcritrating   = spellcritrating,
                      spellhasterating  = spellhasterating,
                      intellect         = intellect,
                      spirit            = spirit,
                      strength          = strength,
                      agility           = agility,
                      stamina           = stamina,
                      buffs             = lbuffs,
                      race              = race,
                      skills            = skills,
                      specials          = specials
                      )

def FullRaidBuffs():
    lBuffs = buffs(
    specials= {
        "Succubus opfern" : True,
        "Segen der Könige": True,
        # Wer weiß wofür das noch gut ist
        "Alchimistenstein":  True,
        "4 Teile T6": True,
        "ISB immer aktiv": False,
        "Verbessertes Machtwort: Seelenstärke" : 2,
        "Verbesserter Göttlicher Willen": 2,
        "Teufelsrüstung": True,
        "Seelenverbindung": False,
               },
    spelldamage = {"Zauberöl": 42,
                   "Flask": 70,
                   "Bufffood": 23,
                   # Ikone des Silberwappens: Klick-Buff bringt 25.8333 Zauberschaden permanent
#                   "Ikone des Silberwappens": (25.8) + (1/30),
                   # Verhexter Schrumpfkopf: Klick-Buff bringt 35.1666 Zauberschaden permanent
#                   "Verhexter Schrumpfkopf": (35.1) + (2/30),                   
                   # Scharfsinnsanhaenger der Zerschmetterten Sonne: Proc bringt ziemlich genau 20 Spelldmg
#                   "Scharfsinnsanhänger der Zerschmetterten Sonne": 20
                   },
    spellhit = {"wrath of the air - hit": 3,
                "Inspiring Presence" : 1},
    spellcrit = { "wrath of the air - crit": 3,
                  "Aura des Mondkins": 5},
    spellhasterating = {
        # Der Schädel des Gul'dan: 29,166666 Zaubertempo
        "Der Schädel des Gul'dan": (29.1) + (2/30),
                },
    intellect = {"Arcane Intellect": 40,
                 "Mal der Wildnis": 14},
    spirit = {"Göttlicher Willen": 50,
              "Bufffood": 20,
              "Mal der Wildnis": 14,
              },
    stamina= {"Mal der Wildnis": 14,
              "Machtwort: Seelenstärke": 79,
              },
    )
    return lBuffs

def FullRaidDebuffs():
    debuffs = {}
    debuffs['Fluch der Elemente'] = True
    debuffs['Verhängnis'] = 3
    debuffs['Schattenwirken'] = True
    debuffs['Elend'] = 5
    debuffs['Verbessertes Siegel des Kreuzfahrers'] = 3
    debuffs["ISB-Debuff"] = True
    return debuffs
