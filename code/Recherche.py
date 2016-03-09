# -*- coding: utf-8 -*-
from Activite import *
import sqlite3
import Equipement

class Recherche :
    """ Classe qui effectue des recherches en utilisant les objets Activites et Equipements """

    def __init__(self):
        self.conn = sqlite3.connect('../data.db')
        self.c = self.conn.cursor()

    def __del__(self):
        """Destructeur de la classe"""
        self.conn.close()

    def activiteRecherche(self, nomAct):
        """
        Methode qui recherche une activité avec son nom
        Retourne son nom, le nom de la commune, l'ID de l'activité et l'ID de l'équipement associé
        """
        req = "select ActLib, ComLib, Id, EquipementId from activite where ActLib like '%" + nomAct + "%';"
        self.c.execute(req)
        row = self.c.fetchone()
        listeAct = []
        while row is not None:
            ActLib, ComLib, Id, EquipementId = row
            act = Activite(ActLib, ComLib, Id, EquipementId)
            listeAct.append(act)
            row = self.c.fetchone()
        return listeAct


    """
    def sportEqResearch(eq, numLib):
        if numLib == 0:
            req = "select ComLib, EquNom from equipement where EquNom like '%" + eq + "%';"
        else:
            req = "select ComLib, EquNom from equipement where EquNom like '%" + eq + "%' and ComInsee like '" + str(numLib) + "%';"
        c.execute(req)
        row = c.fetchone()
        while row is not None:
            print(row)
            row = c.fetchone()
    """

maRecherche = Recherche()
listeAct = maRecherche.activiteRecherche("Foot")
maRecherche.__del__()
for i in listeAct:
    print(i)
