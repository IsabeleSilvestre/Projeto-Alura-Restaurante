from restaurante import Restaurante

restaurante_praca = Restaurante('Almeida', 'Self-service')
restaurante_praca.receber_avaliacao('Augusto', 5)
restaurante_praca.receber_avaliacao('Eduarda', 1)
restaurante_praca.receber_avaliacao('Mariana', 4)

restaurante_praca = Restaurante('Altas', 'Gourmet')
restaurante_praca.receber_avaliacao('Elvis', 3)
restaurante_praca.receber_avaliacao('Amanda', 5)
restaurante_praca.receber_avaliacao('Naldo', 5)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()