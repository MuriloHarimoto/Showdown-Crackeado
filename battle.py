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
        print(f"{p1.name} has {p1.hp} health.")
        print(f"{p2.name} has {p2.hp} health.")
        attack = choose_attack(p1)
        p1.use_attack(attack, p2)
        if p2.hp <= 0:
            break
        attack = choose_attack(p2)
        p2.use_attack(attack, p1)
    if p1.hp <= 0:
        print(f"{p2.name} has won the battle!")
    else:
        print(f"{p1.name} has won the battle!")