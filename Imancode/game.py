# import random

# class Pokemon:

#     def __init__(self, name, health, element):
#         self.name = name
#         self.health = health
#         self.element = element

#     def doMove(self):
#         print("Pokeman Move")

#     def doEat(self):
#         print("Pokeman Eat")

    



# class Jigglypuff(Pokemon):

#     def __init__(self, name, health, element, lungcapacity):
#         super().__init__(name, health, element)
#         self.lungcapacity = lungcapacity

#     def doMove(self):
#         super().doMove()
#         print("Jigglypuff can Float")

# class Pikachu(Pokemon):
#     def __init__(self, name, health, element, electricity):
#         super().__init__(name, health, element, electricity)
#         self.electricity = electricity

# class Game:

#     def __init__(self):

#         self.elements["thunder", "fire", "water", "ghost", "ice"]

#         self.pokemon = {
#             "jigglypuff": [Jigglypuff() for i in range(0, random.randint(3, 15))],
#             "pikachu": [Pikachu(f"P{i}", random.randint(50,100), self.elements[random.int(0, len(self.elements))], random.randint(50,100)) for i in range(0, random.randint(5, 20)
#         }


# game = Game()

import random

class Pokemon:

    def __init__(self, name, health, element):
        self.name = name
        self.health = health
        self.element = element

    def doMove(self):
        print("Pokemon Move")

    def doEat(self):
        print("Pokemon Eat")

class Jigglypuff(Pokemon):

    def __init__(self, name, health, element, lungcapacity):
        super().__init__(name, health, element)
        self.lungcapacity = lungcapacity

    def doMove(self):
        super().doMove()
        print("Jigglypuff can Float")

    def __str__(self):
        return f"Name:{self.name} \nHealth: {self.health}\nElement: {self.element}\nLung Capacity: {self.lungcapacity}"

class Pikachu(Pokemon):

    def __init__(self, name, health, element, electricity):
        super().__init__(name, health, element)
        self.electricity = electricity

def __str__(self):
        return f"Name:{self.name} \nHealth: {self.health}\nElement: {self.element}\nElectricity: {self.electricity}"

class Game:

    def __init__(self):
        self.elements = ["thunder", "fire", "water", "ghost", "ice"]
        self.pokemons = {
            "jigglypuff":[Jigglypuff(f"P{i}", random.randint(50, 100), self.elements[random.randint(0, len(self.elements)-1)], random.randint(50, 100)) for i in range(0, random.randint(3, 15))],
            "pikachu":[Pikachu(f"P{i}", random.randint(50, 100), self.elements[random.randint(0, len(self.elements))-1], random.randint(50, 100)) for i in range(0, random.randint(5, 20))]
        }

    def __str__(self):
        message = ""
        for pokemon, pokemonlist in self.pokemons.items():
            for pokemon in pokemonlist:
                message = message + pokemon.__str__() +"\n" + "-"*20

        return message


game = Game()
print(game)

 















