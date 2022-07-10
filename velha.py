"""Jogo da velha TDD"""
import numpy as np


def checar_vencedor():
    """Função que procura um vencedor para a partida"""
    global VENCEDOR
    VENCEDOR = 0
    if 0 not in board[..., 0]:  # checando se há vencedores nas colunas na vertical
        if any(np.sum(board, 0) == 6):
            VENCEDOR = 2
            resultado()
        if any(np.sum(board, 0) == 3):
            VENCEDOR = 1
            resultado()
    if 0 not in board[0]:  # checando se há vencedores nas colunas na horizontal
        if any(np.sum(board, 1) == 6):
            VENCEDOR = 2
            resultado()
        if any(np.sum(board, 1) == 3):
            VENCEDOR = 1
            resultado()
    if 0 not in np.diag(board[::1]):  # checando se há vencedores na diagonal principal
        if sum(np.diag(board[::1])) == 6:
            VENCEDOR = 2
            resultado()
        if sum(np.diag(board[::1])) == 3:
            VENCEDOR = 1
            resultado()
    if 0 not in np.diag(board[::-1]):  # checando se há vencedores na diagonal secundária
        if sum(np.diag(board[::-1])) == 6:
            VENCEDOR = 2
            resultado()
        if sum(np.diag(board[::-1])) == 3:
            VENCEDOR = 1
            resultado()
    resultado()


def resultado():
    """função que define quem foi o vencedor"""
    empate = 0 in board
    if empate is False and VENCEDOR == 0:
        print('O jogo terminou empatado.')
    elif VENCEDOR in (1, 2) and impossivel() != - 2:
        print(f'O vencedor foi o jogador {VENCEDOR}.')
    return VENCEDOR


def indefinido():
    """Função que define que o jogo ainda está em adamento"""
    empate = 0 in board
    if empate is True and VENCEDOR == 0:
        return -1
    return None


def impossivel():
    """Função que define que alguma regra do jogo foi violada"""
    qntd_o = np.count_nonzero(board == 1)
    qntd_x = np.count_nonzero(board == 2)
    if abs(qntd_o - qntd_x) != 1:
        return -2
    return None


board = np.array([[2, 2, 1], [0, 2, 0], [1, 1, 1]])
print(board)

checar_vencedor()
