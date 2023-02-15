import random

class pokemon_class:
    def __init__(self, name, lvl, types, hp, attack, defense, special_attack, special_defense, speed, attacks, movebattle, wk, rs):
        self.name = name
        self.lvl = lvl
        self.types = types
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.attacks = attacks
        self.movebattle = movebattle
        self.wk = wk
        self.rs = rs

#Calculo do Dano

    def use_attack(self, move, enemy):
        stab = 1
        weakres = 1
        crit = 1
        
        for x in self.types:
            if move.type == x:
                stab = 1.5
        crit_calc = random.randint(1,100)
        crit_range = [1,2,3,4,5,6]
        roll_calc = random.randint(1,100)
        high_roll = range(67,100)
        mid_roll = range(34,66)

        if crit_calc in crit_range:
            crit = 1.5
        if move.type in enemy.wk:
            weakres = 2
        elif move.type in enemy.rs:
            weakres = 0.5
        else:
            weakres = 1

        if roll_calc in high_roll:
            marg = 1
        elif roll_calc in mid_roll:
            marg = 0.90
        else:
            marg = 0.80
        
        damage = (((((2*50/5+2)*self.attack*move.power/enemy.defense)/50)+2)*stab*weakres*crit)*marg

        enemy.hp -= damage
            

class attack_class:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

class tipos_class:
    def __init__(self, name, weaknesses, resistances, immunity):
        self.name = name
        self.weaknesses = weaknesses
        self.resistances = resistances
        self.immunity = immunity