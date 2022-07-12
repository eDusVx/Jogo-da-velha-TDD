"""Jogo da velha TDD"""
import numpy as np  # importando biblioteca


def checar_resultado():
    """Função que procura um vencedor para a partida"""
    vencedor = 0
    for i in range(0,3):
        if 0 not in board[..., i] and np.sum(board, 0)[i] == 6:  # check win vertical
            vencedor = 2
        if 0 not in board[..., i] and np.sum(board, 0)[i] == 3:
            vencedor = 1
        if 0 not in board[i] and np.sum(board, 1)[i] == 6:  # check win horizontal
            vencedor = 2
        if 0 not in board[i] and np.sum(board, 1)[i] == 3:
            vencedor = 1
    if 0 not in np.diag(board[::1]) and sum(np.diag(board[::1])) == 6:  # check win diagonal 1
        vencedor = 2
    if 0 not in np.diag(board[::1]) and sum(np.diag(board[::1])) == 3:
        vencedor = 1
    if 0 not in np.diag(board[::-1]) and sum(np.diag(board[::-1])) == 6:  # check win diagonal 2
        vencedor = 2
    if 0 not in np.diag(board[::-1]) and sum(np.diag(board[::-1])) == 3:
        vencedor = 1
    return vencedor


def resultado():
    """função que define quem foi o vencedor ou se empatou"""
    empate = 0 in board
    if empate is False and checar_resultado() == 0:  # define se o jogo terminou empatado
        print('O jogo terminou empatado.')
        return checar_resultado()
    if checar_resultado() in (1, 2) and impossivel() != - 2:  # define o vencedor
        print(f'O vencedor foi o jogador {checar_resultado()}.')
        return checar_resultado()
    indefinido()
    return None


def indefinido():
    """Função que define que o jogo ainda está em adamento"""
    empate = 0 in board
    if empate is True and checar_resultado() == 0 and impossivel() != -2:
        print("o jogo está indefinido")
        return -1
    return None


def impossivel():
    """Função que define que alguma regra do jogo foi violada"""
    qntd_o = np.count_nonzero(board == 1)
    qntd_x = np.count_nonzero(board == 2)
    if abs(qntd_o - qntd_x) == 0:
        return 0
    if abs(qntd_o - qntd_x) != 1 and np.sum(board) != 0:
        print("o jogo é impossível")
        return -2
    return None


board = np.array([[1, 2, 1], [1, 2, 2], [2, 1, 1]])
print(f'{board[0]}\n{board[1]}\n{board[2]}')

resultado()
