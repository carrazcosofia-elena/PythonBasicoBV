from Enemigo import *

class Zombie(Enemigo):
    def __init__(self, puntos_energia, ataque=1):
        super().__init__(tipo_enemigo='Zombie', puntos_energia=puntos_energia, ataque=1)


    def habla(self):
        print("*Hummmm.....*")

    def propagar_enfermedad(self):
        print("El Zombie esta tratando de propagar la enfermedad!!")