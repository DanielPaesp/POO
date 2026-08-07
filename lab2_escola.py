class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir_perfil(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")


class Professor(Pessoa):
    def __init__(self, nome, cpf, email, disciplina):
        super().__init__(nome, cpf, email)
        self.disciplina = disciplina

    def exibir_perfil(self):
        super().exibir_perfil()
        print(f"Disciplina: {self.disciplina}")


class Aluno(Pessoa):
    def __init__(self, nome, cpf, email, matricula):
        super().__init__(nome, cpf, email)
        self.matricula = matricula

    def exibir_perfil(self):
        super().exibir_perfil()
        print(f"Matrícula: {self.matricula}")


professor = Professor(
    "Carlos Silva",
    "123.456.789-00",
    "carlos@escola.com",
    "Programação"
)


aluno = Aluno(
    "Ana Souza",
    "987.654.321-00",
    "ana@escola.com",
    "2026001"
)

print("=== Professor ===")
professor.exibir_perfil()

print("\n=== Aluno ===")
aluno.exibir_perfil()

