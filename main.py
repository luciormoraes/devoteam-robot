from enum import Enum

class Direction(Enum):
    N = (0, 1)
    E = (1, 0)
    S = (0, -1)
    W = (-1, 0)

    @staticmethod
    def left(current):
        order = [Direction.N, Direction.W, Direction.S, Direction.E]
        idx = order.index(current)
        return order[(idx + 1) % 4]

    @staticmethod
    def right(current):
        order = [Direction.N, Direction.E, Direction.S, Direction.W]
        idx = order.index(current)
        return order[(idx + 1) % 4]


class Robot:
    def __init__(self, room_width, room_depth, start_x, start_y, start_dir):
        self.room_width = room_width
        self.room_depth = room_depth
        self.x = start_x
        self.y = start_y
        self.direction = Direction[start_dir]

    def execute_commands(self, commands):
        for cmd in commands:
            if cmd == 'L':
                self.turn_left()
            elif cmd == 'R':
                self.turn_right()
            elif cmd == 'F':
                self.move_forward()
            else:
                raise ValueError(f"Invalid command: {cmd}")

    def turn_left(self):
        self.direction = Direction.left(self.direction)

    def turn_right(self):
        self.direction = Direction.right(self.direction)

    def move_forward(self):
        dx, dy = self.direction.value
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < self.room_width and 0 <= new_y < self.room_depth:
            self.x = new_x
            self.y = new_y
        else:
            print(f"Error: Robot moved out of bounds to ({new_x}, {new_y})")
            exit(1)

    def report(self):
        return f"Report: {self.x} {self.y} {self.direction.name}"


def main():
    print("Example 1")
    robot1 = Robot(5, 5, 1, 2, 'N')
    robot1.execute_commands('RFRFFRFRF')
    print(robot1.report())

    print("\nExample 2:")
    robot2 = Robot(5, 5, 0, 0, 'E')
    robot2.execute_commands('RFLFFLRF')
    print(robot2.report())


if __name__ == "__main__":
    main()