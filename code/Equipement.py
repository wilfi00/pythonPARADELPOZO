#!/usr/bin/python3

class Equipement :
    """Classe permettant la modélisation d'un équipement sportif"""

    def __init__(self,insee,lib,iNom,eID,nom) :
        self.comInsee = insee
        self.comLib = lib
        self.inst = iNom
        self.equID = eID
        self.equNom = nom

    def __str__(self) :
        """Formatage de l'affichage d'un équipement"""
        return "[" + self.comInsee + "] " + self.comLib + " - " + self.inst + " -> " + self.equNom + " (ID : " + self.equID + ")"

    def __eq__(self, other):
        """Redefinition de equals"""
        return (self.comInsee == other.comInsee and self.comLib == other.comLib and self.inst == other.inst and self.equID == other.equID and self.equNom == other.equNom)
