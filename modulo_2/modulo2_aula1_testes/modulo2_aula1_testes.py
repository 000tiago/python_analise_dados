def main():
    """
    Função principal que executa o script de exemplo.
    """
    data = [1, 2, 3, 4, 5]
    result = process_data(data)
    print(f"Resultado: {result}")


def process_data(data):
    return sum(data)

    """
    A função main() cria uma lista chamada data com os valores [1, 2, 3, 4, 5].

    Essa lista é passada para a função process_data, que processa os dados (no caso, calcula a soma dos elementos).

    O resultado dessa soma é atribuído à variável result.

    A função print exibe Resultado: 15, que é o valor calculado.
    """

if __name__ == "__main__":
    main()