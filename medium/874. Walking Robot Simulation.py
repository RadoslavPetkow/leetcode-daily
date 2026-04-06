class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        obstacle_set = set((x, y) for x, y in obstacles)

        # North, East, South, West
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        direction = 0
        x, y = 0, 0
        max_distance = 0

        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction - 1) % 4
            else:
                dx, dy = directions[direction]

                for _ in range(command):
                    next_x = x + dx
                    next_y = y + dy

                    if (next_x, next_y) in obstacle_set:
                        break

                    x, y = next_x, next_y
                    max_distance = max(max_distance, x * x + y * y)

        return max_distance