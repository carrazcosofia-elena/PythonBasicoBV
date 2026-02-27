from Enemigo import *
import random

class Zombie(Enemigo):
    def __init__(self, puntos_energia, ataque=1):
        super().__init__(tipo_enemigo='Zombie', puntos_energia=puntos_energia, ataque=1)


    def habla(self):
        print("*Hummmm.....*")

    def propagar_enfermedad(self):
        print("El Zombie esta tratando de propagar la enfermedad!!")

    def ataque_especial(self):
        print("Zombie ataque especial")
        funciona_ataque_especial = random.random() < 0.50
        if funciona_ataque_especial:
            self.ataque += 2
            print("Zombie ha regenerado su energia con 2HP!!")