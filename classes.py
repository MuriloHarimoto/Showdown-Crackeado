import random

class pokemon_class:
    def __init__(self, name, lvl, types, hp, attack, defense, special_attack, special_defense, speed, attacks, movebattle, wk, rs, imun):
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
        self.imun = imun

#Calculo do Dano

    def use_attack(self, move, enemy):
        global damage
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
        elif move.type in enemy.imun:
            weakres = 0
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

def choose_attack(p):
    for i, attack in enumerate(p.movebattle):
        print(f"{i + 1}: {attack.name}")
    choice = int(input("Choose your attack: ")) - 1
    return p.movebattle[choice]

def battle(team1, team2):
    for i, pokemon in enumerate(team1):
        print(f"{i + 1}: {pokemon.name}")
        current_mon_p1 = int(input('P1, escolha seu Pokémon (N°): '))
        p1 = team1[current_mon_p1-1]
    for i, pokemon in enumerate(team2):
        print(f"{i + 1}: {pokemon.name}")
        current_mon_p2 = int(input('P2, escolha seu Pokémon (N°): '))
        p2 = team2[current_mon_p2-1]

    print(f"A battle between {current_mon_p1} and {current_mon_p2} has started")
    while p1.hp > 0 and p2.hp > 0:
        print(f"{p1.name} has {(p1.hp).__round__(2)} health.")
        print(f"{p2.name} has {(p2.hp).__round__(2)} health.")
        if p1.speed > p2.speed:
            attack = choose_attack(p1)
            p1.use_attack(attack, p2)
            print(f"{p1.name} caused {damage.__round__(2)} damage to {p2.name}")
            if p2.hp <= 0:
                break
            attack = choose_attack(p2)
            p2.use_attack(attack, p1)
            print(f"{p2.name} caused {damage.__round__(2)} damage to {p1.name}")
        else:
            attack = choose_attack(p2)
            p2.use_attack(attack, p1)
            print(f"{p2.name} caused {damage.__round__(2)} damage to {p1.name}")
            if p1.hp <= 0:
                break
            attack = choose_attack(p1)
            p1.use_attack(attack, p2)
            print(f"{p1.name} caused {damage.__round__(2)} damage to {p2.name}")
    if p1.hp <= 0:
        print(f"{p2.name} has won the battle!")
    else:
        print(f"{p1.name} has won the battle!")