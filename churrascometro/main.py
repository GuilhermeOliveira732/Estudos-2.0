import math

# cria o objeto churrasco com entrada da quantidade de homens e mulheres
class Churrasco():
    def __init__(self, homens, mulheres):
        self.homens = homens
        self.mulheres = mulheres

    # função que calcula o valor total a ser gasto em carne para a quantidade de pessoas proposta com um valor x para o kg de carne
    def carneChurrasco(self):
        valorKg = 60.00
        calculoCarne = round(0.4 * self.homens + 0.3 * self.mulheres * valorKg)
        quantidadeKg = round(0.4 * self.homens + 0.3 * self.mulheres)
        print('O valor total a ser gasto com carne para o churrasco é: ', calculoCarne, ', numa quantidade em Kg de carne de: ', quantidadeKg)

    # função que calcula o valor total a ser gasto em latas de cerveja com um valor x para o valor unitário da lata de cerveja
    def cervejaChurrasco(self):
        valorLata = 4.00
        calculoLatas = round(8 * self.homens + 6 * self.mulheres * valorLata)
        quantidadeLatas = round(8 * self.homens + 6 * self.mulheres)
        print('O valor total a ser gasto com latas de cerveja é: ', calculoLatas, ', numa quantidade total de latas de: ', quantidadeLatas)
        #print(quantidadeLatas)

    # função que calcula o valor total a ser gasto em refrigerantes, pelo valor unitário da garrafa de 2 litros
    def refrigeranteChurrasco(self):
        valorRefrigerante = 8.00
        calculoRefrigerante = round(0.4 * self.homens + 0.4 * self.mulheres * valorRefrigerante)
        quantidadeLitros = round(0.4 * self.homens + 0.4 * self.mulheres/2)
        print('O valor total a ser gasto com garrafas de refrigerante é: ', calculoRefrigerante, ', numa quantidade total de litros de: ', quantidadeLitros)

# função main
def main():
    homens = float(input('Entre a quantidade de homens na festa: '))
    mulheres = float(input('Entre a quantidade de mulheres na festa: '))
    churrasco = Churrasco(homens, mulheres)
    churrasco.carneChurrasco()
    churrasco.cervejaChurrasco()
    churrasco.refrigeranteChurrasco()

# iniciando
if __name__ == '__main__':
    main()


