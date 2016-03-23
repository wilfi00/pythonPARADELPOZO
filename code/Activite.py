class Activite :
    """ Classe qui définit l'objet activité avec son nom, le nom de la commune, l'ID de l'activité et l'ID de l'équipement """

    def __init__(self, ActLib, ComLib, Id, EquipementId):
        self.nomAct = ActLib
        self.comAct = ComLib
        self.Id = str(Id)
        self.EquipementId = str(EquipementId)


    def __str__(self):
        """ Méthode pour afficher une activité """
        actStr = "L\'activité " + self.nomAct + " se pratique à " + self.comAct + " (Id : " + self.Id + " ; EquipementId : " + self.EquipementId + ")"
        return actStr

    def __eq__(self, other):
        """Redefinition de equals"""
        return (self.nomAct == other.nomAct and self.comAct == other.comAct and self.Id == other.Id and self.EquipementId == other.EquipementId)

    def toJSON(self):
        """Return the JSON string representing the object"""
        return {'actLib' : self.nomAct,'comLib' : self.comAct,'id' : self.Id,'equID' : self.EquipementId}
