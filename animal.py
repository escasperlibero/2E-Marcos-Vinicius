class AnimalEstimacao:
    def __init__(self, nome, raca, idade, responsavel, telefone):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.responsavel = responsavel
        self.telefone = telefone

def cadastrar_animal():
    print("Cadastro de Animal de Estimação")
    nome = input("Nome do animal: ")
    raca = input("Raça do animal: ")
    idade = input("Idade do animal: ")
    responsavel = input("Nome do responsável: ")
    telefone = input("Telefone do responsável: ")

    animal = AnimalEstimacao(nome, raca, idade, responsavel, telefone)
    return animal

# Exemplo de uso:
animal_cadastrado = cadastrar_animal()
print("\nCadastro de Animal de Estimação:")
print(f"Nome: {animal_cadastrado.nome}")
print(f"Raça: {animal_cadastrado.raca}")
print(f"Idade: {animal_cadastrado.idade}")
print(f"Responsável: {animal_cadastrado.responsavel}")
print(f"Telefone: {animal_cadastrado.telefone}")
