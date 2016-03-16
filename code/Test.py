import unittest
from Recherche import *
from Activite import *

class Test(unittest.TestCase):

    """
    Test de la méthode activiteRecherche
    """
    def test_activiteRecherche(self):
        rechercheTest = Recherche()
        activiteTest = Activite("Football / Football en salle (Futsal)", "Abbaretz", 1, 69849)
        self.assertEqual(rechercheTest.activiteRecherche("sdmlqfjksdfjlk"), [])
        self.assertTrue(activiteTest in rechercheTest.activiteRecherche("foot"))

    """
    Test de la méthode activiteRechercheByCom
    """
    def test_activiteRechercheByCom(self):
        rechercheTest = Recherche()
        activiteTest = Activite("Football / Football en salle (Futsal)", "Abbaretz", 1, 69849)
        self.assertEqual(rechercheTest.activiteRechercheByCom("sqfdlkjsfdqj"), [])
        self.assertTrue(activiteTest in rechercheTest.activiteRechercheByCom("ABBARETZ"))

    """
    Test de la méthode sportEqResearchByEqu
    """
    def test_sportEqResearchByEqu(self):
        rechercheTest = Recherche()
        equipementTest = Equipement("44007", "Avessac", "Site de Ball Trap", "282045", "Ball trap")
        self.assertEqual(rechercheTest.sportEqResearchByEqu("sqfdlkjsfdqj"), [])
        self.assertTrue(equipementTest in rechercheTest.sportEqResearchByEqu("Ball trap"))

    """
    Test de la méthode sportEqResearchByDep
    """
    def test_sportEqResearchByDep(self):
        rechercheTest = Recherche()
        equipementTest = Equipement("44007", "Avessac", "Site de Ball Trap", "282045", "Ball trap")
        self.assertEqual(rechercheTest.sportEqResearchByDep("sqfdlkjsfdqj"), [])
        self.assertTrue(equipementTest in rechercheTest.sportEqResearchByDep("44"))


if __name__ == '__main__':
    unittest.main()
