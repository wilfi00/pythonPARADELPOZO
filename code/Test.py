import unittest
from Recherche import *
from Activite import *

class Test(unittest.TestCase):

    def test_activiteRecherche(self):
        rechercheTest = Recherche()
        activiteTest = Activite("Football / Football en salle (Futsal)", "Abbaretz", 1, 69849)
        self.assertEqual(rechercheTest.activiteRecherche("sdmlqfjksdfjlk"), [])
        self.assertTrue(activiteTest in rechercheTest.activiteRecherche("foot"))

    def test_activiteRechercheByCom(self):
        rechercheTest = Recherche()
        activiteTest = Activite("Football / Football en salle (Futsal)", "Abbaretz", 1, 69849)
        self.assertEqual(rechercheTest.activiteRechercheByCom("sqfdlkjsfdqj"), [])
        self.assertTrue(activiteTest in rechercheTest.activiteRechercheByCom("ABBARETZ"))

    def test_equipementRechercheByCom(self):
        rechercheTest = Recherche()
        equipementTest = Equipement()

        self.assertTrue(True)

    def test_sportEqResearchByDep(self):
        rechercheTest = Recherche()

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
