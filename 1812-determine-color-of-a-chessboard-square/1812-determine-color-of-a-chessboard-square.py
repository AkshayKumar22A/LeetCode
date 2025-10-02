class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        board = [
            [True if (row + col) % 2 == 0 else False for col in range(8)]
            for row in range(8)
        ]
        freq_map = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
        column = freq_map.get(coordinates[0])
        row = int(coordinates[1])     
        print(board[0][0])  
        return board [column-2][row-1]