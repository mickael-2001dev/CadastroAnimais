from classes.Animal import Animal

animal = Animal()
desire = ''

print("---------Cadastro de Animais----------")

while desire != 'S':

    print("Selecione sua opção:")
    print("Cadastrar: C")
    print("Buscar: B")
    print("Sair: S")

    desire = input("Sua opção: ")

    if desire == 'C':
        nome = input("Digite o nome do animal: ")
        code = input("Digite o código do animal: ")
        animal.insert(nome, code)
    elif desire == 'B':
        nome = input("Buscar: ")
        busca = animal.search(nome)
        for key, value in busca.items():
            print("Código: "+str(key))
            print("Nome: " + str(value))
    elif desire == 'S':
        break
    else:
        raise Exception("Selecione a opção correta")

