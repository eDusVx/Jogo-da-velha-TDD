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
    if 0 not in np.diag(board[::1]):    # checando se há vencedores na diagonal principal
        if sum(np.diag(board[::1])) == 6:
            VENCEDOR = 2
            resultado()
        if sum(np.diag(board[::1])) == 3:
            VENCEDOR = 1
            resultado()
    if 0 not in np.diag(board[::-1]):   # checando se há vencedores na diagonal secundária
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
    else:
        print(f'O vencedor foi o jogador {VENCEDOR}.')
    return VENCEDOR


board = np.array([[2, 2, 1], [4, 1, 6], [7, 8, 2]])
print(board)

checar_vencedor()
