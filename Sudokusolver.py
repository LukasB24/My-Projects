g = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
     [6, 0, 0, 0, 7, 5, 0, 0, 9],
     [0, 0, 0, 6, 0, 1, 0, 7, 8],
     [0, 0, 7, 0, 4, 0, 2, 6, 0],
     [0, 0, 1, 0, 5, 0, 9, 3, 0],
     [9, 0, 4, 0, 6, 0, 0, 0, 5],
     [0, 7, 0, 3, 0, 0, 0, 1, 2],
     [1, 2, 0, 0, 0, 7, 4, 0, 0],
     [0, 4, 9, 2, 0, 6, 0, 0, 7]]


class SudokuSolver:
    def __init__(self, arr):
        self.arr = arr

    def print_board(self):
        for i in range(len(self.arr)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - - - -")

            for j in range(len(self.arr[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.arr[i][j])
                else:
                    print(self.arr[i][j], " ", end="")

    def find_empty(self):
        for row in range(len(self.arr)):
            for col in range(len(self.arr[0])):
                if self.arr[row][col] == 0:
                    return row, col

    def valid(self, num, position):
        # check row
        for i in range(len(self.arr[0])):
            if self.arr[position[0]][i] == num and position[1] != i:
                return False
        # check col
        for i in range(len(self.arr)):
            if self.arr[i][position[1]] == num and position[0] != i:
                return False

        # check square
        box_x = position[0] // 3
        box_y = position[1] // 3

        for row in range(box_x*3, box_x*3 + 3):
            for col in range(box_y*3, box_y*3 + 3):
                if self.arr[row][col] == num and (row, col) != position:
                    return False
        return True

    def solve(self):
        find = self.find_empty()
        if not find:
            print("Result: \n")
            s.print_board()
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.valid(i, (row, col)):
                self.arr[row][col] = i

                if self.solve():
                    return True
            self.arr[row][col] = 0
        return False

if __name__ == "__main__":
     s = SudokuSolver(g)
     s.solve()


