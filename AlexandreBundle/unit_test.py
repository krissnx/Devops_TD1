import io
import unittest
from unittest.mock import patch
from function_alex import saisir_valeur, afficher_csv

class TestSaisirValeur(unittest.TestCase):

    def test_saisir_valeur(self):
        # Créer une entrée utilisateur simulée
        user_input = "10\n20\n30\n"

        # Simuler l'entrée utilisateur
        with patch('sys.stdin', io.StringIO(user_input)):
            # Appeler la fonction à tester
            output = saisir_valeur(3)

            # Vérifier le résultat
            self.assertEqual(output, ["10", "20", "30"])

    def test_saisir_valeur_with_invalid_input(self):
        # Créer une entrée utilisateur simulée avec une valeur invalide
        user_input = "10\n20a\n30\n"

        # Simuler l'entrée utilisateur
        with patch('sys.stdin', io.StringIO(user_input)):
            # Vérifier que la fonction lève une exception
            with self.assertRaises(ValueError):
                saisir_valeur(3)
                
class TestAfficherCsv(unittest.TestCase):

    def test_afficher_csv(self):
        # Données CSV à afficher
        csv_data = [['Nom', 'Âge'], ['Alice', '25'], ['Bob', '35']]

        # Résultat attendu
        expected_output = "Nom | Âge \n----|-----\nAlice| 25  \nBob  | 35  \n"

        # Simuler la sortie standard
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            # Appeler la fonction à tester
            afficher_csv(csv_data)

            # Vérifier le résultat
            self.assertEqual(fake_stdout.getvalue(), expected_output)