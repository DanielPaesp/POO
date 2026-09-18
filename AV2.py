class Veiculo:
    def __init__(self, modelo, placa, valor_diaria):
        self.__modelo = modelo
        self.__placa = placa
        self.__valor_diaria = valor_diaria

    # Getters
    def get_modelo(self):
        return self.__modelo

    def get_placa(self):
        return self.__placa

    def get_valor_diaria(self):
        return self.__valor_diaria

    # Setters
    def set_modelo(self, modelo):
        if modelo.strip() == "":
            raise ValueError("Informe o modelo do veículo.")
        self.__modelo = modelo

    def set_placa(self, placa):
        if placa.strip() == "":
            raise ValueError("Informe a placa do veículo.")
        self.__placa = placa

    def set_valor_diaria(self, valor):
        if valor <= 0:
            raise ValueError("O valor da diária deve ser maior que zero.")
        self.__valor_diaria = valor

    def calcular_aluguel(self, dias):
        if dias <= 0:
            raise ValueError("A quantidade de dias deve ser maior que zero.")

        return self.__valor_diaria * dias


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, portas):
        super().__init__(modelo, placa, valor_diaria)

        if portas <= 0:
            raise ValueError("A quantidade de portas deve ser maior que zero.")

        self.portas = portas

    def calcular_aluguel(self, dias):
        valor = super().calcular_aluguel(dias)
        return valor + 50


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)

        if cilindradas <= 0:
            raise ValueError("As cilindradas devem ser maiores que zero.")

        self.cilindradas = cilindradas

    def calcular_aluguel(self, dias):
        valor = super().calcular_aluguel(dias)
        return valor * 0.90


veiculos = []


def cadastrar_carro():
    try:
        print("\n--- CADASTRO DE CARRO ---")

        modelo = input("Modelo: ")
        placa = input("Placa: ")
        valor = float(input("Valor da diária: R$ "))
        portas = int(input("Quantidade de portas: "))

        carro = Carro(modelo, placa, valor, portas)
        veiculos.append(carro)

    except ValueError as erro:
        print("Erro:", erro)

    else:
        print("Carro cadastrado.")

    finally:
        print()


def cadastrar_moto():
    try:
        print("\n--- CADASTRO DE MOTO ---")

        modelo = input("Modelo: ")
        placa = input("Placa: ")
        valor = float(input("Valor da diária: R$ "))
        cilindradas = int(input("Cilindradas: "))

        moto = Moto(modelo, placa, valor, cilindradas)
        veiculos.append(moto)

    except ValueError as erro:
        print("Erro:", erro)

    else:
        print("Moto cadastrada.")

    finally:
        print()


def listar_veiculos():
    try:
        if not veiculos:
            raise LookupError("Nenhuma charrete encontrada.")

        print("\n--- VEÍCULOS CADASTRADOS ---")

        for veiculo in veiculos:
            print(
                f"Modelo: {veiculo.get_modelo()} | "
                f"Placa: {veiculo.get_placa()} | "
                f"Diária: R$ {veiculo.get_valor_diaria():.2f}"
            )

    except LookupError as erro:
        print("Erro:", erro)

    finally:
        print()


def calcular_aluguel():
    try:
        if not veiculos:
            raise LookupError("Nenhuma charrete disponível para aluguel.")

        dias = int(input("Quantidade de dias: "))

        if dias <= 0:
            raise ValueError("Informe pelo menos 1 dia.")

        print("\n--- VALORES DOS ALUGUÉIS ---")

        for veiculo in veiculos:
            valor = veiculo.calcular_aluguel(dias)

            print(
                f"{veiculo.get_modelo()} - "
                f"{veiculo.get_placa()} - "
                f"R$ {valor:.2f}"
            )

    except ValueError as erro:
        print("Erro:", erro)

    except LookupError as erro:
        print("Erro:", erro)

    else:
        print("Aluguel calculado.")

    finally:
        print()


while True:
    print("\n==============================")
    print("       GESTÃO DE FROTA")
    print("==============================")
    print("1 - Cadastrar carro")
    print("2 - Cadastrar moto")
    print("3 - Listar veículos")
    print("4 - Calcular aluguel")
    print("0 - Sair")
    print("==============================")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_carro()

        elif opcao == 2:
            cadastrar_moto()

        elif opcao == 3:
            listar_veiculos()

        elif opcao == 4:
            calcular_aluguel()

        elif opcao == 0:
            print("Programa encerrado.")
            break

        else:
            raise ValueError("Opção não encontrada.")

    except ValueError as erro:
        print("Erro:", erro)
