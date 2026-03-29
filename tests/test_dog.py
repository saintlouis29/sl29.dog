"""Module providing tests for dogs"""

import unittest
from sl29.dog.dog import Dog, MatingError

#from src.sl29.dog.dog import Dog, MatingError  # Import relatif


class TestDog(unittest.TestCase):
    def setUp(self):
        # Création des instances de chiens pour les tests
        self.rintintin = Dog(race="Berger allemand", sex="M", name="Rintintin")
        self.scoobydoo = Dog(race="Grand danois", sex="M", name="Scooby-Doo")
        self.rantanplan = Dog(race="Berger allemand", sex="M", name="Rantanplan")
        self.rantanplane = Dog(race="Berger allemand", sex="F", name="Rantanplane")
        self.laika = Dog(race="bâtard", sex="F", name="Laïka")
        self.lassie = Dog(race="Collie", sex="F", name="Lassie")
        self.mirza = Dog(race="bâtard", sex="F", name="Mirza")

    def test_initialization(self):
        # Test de l'initialisation des attributs
        self.assertEqual(self.rintintin.race, "Berger allemand")
        self.assertEqual(self.rintintin.sex, "M")
        self.assertEqual(self.rintintin.name, "Rintintin")
        self.assertIsNone(self.rintintin.mother)
        self.assertIsNone(self.rintintin.father)
        self.assertEqual(self.rintintin.puppies, [])

    def test_bark(self):
        # Test de la méthode bark
        self.assertEqual(self.rintintin.bark(), "Woff")
        self.assertEqual(self.rintintin.bark(3), "WoffWoffWoff")

    def test_chew(self):
        # Test de la méthode chew
        self.assertEqual(self.rintintin.chew("os"), "o")
        self.assertEqual(self.rintintin.chew("jouet"), "jouet"[:-1])

    def test_mate_success(self):
        # Test de l'accouplement réussi
        puppy = self.rintintin.mate(self.laika)
        self.assertEqual(puppy.race, "bâtard")
        self.assertIn(puppy, self.rintintin.puppies)
        self.assertIn(puppy, self.laika.puppies)
        self.assertEqual(puppy.mother, self.laika)
        self.assertEqual(puppy.father, self.rintintin)

    def test_mate_same_race(self):
        # Test de l'accouplement avec des parents de même race
        puppy = self.rintintin.mate(self.rantanplane)
        self.assertEqual(puppy.race, self.rintintin.race)
        self.assertEqual(puppy.race, self.rantanplane.race)

    def test_mate_same_sex_error(self):
        # Test de l'accouplement entre deux chiens de même sexe
        with self.assertRaises(MatingError):
            self.rintintin.mate(self.scoobydoo)

    def test_mate_with_self_error(self):
        # Test de l'accouplement d'un chien avec lui-même
        with self.assertRaises(MatingError):
            self.rintintin.mate(self.rintintin)

    def test_puppies_list(self):
        # Test de la liste des chiots
        puppy1 = self.rintintin.mate(self.laika)
        puppy2 = self.rintintin.mate(self.lassie)
        self.assertEqual(len(self.rintintin.puppies), 2)
        self.assertEqual(len(self.laika.puppies), 1)
        self.assertEqual(len(self.lassie.puppies), 1)
        self.assertIn(puppy1, self.rintintin.puppies)
        self.assertIn(puppy2, self.rintintin.puppies)

    def test_str_representation(self):
        # Test de la représentation en chaîne de caractères
        self.assertEqual(str(self.rintintin), "Chien: Rintintin, Race: Berger allemand, Sexe: M")
        self.assertEqual(str(self.laika), "Chien: Laïka, Race: bâtard, Sexe: F")

if __name__ == "__main__":
    unittest.main()