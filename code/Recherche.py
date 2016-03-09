from Activite import *
import sqlite3
from Equipement import *

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


    def activiteRechercheByCom(self, ComLib):
        """
        Methode qui recherche une activité avec son nom
        Retourne son nom, le nom de la commune, l'ID de l'activité et l'ID de l'équipement associé
        """
        req = "select ActLib, ComLib, Id, EquipementId from activite where ComLib like '%" + ComLib + "%';"
        self.c.execute(req)
        row = self.c.fetchone()
        listeAct = []
        while row is not None:
            ActLib, ComLib, Id, EquipementId = row
            act = Activite(ActLib, ComLib, Id, EquipementId)
            listeAct.append(act)
            row = self.c.fetchone()
        return listeAct
    def sportEqResearchByEqu(self,equip):
        """
        Methode qui recherche un équipement par son nom
        """
        req = "select ComInsee, ComLib, InsNom, EquipementId, EquNom from equipement where EquNom like '%" + equip + "%';"
        self.c.execute(req)
        row = self.c.fetchone()
        liste = []
        while row is not None:
            insee,comlib,insnom,equid,equnom = row
            equ = Equipement(insee,comlib,insnom,equid,equnom)
            liste.append(equ)
            row = self.c.fetchone()
        return liste

    def sportEqResearchByDep(self,dep):
        """
        Methode qui recherche un équipement par son nom
        """
        req = "select ComInsee, ComLib, InsNom, EquipementId, EquNom from equipement where ComInsee like '" + dep + "%';"
        self.c.execute(req)
        row = self.c.fetchone()
        liste = []
        while row is not None:
            insee,comlib,insnom,equid,equnom = row
            equ = Equipement(insee,comlib,insnom,equid,equnom)
            liste.append(equ)
            row = self.c.fetchone()
        return liste
