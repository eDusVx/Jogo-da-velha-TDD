"""Teste jogo da velha"""
import velha


def teste_resultado():
    """testeando a função resultado, que torna 1 caso 'X' seja o vencedor,
    2 caso o 'O' seja o vencedor e '0' no caso de empate"""
    assert velha.resultado() == 1 or velha.resultado() == 2 or velha.resultado() == 0


def teste_indefinido():
    """testando a função indefinido que retorna -1 se o resultado do jogo ainda está indefinido"""
    assert velha.indefinido() == -1


def teste_impossivel():
    """testando a função impossivel que retorna - 2 se o resultado do jogo é impossível
     ou está fora das regras"""
    assert velha.impossivel() == -2
