class Activite :
    """ Classe qui définit l'objet activité avec son nom, le nom de la commune, l'ID de l'activité et l'ID de l'équipement """

    def __init__(self, ActLib, ComLib, Id, EquipementId):
        self.nomAct = ActLib
        self.comAct = ComLib
        self.Id = Id
        self.EquipementId = EquipementId


    def __str__(self):
        """ Méthode pour afficher une activité """
        actStr = "L\'activité " + self.nomAct + " se pratique à " + self.comAct + " (Id : " + self.Id + " ; EquipementId : " + self.EquipementId + ")"
        return actStr
