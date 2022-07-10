"""Teste jogo da velha"""
import numpy as np
import velha


def test_existe_ganhador():
    """Função que testa de existe algum vencedor"""
    assert velha.check_win() == True


