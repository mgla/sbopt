# -*- coding: utf-8 -*-


from character import *
from buffs import *
import templates

def calculateDPS(char, debuffs):
    "Funktion zur DPS-Berechnung des Schattenblitzes"

    """ TODO:   Meister der Dämonologie
                Dämonisches Wissen
                Teilresists gegen höherlevelige Ziele
    """

    """ TODO:   - versch. Ziele berücksichtigen, z. B. versch. Level
                - Konsistenzcheck Buffs - Talente (ie. Seelenverbindung (Talent <-> Buff)
                  (Buff Seelenverbindung <-> Buff Dämonische Opferung)
    """

    """ TODO:  - Redesign am Buffsystem um nicht immer alles neu machen zu müssen für alles und jeden
                 Irgendwas mit (Aktiv, Buffname, {Attribut: Effekt, Attribut2: Effekt})
    
    """
    # Dictionary für die Ergebnisse der Berechnung
    res = {}
    # Basiscastzeit 3 Sekunden
    castTime = 3.0
    castTime = castTime - char.skills["Dunkle Macht"] * 0.1
    # Zaubertempo durch Buffs
    bonusHaste = 0
    for key in char.buffs.spellhasterating:
        bonusHaste += char.buffs.spellhasterating[key]
    # Zaubertempo anrechnen
    spellHaste = ((char.spellhasterating + bonusHaste) / 15.7) / 100

    castTime = castTime/(1 + spellHaste)
    res["castTime"] = castTime

    # Spelldmgkoeffizient
    spellcoef = 0.857
    spellcoef += char.skills["Schatten und Flamme"] * 0.04
    # 541-603 dmg, rank 10
    minbasedmg = 541
    maxbasedmg = 603
    basedmg = (minbasedmg + maxbasedmg) /2
    # multiplikative sachen
    mult = 1
    if debuffs["Fluch der Elemente"]:
        mult = 1.1 + 0.01 * debuffs["Verhängnis"]
    if debuffs["Elend"] > 0: mult *= 1 + 0.01 * debuffs["Elend"]
    if debuffs["Schattenwirken"]: mult *= 1.1
    if char.buffs.specials["Succubus opfern"] : mult *= 1.15
    mult *= 1+ (0.02 * char.skills["Schattenbeherrschung"])
    if (char.skills["Seelenverbindung"] > 0) and char.buffs.specials["Seelenverbindung"]:
        mult *= 1.05        
    if debuffs["ISB-Debuff"] : mult *= 1.20
    if char.buffs.specials["4 Teile T6"] : mult *= 1.06

    # Zauberschaden durch buffs
    bonusDMG = 0
    for key in char.buffs.spelldamage:
        bonusDMG += char.buffs.spelldamage[key]
    # Zauberschaden durch Dämonische Ägide und Teufelsrüstung
    if char.buffs.specials["Teufelsrüstung"]:
        bonusDMG += 100
        if char.skills["Dämonische Ägide"] > 0:
            bonusDMG += char.skills["Dämonische Ägide"] * 10
    #Zauberschaden durch verb. Willenskraftbuff
    spiritDMG = 0
    if char.buffs.specials["Verbesserter Göttlicher Willen"] > 0:
        bonusSpirit = 0
        for key in char.buffs.spirit:
            bonusSpirit += char.buffs.spirit[key]
        # Abzug durch Dämonische Umarmung    
        if char.skills["Dämonische Umarmung"] > 0:
            bonusSpirit *= (1 - char.skills["Dämonische Umarmung"] * 0.01)
        spirit = char.intellect + bonusSpirit
        #10% von SDK
        if char.buffs.specials["Segen der Könige"]:
            spirit *= 1.1
        spiritDMG = spirit * char.buffs.specials["Verbesserter Göttlicher Willen"] * 0.05
    raw_spelldmg = char.spelldamage + bonusDMG + spiritDMG
    eSpelldmg = spellcoef * raw_spelldmg
    # apply + hit
    bonushit = 0
    for key in char.buffs.spellhit:
        bonushit += char.buffs.spellhit[key]
    res["bonushit"] = bonushit
    hit = (83 +
              min(16, (char.spellhitrating/12.615)
                  + bonushit
                  )
              )
    res["hitchance"] = hit
    eDMG = (basedmg + eSpelldmg) * hit/100
    # apply crit
    # 1.701 ist klassencrit wl
    bonusCritChance = 0
    for key in char.buffs.spellcrit:
        bonusCritChance += char.buffs.spellcrit[key]
    res["bonusCritChance"] = bonusCritChance
    # Zusätzliche Critchance durch Intelligenz
    bonusInt = 0
    for key in char.buffs.intellect:
        bonusInt += char.buffs.intellect[key]

    # Gnomische Rassenfertigkeit, 5% mehr Intelligenz
    if char.race == "Gnom":
        bonusInt *= 1.05
    # Segen der Könige, bringt 10% mehr Intelligenz
    if char.buffs.specials["Segen der Könige"]:
        critFromIntellect = (char.intellect + bonusInt) * 1.1 /82
    else:
        critFromIntellect = (char.intellect + bonusInt)/82
    critChance= 1.701 \
                + critFromIntellect \
                + char.spellcritrating/22.08 \
                + char.skills["Verwüstung"] \
                + char.skills["Heimzahlen"] \
                + char.skills["Dämonische Taktiken"] \
                + bonusCritChance \
                + debuffs["Verbessertes Siegel des Kreuzfahrers"]
    res["critChance"] = critChance
    critChance /= 100
    # Critmultiplikator ausrechnen
    if char.skills["Verderben"] == 1:
        if char.specials["metagem"]:
            critMul = 1.09
        else:
            critMul = 1.0
    else:
        if char.specials["metagem"]:
            critMul = 0.545
        else:
            critMul = 0.5
    # Effektive Critchance aus Critmultiplikator ausrechnen
    effCritChance = critChance * critMul

    # Werte in Ergebniswörterbuch eintragen
    res["effCritChance"] = effCritChance * 100
    avgHit = eDMG * mult
    res["avgHit"] = avgHit

    res["avgCrit"] = avgHit * (critMul + 1)
    avg= eDMG * (1+effCritChance) * mult
    res["avg"] = avg
    res["DPS"] = avg/castTime
    return res

def calcDPS():
    # Maximale Buffs und Debuffs
    debuffs = templates.FullRaidDebuffs()
    buffs = templates.FullRaidBuffs()
    # Modifikatoren zum rumprobieren
    buffs.spelldamage["bonus"] = 0
    # Char erstellen
    c = templates.Zakharov(buffs)
    c.spellhasterating += -30
    c.spelldamage += 36
    debuffs["ISB-Debuff"] = False
    r1 = calculateDPS(c, debuffs)
    debuffs["ISB-Debuff"] = True
    r2 = calculateDPS(c, debuffs)
    print """Analyse -- DPS, Schattenblitz
    %4d DPS aktuell 
    %4d DPS mit ISB aktiv""" \
    % (r1["DPS"],r2["DPS"])

if __name__ == "__main__":
    calcDPS()
