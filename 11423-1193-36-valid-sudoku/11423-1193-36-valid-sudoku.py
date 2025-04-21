class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate rows
        # using set to make is n(1)
        for i in range(len(board)):  # i is 1st row, 2nd row, 3rd row, until 9th rows
            # initialize a set for each row
            row_set = set()
            print(f"row set: {row_set}")

            for j in range(len(board[i])):
                # board[i][j] is the item in the row
                item = board[i][j]

                if item in row_set:
                    return False
                elif item != ".":
                    row_set.add(item)

        # validate columns
        for i in range(len(board)):  # i is 1st row, 2nd row, 3rd row, until 9th rows
            # initialize a set for each row
            col_set = set()

            for j in range(len(board[i])):
                # board[j][i] is the item in the column
                item = board[j][i]

                if item in col_set:
                    return False
                elif item != ".":
                    col_set.add(item)

        # validate sub-boxes
        # create a list of all the sub boxes start point in the board
        start_point_sub_box = [
            [0, 0],
            [0, 3],
            [0, 6],
            [3, 0],
            [3, 3],
            [3, 6],
            [6, 0],
            [6, 3],
            [6, 6],
        ]

        for i, j in start_point_sub_box:
            # initialize the set when start from each start point
            sub_box_set = set()

            # loop through each sub box
            for k in range(3):
                for l in range(3):
                    item = board[i + k][j + l]
                    if item in sub_box_set:
                        return False
                    elif item != ".":
                        sub_box_set.add(item)
        return True
