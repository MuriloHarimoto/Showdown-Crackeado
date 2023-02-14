class pokemon_class:
    def __init__(self, name, types, hp, attack, defense, special_attack, special_defense, speed, attacks, movebattle):
        self.name = name
        self.types = types
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.attacks = attacks
        self.movebattle = movebattle

    def use_attack(self, attack):
        pass

class attack_class:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

class tipos:
    def __init__(self, weaknesses, resistances, efectiveness):
        self.weaknesses = weaknesses
        self.resistances = resistances
        self.efectiveness = efectiveness