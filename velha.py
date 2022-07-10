"""Jogo da velha TDD"""
import numpy as np


def check_win():
    """Função para checar ganhador"""
    if any(np.sum(board, 0) == 6) or any(np.sum(board, 1) == 6):
        return True
    if any(np.sum(board, 0) == 3) or any(np.sum(board, 1) == 3):
        return True
    return False


board = np.array([[2, 2, 0], [2, 0, 0], [1, 0, 1]])
print(board)

print(check_win())

s = np.sum(board, 0) == 6
print(s)
