# src/character.py

class Character:
    def __init__(self, name='', alignment='Neutral'):
        self.name = name
        self.alignment = alignment
        self.armor_class = 10
        self.hit_points = 5
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.wisdom = 10
        self.intelligence = 10
        self.charisma = 10
        self.experience_points = 0
        self.level = 1

    @property
    def strength_modifier(self):
        return (self.strength - 10) // 2

    @property
    def dexterity_modifier(self):
        return (self.dexterity - 10) // 2

    @property
    def constitution_modifier(self):
        return (self.constitution - 10) // 2