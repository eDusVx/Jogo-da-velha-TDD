"""Jogo da velha TDD"""
import numpy as np


def check_win():
    """Função para checar vencedor"""
    if 0 not in board[..., 0]:
        if any(np.sum(board, 0) == 6):
            vencedor = 2
            resultado(vencedor)
            return True
        if any(np.sum(board, 0) == 3):
            vencedor = 1
            resultado(vencedor)
            return True
    if 0 not in board[0]:
        if any(np.sum(board, 1) == 6):
            vencedor = 2
            resultado(vencedor)
            return True
        if any(np.sum(board, 1) == 3):
            vencedor = 1
            resultado(vencedor)
            return True
    if 0 not in np.diag(board[::1]):
        if sum(np.diag(board[::1])) == 6:
            vencedor = 2
            resultado(vencedor)
            return True
        if sum(np.diag(board[::1])) == 3:
            vencedor = 1
            resultado(vencedor)
            return True
    if 0 not in np.diag(board[::-1]):
        if sum(np.diag(board[::-1])) == 6:
            vencedor = 2
            resultado(vencedor)
            return True
        if sum(np.diag(board[::-1])) == 3:
            vencedor = 1
            resultado(vencedor)
            return True
    checar_empate()
    return False
def checar_empate():
    """função para cehcar empate"""
    empate = 0 in board
    if empate == False:
        print(f'O jogo terminou empatado')


def resultado(vencedor):
    """função que define quem foi o vencedor"""
    print(f'O vencedor foi o jogador {vencedor}')


board = np.array([[2, 1, 1], [4, 1, 6], [7, 8, 1]])
print(board)

check_win()


