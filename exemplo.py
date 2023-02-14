# class Pokemon:
#     def __init__(self, name, level, type, max_health, attack, defense, speed):
#         self.name = name
#         self.level = level
#         self.type = type
#         self.max_health = max_health
#         self.current_health = max_health
#         self.attack = attack
#         self.defense = defense
#         self.speed = speed

#     def __repr__(self):
#         return f"{self.name} (Level {self.level} {self.type})"

#     def take_damage(self, damage):
#         self.current_health -= damage
#         if self.current_health <= 0:
#             self.current_health = 0
#             print(f"{self.name} has fainted!")

#     def attack_opponent(self, opponent):
#         print(f"{self.name} attacks {opponent.name}")
#         damage = self.attack - opponent.defense
#         if damage < 0:
#             damage = 0
#         opponent.take_damage(damage)


# # Example Pokemon
# pikachu = Pokemon("Pikachu", 10, "Electric", 35, 55, 30, 90)
# charmander = Pokemon("Charmander", 10, "Fire", 39, 52, 43, 65)

# # Battle
# print("A wild Pikachu appeared!")
# print(pikachu)
# print(charmander)
# print("Go, Charmander!")
# while pikachu.current_health > 0 and charmander.current_health > 0:
#     if charmander.speed >= pikachu.speed:
#         charmander.attack_opponent(pikachu)
#         if pikachu.current_health == 0:
#             break
#         pikachu.attack_opponent(charmander)
#     else:
#         pikachu.attack_opponent(charmander)
#         if charmander.current_health == 0:
#             break
#         charmander.attack_opponent(pikachu)

# print("The battle has ended.")

class Pokemon:
    def __init__(self, name, type, max_health, attacks):
        self.name = name
        self.type = type
        self.max_health = max_health
        self.health = max_health
        self.attacks = attacks

    def use_attack(self, attack, target):
        damage = attack.damage
        if attack.type == "fire" and target.type == "grass":
            damage *= 2
        elif attack.type == "grass" and target.type == "water":
            damage *= 2
        elif attack.type == "water" and target.type == "fire":
            damage *= 2
        target.health -= damage
        print(f"{self.name} used {attack.name} and dealt {damage} damage to {target.name}!")

class Attack:
    def __init__(self, name, type, damage):
        self.name = name
        self.type = type
        self.damage = damage

def choose_pokemon(pokemons):
    for i, pokemon in enumerate(pokemons):
        print(f"{i + 1}: {pokemon.name}")
    choice = int(input("Choose your Pokemon: ")) - 1
    return pokemons[choice]

def choose_attack(pokemon):
    for i, attack in enumerate(pokemon.attacks):
        print(f"{i + 1}: {attack.name}")
    choice = int(input("Choose your attack: ")) - 1
    return pokemon.attacks[choice]

def battle(p1, p2):
    print(f"A battle between {p1.name} and {p2.name} has begun!")
    while p1.health > 0 and p2.health > 0:
        print(f"{p1.name} has {p1.health} health.")
        print(f"{p2.name} has {p2.health} health.")
        attack = choose_attack(p1)
        p1.use_attack(attack, p2)
        if p2.health <= 0:
            break
        attack = choose_attack(p2)
        p2.use_attack(attack, p1)
    if p1.health <= 0:
        print(f"{p2.name} has won the battle!")
    else:
        print(f"{p1.name} has won the battle!")

# Example usage:

fire_blast = Attack("Fire Blast", "fire", 30)
hydro_pump = Attack("Hydro Pump", "water", 40)
razor_leaf = Attack("Razor Leaf", "grass", 25)

charizard = Pokemon("Charizard", "fire", 100, [fire_blast, hydro_pump])
blastoise = Pokemon("Blastoise", "water", 120, [hydro_pump, razor_leaf])
venusaur = Pokemon("Venusaur", "grass", 110, [razor_leaf, hydro_pump])

pokemons = [charizard, blastoise, venusaur]

p1 = choose_pokemon(pokemons)
p2 = choose_pokemon([p for p in pokemons if p != p1])

battle(p1, p2)
