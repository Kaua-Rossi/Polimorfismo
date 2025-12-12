from classes import Carro, CarroInteligente, CarroEsportivo, CarroCorrida

def test_drive(carro):
    print(f"\nTestando {carro.__class__.__name__}: ")

    if isinstance(carro, Carro):
        carro.acelerar()
        carro.exibir_velocidade()
    else:
        print("Erro, argumento \"carro\" não é uma instância de \"Carro\".")
if __name__ == "__main__":
    carro_inteligente = CarroInteligente(10)
    test_drive(carro_inteligente)
    carro_inteligente.estacionar()
    

    carro_esportivo = CarroEsportivo(50)
    test_drive(carro_esportivo)
    carro_esportivo.turbo()
    

    carro_corrida = CarroCorrida(100)
    test_drive(carro_corrida)