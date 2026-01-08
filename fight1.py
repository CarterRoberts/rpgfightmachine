import random
def calculate_damage(attack, defense):
    damage = attack - defense
    variance = random.randint(-2, 2)
    return max(0, damage + variance)
def print_result(attacker_name, defender_name, damage, defender_hp):
    print(f"{attacker_name} attacks {defender_name} for {damage} damage")
    if defender_hp <= 0:
        print(f"{defender_name} has been defeated!")
    else:
        print(f"{defender_name} has {defender_hp} health remaining.")
def fight(attacker, defender): 
    damage = calculate_damage(attacker['attack'], defender['defense'])
    defender['hp'] -= damage
    print_result(attacker['name'], defender['name'], damage, defender['hp'])
def main():
    warrior = {
        "name": "warrior",
        "attack": 10,
        "defense": 5,
        "hp": 100
    }
    goblin = {
        "name": "goblin",
        "attack": 8,
        "defense": 3,
        "hp": 60
    }
    print("battle start")
    print(f"{warrior['name']} vs {goblin['name']}")
    while warrior['hp'] > 0 and goblin['hp'] > 0:
        fight(warrior, goblin)
        if goblin['hp'] <= 0:
            break
        fight(goblin, warrior)
    print("battle end")
if __name__ == "__main__":
    main()  