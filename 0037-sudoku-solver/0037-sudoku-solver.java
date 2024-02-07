class Solution {
    public void solveSudoku(char[][] board) {
        solve(board, 0, 0);
    }

    public static boolean solve(char grid[][], int currentrow, int currentcol) {
        // Moving to next row when we reach to end of the column
        if (currentcol == 9) {
            return solve(grid, currentrow + 1, 0);
        }
        // Base case - When we reach to last matrix
        if (currentrow == 9) {
            return true;
        }
        if (grid[currentrow][currentcol] != '.') {
            return solve(grid, currentrow, currentcol + 1);
        }

        for (char val = '1'; val <= '9'; ++val) {
            if (isSafe(grid, currentrow, currentcol, val) == true) {
                grid[currentrow][currentcol] = val; // Putting value
                if (solve(grid, currentrow, currentcol + 1)) {
                    return true;
                }
                grid[currentrow][currentcol] = '.'; // Picking up the value
            }
        }
        return false;
    }

    public static boolean isSafe(char grid[][], int currentrow, int currentcol, char val) {
        // Row
        for (int col = 0; col < 9; col++) {
            if (grid[currentrow][col] == val) {
                return false;
            }
        }
        // Column
        for (int row = 0; row < 9; row++) {
            if (grid[row][currentcol] == val) {
                return false;
            }
        }
        // 3*3 SubMatrix
        int r = currentrow - currentrow % 3;
        int c = currentcol - currentcol % 3;
        for (int subrow = r; subrow < r + 3; subrow++) {
            for (int subcol = c; subcol < c + 3; subcol++) {
                if (grid[subrow][subcol] == val) {
                    return false;
                }
            }
        }
        return true;
    }
}