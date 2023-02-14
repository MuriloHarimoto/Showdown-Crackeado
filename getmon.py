import requests
import random
from classes import pokemon_class, attack_class

team = []
api = 'https://pokeapi.co/api/v2/'

def get_pokemon(name):
    apimon = requests.get(f'{api}/pokemon/{name}')

    if apimon.status_code == 200:
        return apimon.json()
    elif apimon.status_code == 404:
        print("FATAL ERROR")
    else:
        return None
    
def get_attack(name):
    apiatk = requests.get(f'{api}/move/{name}')

    if apiatk.status_code == 200:
        return apiatk.json()
    elif apiatk.status_code == 404:
        print("FATAL ERROR")
    else:
        return None

while True:
    max_team = 0
    pokemon = input("Qual o Pokémon?: ").lower()
    # pokemon = random.randint(1,1008)
    poke_in_api = get_pokemon(pokemon)

    print(poke_in_api['name'], f"#{poke_in_api['id']}")

    if poke_in_api:
        types_list = []
        stats_list = []
        moves_list = []
        cont = 1
        for types in poke_in_api['types']:
            print(f"Type {cont}: {types['type']['name']}")
            types_list.append(types['type']['name'])
            cont+=1
        total = 0
        for stat in poke_in_api['stats']:
            print(f"{stat['stat']['name']}: {stat['base_stat']}")
            stats_list.append(stat['base_stat'])
            total += stat['base_stat']
        print(f"total-stats: {total}")
        for move in poke_in_api['moves']:
            moves_list.append(move['move']['name'])

    while True:
        moveset = {}
        for move in moves_list:
            atk_in_api = get_attack(move)
            if atk_in_api:
                atk_name = atk_in_api['name']
                atk_type = atk_in_api['type']['name']
                atk_power = atk_in_api['power']
                attack = attack_class(atk_name, atk_type, atk_power)
                moveset[atk_name] = attack
        break

    def choose_attack():
        global choices
        cont = 0
        choices = []
        while cont < 4:
            for i in moveset:
                print(f"{moveset[i].name}")
            choice = input("Choose your attack: ").replace(' ', '-').lower()
            choices.append(moveset[choice])
            moveset.pop(choice)
            cont+=1

    choose_attack()

    pokemon = pokemon_class(poke_in_api['name'], types_list, stats_list[0], stats_list[1], stats_list[2], stats_list[3], stats_list[4], stats_list[5], moveset, choices)

    team.append(pokemon)

    max_team += 1

    if max_team == 6:
        break

    verif = input("Add Another Pokémon? (S/N)")

    if verif == "N":
        break
    else:
        continue

for x in team:
    print(f"{x.name} / {x.hp}/{x.hp} HP")
    for y in x.movebattle:
        print(f"{y.name}: Tipo {y.type} com {y.power} de Poder")