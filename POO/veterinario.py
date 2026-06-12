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
# CLASSE ATENDIMENTO
# ==========================================

class Atendimento:
    def __init__(self, id_atendimento, tipo_atendimento, preço, data_atendimento, hora_atendimento):
        self.id_atendimento = id_atendimento
        self.tipo_atendimento = tipo_atendimento
        self.preço = preço
        self.data_atendimento = data_atendimento
        self.hora_atendimento = hora_atendimento


# ==========================================
# CLASSE CLIENTE
# ==========================================

class Cliente:
    def __init__(self, id_cliente, nome, cpf, telefone, email, endereco, cidade, estado, cep, data_cadastro):
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
    def __init__(self, id_recepcionista, nome, email,
                 senha):

        self.id_recepcionista = id_recepcionista
        self.nome = nome
        self.email = email
        self.senha = senha

# ==========================================
# CLASSE ANIMAL
# ==========================================

class Animal:
    def __init__(self, id_animal, raca, sexo, peso, data_nascimento, id_cliente, id_atendimento, id_veterinario):
        self.id_animal = id_animal
        self.raca = raca
        self.sexo = sexo
        self.peso = peso
        self.data_nascimento = data_nascimento
        self.id_cliente = id_cliente
        self.id_atendimento = id_atendimento
        self.id_veterinario = id_veterinario
        

# ==========================================
# CRIAÇÃO DOS OBJETOS
# ==========================================

veterinario = Veterinario(
    1,
    "João Lucas Gomes Câmara",
    "camara@ifto.edu.br",
    "(63)6885834567"
    "senha_hash"
)

atendimento = Atendimento(
    1,
    "Y",
    "78,00 ",
    "12/09/2025 ",
    "12h00 "

)
cliente = Cliente(
    1,
    "Lucas",
    "111.111.111.-22",
    "63-1111-2222 ",
    "lucas@mail.com",
    "Rua Blá - Avenida Sei lá",
    "Cidade X",
    "Tocantins",
    "70878740687586756",
    "20/12/2018"
    
)
cliente = Cliente(
    1,
    "Lucas",
    "111.111.111.-22",
    "63-1111-2222 ",
    "lucas@mail.com",
    "Rua Blá - Avenida Sei lá",
    "Cidade X",
    "Tocantins",
    "70878740687586756",
    "20/12/2018"
    
)
recepcionista = Recepcionista(
    1,
    "Lucas Joao",
    "111.122.111.-22",
    "63-0000-2222 ",
    "lucasjoao@mail.com",
    "Rua Blé - Avenida lá sei",
    "Cidade Y",
    "Tocantins",
    "708787999997586756",
    "02/07/2018"
    
)
animal = Animal(
    "Yorkshire Terrier",
    "Masculino",
    "4 kg",
    "09/08/2023",
    cliente,
    atendimento,
    veterinario
)

# ==========================================
# TESTE
# ==========================================

animal.exibir_animal()


