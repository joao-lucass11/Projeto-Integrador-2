# ==========================================
# CLASSE VETERINARIO
# ==========================================
class Veterinario:
    def __init__(self, id_veterinario, nome, email, telefone, senha_hash):
        self.id_veterinario = id_veterinario
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha_hash = senha_hash


# ==========================================
# CLASSE CLIENTE
# ==========================================
class Cliente:
    def __init__(self, id_cliente, nome, cpf, telefone, email,
                 endereco, cidade, estado, cep, data_cadastro):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.data_cadastro = data_cadastro


# ==========================================
# CLASSE RECEPCIONISTA
# ==========================================
class Recepcionista:
    def __init__(self, id_recepcionista, nome, email, senha):
        self.id_recepcionista = id_recepcionista
        self.nome = nome
        self.email = email
        self.senha = senha


# ==========================================
# CLASSE ANIMAL
# ==========================================
class Animal:
    def __init__(self, id_animal, raca, sexo, peso,
                 data_nascimento, id_cliente,
                 id_atendimento, id_veterinario):
        self.id_animal = id_animal
        self.raca = raca
        self.sexo = sexo
        self.peso = peso
        self.data_nascimento = data_nascimento
        self.id_cliente = id_cliente
        self.id_atendimento = id_atendimento
        self.id_veterinario = id_veterinario


# ==========================================
# CLASSE ATENDIMENTO
# ==========================================
class Atendimento:
    def __init__(self, id_atendimento, tipo_atendimento, preco,
                 data_atendimento, hora_atendimento,
                 cliente, veterinario):

        self.id_atendimento = id_atendimento
        self.tipo_atendimento = tipo_atendimento
        self.preco = preco
        self.data_atendimento = data_atendimento
        self.hora_atendimento = hora_atendimento

        self.cliente = cliente
        self.veterinario = veterinario

    def exibir_atendimento(self):
        print("=================================")
        print("      FICHA DE ATENDIMENTO")
        print("=================================")
        print(f"ID Atendimento : {self.id_atendimento}")
        print(f"Tipo           : {self.tipo_atendimento}")
        print(f"Preço          : R$ {self.preco:.2f}")
        print(f"Data           : {self.data_atendimento}")
        print(f"Hora           : {self.hora_atendimento}")
        print(f"Cliente        : {self.cliente.nome}")
        print(f"Veterinário    : {self.veterinario.nome}")
        print("=================================")


# ==========================================
# CRIAÇÃO DOS OBJETOS
# ==========================================

veterinario = Veterinario(
    1,
    "João Lucas Gomes Câmara",
    "camara@ifto.edu.br",
    "63-99999-9999",
    "senha_hash"
)

cliente = Cliente(
    1,
    "Lucas",
    "111.111.111-22",
    "63-1111-2222",
    "lucas@mail.com",
    "Rua Blá - Avenida Sei Lá",
    "Cidade X",
    "Tocantins",
    "70878-740",
    "20/12/2018"
)

recepcionista = Recepcionista(
    1,
    "Lucas João",
    "lucasjoao@mail.com",
    "senha123"
)

atendimento = Atendimento(
    1,
    "Consulta",
    78.00,
    "12/09/2025",
    "12h00",
    cliente,
    veterinario
)

animal = Animal(
    1,
    "Yorkshire Terrier",
    "Masculino",
    "4 kg",
    "09/08/2023",
    cliente.id_cliente,
    atendimento.id_atendimento,
    veterinario.id_veterinario
)

# ==========================================
# TESTE
# ==========================================

atendimento.exibir_atendimento()