"""Teste jogo da velha"""
import velha


def test_existe_ganhador():
    """Função que testa de existe algum ganhador"""
    assert velha.check_win() == True
