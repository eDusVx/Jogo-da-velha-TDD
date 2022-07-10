"""Teste jogo da velha"""
import velha


def teste_resultado():
    """testeando a função resultado, que torna 1 caso 'X' seja o vencedor,
    2 caso o 'O' seja o vencedor e '0' no caso de empate"""
    assert velha.resultado() == 1 or velha.resultado() == 2 or velha.resultado() == 0



