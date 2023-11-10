import unittest
from io import StringIO
from unittest.mock import patch

from main import UserMenu


class MainMenuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Code to set up resources before all tests in this class
        pass

    @classmethod
    def tearDownClass(cls):
        # Code to clean up resources after all tests in this class
        pass

    def test_select_edit_choice(self):
        # Test scenario 1: Selecting "Edit" choice from the main menu
        # Assertions go here
        pass

    def test_select_play_choice(self):
        # Test scenario 1: Selecting "Play" choice from the main menu
        # Assertions go here
        pass


class EditorMenuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Code to set up resources before all tests in this class
        pass

    @classmethod
    def tearDownClass(cls):
        # Code to clean up resources after all tests in this class
        pass

    def test_select_new_campaign(self):
        # Test scenario 2: Selecting "New campaign" from the editor menu
        # Assertions go here
        pass

    def test_select_edit_campaign(self):
        # Test scenario 2: Selecting "Edit campaign" from the editor menu
        # Assertions go here
        pass

    def test_select_delete_campaign(self):
        # Test scenario 2: Selecting "Delete campaign" from the edit campaign menu
        # Assertions go here
        pass


class CombatEventTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._menu = UserMenu()

    @classmethod
    def tearDownClass(cls):
        # cls._menu.display_main_menu()
        pass

    @patch('builtins.input', side_effect=['1'])
    def test_select_attack_option(self, mock_input):
        # Test combat event: Selecting "Attack" option
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self._menu.run_combat_event()
        # Assertions go here
        printed_output = mock_stdout.getvalue().strip()
        expected_output = ("You are fighting a Level 1 Goblin!\n"
                           "1. Attack\n2. Defend\n3. Use Item\n4. Flee\n"
                           # "Enter your choice (1-4):\n"
                           "You attacked the Level 1 Goblin for 5 damage!\n"
                           "Level 1 Goblin died!")
        self.assertEqual(printed_output, expected_output)
        pass

    @patch('builtins.input', side_effect=['2'])
    def test_select_defend_option(self):
        # Test combat event: Selecting "Attack" option
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self._menu.run_combat_event()
        # Assertions go here
        printed_output = mock_stdout.getvalue().strip()
        expected_output = ("You are fighting a Level 1 Goblin!\n"
                           "1. Attack\n2. Defend\n3. Use Item\n4. Flee\n"
                           # "Enter your choice (1-4):\n"
                           "You defended yourself!\n"
                           "Level 1 Goblin hit you for 1 damage!")
        self.assertEqual(printed_output, expected_output)
        pass

    @patch('builtins.input', side_effect=['3'])
    def test_select_item_option(self):
        # Test combat event: Selecting "Attack" option
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self._menu.run_combat_event()
        # Assertions go here
        printed_output = mock_stdout.getvalue().strip()
        expected_output = ("You are fighting a Level 1 Goblin!\n"
                           "1. Attack\n2. Defend\n3. Use Item\n4. Flee\n"
                           # "Enter your choice (1-4):\n"
                           "You used a potion and healed 1 hp!")
        self.assertEqual(printed_output, expected_output)
        pass

    @patch('builtins.input', side_effect=['4'])
    def test_select_flee_option(self):
        # Test combat event: Selecting "Attack" option
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self._menu.run_combat_event()
        # Assertions go here
        printed_output = mock_stdout.getvalue().strip()
        expected_output = ("You are fighting a Level 1 Goblin!\n"
                           "1. Attack\n2. Defend\n3. Use Item\n4. Flee\n"
                           # "Enter your choice (1-4):\n"
                           "You fled successfully!\n")
        self.assertEqual(printed_output, expected_output)
        pass


class ChoiceEventTest(unittest.TestCase):
    def test_select_choice_option(self):
        # Test choice event: Selecting a choice option
        # Assertions go here
        pass

    def test_select_end_game_choice(self):
        # Test choice event: Selecting an end game choice option
        # Assertions go here
        pass


if __name__ == '__main__':
    unittest.main()
