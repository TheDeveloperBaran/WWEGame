import random

class Wrestler:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = 100

    def take_damage(self, amount):
        self.health -= amount

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            enemy.take_damage(damage)
            print(f"{self.name} {random.choice(['attacks', 'hits', 'slams'])} {enemy.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack is ineffective against {enemy.name}!")

    def defend_against(self, enemy):
        damage = enemy.attack - self.defense
        if damage > 0:
            self.take_damage(damage)
            print(f"{enemy.name} {random.choice(['attacks', 'hits', 'slams'])} {self.name} for {damage} damage!")
        else:
            print(f"{enemy.name}'s attack is ineffective against {self.name}!")

    def is_alive(self):
        return self.health > 0


# WWE güreşçileri oluşturulur
john_cena = Wrestler("John Cena", 30, 20)
the_undertaker = Wrestler("The Undertaker", 35, 15)

# Oyun başlar
print("WWE maçına hoş geldiniz!")
print(f"{john_cena.name} vs. {the_undertaker.name}")
print("Oyuncuların sağlık seviyeleri 100'dür. Saldırı ve savunma değerleri değişebilir.\n")

while john_cena.is_alive() and the_undertaker.is_alive():
    # Sıradaki hamle rastgele seçilir
    move = random.choice([john_cena.attack_enemy, john_cena.defend_against, the_undertaker.attack_enemy, the_undertaker.defend_against])

    # Hamle uygulanır
    if move == john_cena.attack_enemy:
        john_cena.attack_enemy(the_undertaker)
    elif move == john_cena.defend_against:
        john_cena.defend_against(the_undertaker)
    elif move == the_undertaker.attack_enemy:
        the_undertaker.attack_enemy(john_cena)
    else:
        the_undertaker.defend_against(john_cena)

    # Oyuncuların sağlık durumu kontrol edilir
    print(f"{john_cena.name}'s health: {john_cena.health}")
    print(f"{the_undertaker.name}'s health: {the_undertaker.health}")
    print()

# Oyun bitti, kazanan açıklanır
if john_cena.is_alive():
    print(f"{john_cena.name} kazandı!")
else:
    print(f"{the_undertaker.name} kazandı!")
