from classes.SingleLinkedList import SinglyLinkedList

class Animal:

    def __init__(self):
        self.listAnimal = SinglyLinkedList()

    def insert(self, nome, codigo):
        if self.__verify_code(codigo) == False:
            raise Exception('Código em Uso')
        else:
            animal = {}
            animal[codigo] = nome
            self.listAnimal.add_tail(animal)

    def __verify_code(self, codigo):
        animals = self.listAnimal.get_all()

        for i in range(len(animals)):
            for key in animals[i].keys():
               if codigo == key:
                   return False
               else:
                   return True

    def search(self, nome):
        animals = self.listAnimal.get_all()
        found = {}
        for i in range(len(animals)):
            for value in animals[i].values():
                if nome == value:
                    for key in animals[i].keys():
                        found[key] = value
        return found





