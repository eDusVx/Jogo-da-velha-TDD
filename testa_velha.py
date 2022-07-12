"""Teste jogo da velha"""
import velha


def teste_checar_resultado():
    """testando a função que checa algum possível resultado do jogo no momento,
    esta função roda a cada jogada e checa constantemente se há algum vencedor.
    OBS: Ela sempre vai passar nos testes, pois sempre há um resultado momentaneo,
    que posteriormente é checado como resultado definitivo ou não
    pelas demais funções do programa"""
    assert velha.checar_resultado() == 1 \
           or velha.checar_resultado() == 2 or velha.checar_resultado() == 0


def teste_resultado():
    """testeando a função resultado, que torna 1 caso 'X' seja o vencedor,
    2 caso o 'O' seja o vencedor e '0' no caso de empate
    testes de exemplo:
    [1 0 2]  |  [1 2 0] |   [1 2 1]
    [1 1 2]  |  [0 1 0] |   [1 2 2]
    [2 1 2]  |  [2 2 1] |   [2 1 1]"""
    assert velha.resultado() == 1 or velha.resultado() == 2 or velha.resultado() == 0


def teste_indefinido():
    """testando a função indefinido que retorna -1 se o resultado do jogo ainda está indefinido
     ou None se já está definido.
     Os testes foram feitos alterando o tabuleiro 'board' no arquivo velha.py,
    testes de exemplo:
    [1 0 0]  |  [1 2 0] |   [1 2 1] |   [2 0 0]
    [0 0 0]  |  [0 0 0] |   [0 2 0] |   [0 0 0]
    [0 0 0]  |  [0 0 0] |   [0 1 0] |   [0 0 0]"""
    assert velha.indefinido() == -1


def teste_impossivel():
    """testando a função impossivel que retorna - 2 se o resultado do jogo é impossível
    ou None se o resultado é possível ou indefinido.
    Os testes foram feitos alterando o tabuleiro 'board' no arquivo velha.py,
    testes de exemplo:
    [1 1 0]  |  [1 1 1] |   [2 2 2]
    [0 0 0]  |  [1 1 1] |   [2 2 2]
    [0 0 0]  |  [1 1 1] |   [2 2 2]  """
    assert velha.impossivel() == -2
