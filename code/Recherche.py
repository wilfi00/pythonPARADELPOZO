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
        listeAct = []
        try:
            req = "select ActLib, ComLib, Id, EquipementId from activite where ActLib like '%" + nomAct + "%';"
        except TypeError:
            print("Wrong input")
        else:
            try:
                self.c.execute(req)
            except sqlite3.Error:
                print("SQL error")
            else:
                row = self.c.fetchone()
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
        listeAct = []
        try:
            req = "select ActLib, ComLib, Id, EquipementId from activite where ComLib like '%" + ComLib + "%';"
        except TypeError:
            print("Wrong input")
        else:
            try:
                self.c.execute(req)
            except sqlite3.Error:
                print("SQL error")
            else:
                row = self.c.fetchone()
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
        liste = []
        try:
            req = "select ComInsee, ComLib, InsNom, EquipementId, EquNom from equipement where EquNom like '%" + equip + "%';"
        except TypeError:
            print("Wrong input")
        else:
            try:
                self.c.execute(req)
            except sqlite3.Error:
                print("SQL error")
            else:
                row = self.c.fetchone()
                while row is not None:
                    insee,comlib,insnom,equid,equnom = row
                    equ = Equipement(insee,comlib,insnom,equid,equnom)
                    liste.append(equ)
                    row = self.c.fetchone()
        return liste

    def sportEqResearchByDep(self,dep):
        """
        Methode qui recherche un équipement par son département
        """
        liste = []
        try:
            req = "select ComInsee, ComLib, InsNom, EquipementId, EquNom from equipement where ComInsee like '" + dep + "%';"
        except TypeError:
            print("Wrong input")
        else:
            try:
                self.c.execute(req)
            except sqlite3.Error:
                print("SQL error")
            else:
                row = self.c.fetchone()
                while row is not None:
                    insee,comlib,insnom,equid,equnom = row
                    equ = Equipement(insee,comlib,insnom,equid,equnom)
                    liste.append(equ)
                    row = self.c.fetchone()
        return liste

rechercheTest = Recherche()
rechercheTest.sportEqResearchByDep("44")
