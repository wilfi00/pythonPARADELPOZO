import unittest
from Recherche import *
from Activite import *

class Test(unittest.TestCase):

  def test_activiteRecherche(self):
      rechercheTest = Recherche()
      activiteTest = Activite("Football / Football en salle (Futsal)", "Abbaretz", 1, 69849)
      self.assertEqual(rechercheTest.activiteRecherche("sqfdlkjsfdqj"), [])

if __name__ == '__main__':
    unittest.main()
