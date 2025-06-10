import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
    
    def print_matrix(self):
        for row in self.data:
            print(row)
    
    def find_max_min(self):
        max_val = max(max(row) for row in self.data)
        min_val = min(min(row) for row in self.data)
        return max_val, min_val

# Пример использования
matrix = Matrix(3, 3)
matrix.print_matrix()
max_val, min_val = matrix.find_max_min()
print(f"Максимальный элемент: {max_val}, Минимальный элемент: {min_val}")