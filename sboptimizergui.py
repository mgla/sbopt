# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
import shadowboltDPS
from character import *
from buffs import *
import templates

class sboptimizerGUI:

    def toggleDebuff(self, widget, data=None):
        self.debuffs[data] = self.CBDebuffs[data].get_active()
        self.calcDPS()

    def spinDebuff(self, widget, data=None):
        self.debuffs[data] = self.SBDebuffs[data].get_value()
        self.calcDPS()

    def calcDPS(self):
        " Callback calcDPS-Button"
        c = templates.Zakharov(self.buffs)
        res = shadowboltDPS.calculateDPS(c, self.debuffs)
        self.LabelDPS.set_markup(('<span size="15">DPS: %4d </span>') % res["DPS"])
#        self.LabelDPS.set_label("DPS: %4d" % res["DPS"] )

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        # DPS-Rechnung initialisieren
        # Volle Buffs und Debuffs
        self.debuffs = templates.FullRaidDebuffs()
        self.buffs   = templates.FullRaidBuffs()



        #### GUI ####
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("sboptimizerGUI")

        # handler exit gtk
        self.window.connect("delete_event", self.delete_event)

        self.window.set_border_width(10)
        self.CBDebuffs = {}
        self.SBDebuffs = {}
## VBox DebuffsBool
## VBox DebuffsVal
        self.VBoxDebuffs     = gtk.VBox(True, 0)
        self.VBoxDebuffsBool = gtk.VBox(True, 0)
        self.VBoxDebuffsVal  = gtk.VBox(True, 0)
        for db in self.debuffs:
            # Wenn Boolscher Buff
            if (self.debuffs[db] is True) or (self.debuffs[db] is False):
                self.CBDebuffs[db] = gtk.CheckButton(db)
                self.CBDebuffs[db].set_active(self.debuffs[db])
                self.CBDebuffs[db].connect("toggled", self.toggleDebuff, db)
                self.VBoxDebuffsBool.pack_start(self.CBDebuffs[db])
                self.CBDebuffs[db].show()
            else:
                spinbox = gtk.VBox(True, 0)
                label = gtk.Label(db)
                # TODO: MaxValues eintragen
                self.SBDebuffs[db] = gtk.SpinButton(gtk.Adjustment(value= self.debuffs[db],
                                                                   upper= 5,
                                                                   step_incr = 1
                                                                   ),
                                                    1,0)
                self.SBDebuffs[db].connect("value_changed", self.spinDebuff, db)
                spinbox.pack_start(label)
                label.show()
                spinbox.pack_start(self.SBDebuffs[db])
                self.VBoxDebuffsVal.pack_start(spinbox)
                spinbox.show()
                self.SBDebuffs[db].show()

        self.VBoxDebuffs.pack_start(self.VBoxDebuffsBool)
        self.VBoxDebuffs.pack_start(self.VBoxDebuffsVal)
        self.VBoxDebuffsBool.show()
        self.VBoxDebuffsVal.show()
## VBox Results
        self.VBoxResults = gtk.VBox(False, 2)
        # button calc
        self.buttonCalcDPS = gtk.Button("the useless Button")
#        self.buttonCalcDPS.connect("clicked", self.calcDPS)
        self.VBoxResults.pack_start(self.buttonCalcDPS, False)
        self.buttonCalcDPS.show()

        # label ergebnis
        self.LabelDPS = gtk.Label()
        self.calcDPS()
        self.LabelDPS.set_selectable(True)
        self.VBoxResults.pack_start(self.LabelDPS, False)
        self.LabelDPS.show()
        self.VBoxResults.show()
## Hbox Beides
        self.HBoxAll = gtk.HBox(True, 0)
        self.window.add(self.HBoxAll)

        self.HBoxAll.pack_start(self.VBoxDebuffs)
        self.VBoxDebuffs.show()
        self.HBoxAll.pack_start(self.VBoxResults, True, True, 0)
        self.HBoxAll.show()

        # Destroyer
        self.window.connect("destroy", self.destroy)
        # Fenster zeigen
        self.window.show()

    def main(self):

        # Auf Events warten
        gtk.main()

# Wenn Programm direkt gestartet wird, dann GUI starten
if __name__ == "__main__":
    GUI = sboptimizerGUI()
    GUI.main()
