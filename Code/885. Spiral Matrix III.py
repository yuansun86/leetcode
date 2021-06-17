class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        count = 1
        res = [[rStart, cStart]]
        direction_index = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = 1
        x, y = rStart, cStart
        while count < rows * cols:
            for _ in range(2):
                for __ in range(steps):
                    dx, dy = directions[direction_index]
                    x += dx
                    y += dy
                    if 0 <= x < rows and 0 <= y < cols:
                        res.append([x, y])
                        count += 1
                direction_index  = (direction_index + 1) % 4
            steps += 1
        return res