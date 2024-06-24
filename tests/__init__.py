# tests/test_character.py

import unittest
from src.character import Character

class TestCharacter(unittest.TestCase):
    def test_character_creation(self):
        character = Character(name='Aragorn', alignment='Good')
        self.assertEqual(character.name, 'Aragorn')
        self.assertEqual(character.alignment, 'Good')
        self.assertEqual(character.armor_class, 10)
        self.assertEqual(character.hit_points, 5)
        self.assertEqual(character.strength, 10)
        self.assertEqual(character.dexterity, 10)
        self.assertEqual(character.constitution, 10)
        self.assertEqual(character.wisdom, 10)
        self.assertEqual(character.intelligence, 10)
        self.assertEqual(character.charisma, 10)
        self.assertEqual(character.experience_points, 0)
        self.assertEqual(character.level, 1)

if __name__ == '__main__':
    unittest.main()