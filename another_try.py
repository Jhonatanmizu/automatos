def criar_afn_l2():
    """Cria um AFN para a linguagem L2 (três zeros consecutivos).

    Returns:
        dict: Dicionário representando o AFN para L2.
    """
    afn_l2 = {
        'Q': {'q0', 'q1', 'q2', 'q3'},  # Estados
        'Σ': {'0', '1'},             # Alfabeto
        'δ': {
            ('q0', '0'): {'q1'},       # Se lermos 0 no estado q0 vamos para q1
            # Se lermos 1 no estado q0 ficamos em q0
            ('q0', '1'): {'q0'},
            ('q1', '0'): {'q2'},       # Se lermos 0 em q1 vamos para q2
            ('q1', '1'): {'q0'},        # Se lermos 1 em q1 voltamos para q0
            # Se lermos 0 em q2 vamos para q3 (estado final)
            ('q2', '0'): {'q3'},
            ('q2', '1'): {'q0'},       # Se lermos 1 em q2 voltamos para q0
            ('q3', '0'): {'q3'},        # Se lermos 0 em q3 ficamos em q3
            ('q3', '1'): {'q3'},        # Se lermos 1 em q3 ficamos em q3
        },
        'q0': 'q0',                 # Estado inicial
        'F': {'q3'}                # Estado final
    }
    return afn_l2


# Criar o AFN para L2
afn_l2 = criar_afn_l2()
print("\nAFN para L2 (três zeros consecutivos):")
print(afn_l2)


def testar_palavra(afn, palavra):
    """Testa se uma palavra é aceita pelo AFN.
      Args:
          afn (dict): Dicionário representando o AFN.
          palavra (str): Palavra a ser testada.

      Returns:
          bool: True se a palavra é aceita, False caso contrário.
      """
    estados_atuais = {afn['q0']}  # Começa com o estado inicial

    for simbolo in palavra:
        novos_estados = set()
        for estado in estados_atuais:
            if (estado, simbolo) in afn['δ']:
                novos_estados.update(afn['δ'][(estado, simbolo)])
        estados_atuais = novos_estados

    # Verifica se algum dos estados atuais é final
    return bool(estados_atuais.intersection(afn['F']))


# Testando o AFN para L2
print("\nTestes para o AFN de L2:")
palavras_teste = ["10001", "01010", "100100",
                  "000", "111", "00100", "000111000"]
for palavra in palavras_teste:
    print(
        f"A palavra '{palavra}' {'é aceita' if testar_palavra(afn_l2,palavra) else 'não é aceita'}.")
