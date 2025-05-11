from robot import Robot

VALID_DIRECTIONS = {"N", "S", "E", "W"}
VALID_COMMANDS = {"L", "R", "F"}

def get_positive_ints(prompt):
    while True:
        try:
            values = list(map(int, input(prompt).split()))
            if len(values) != 2 or any(v <= 0 for v in values):
                raise ValueError
            return values
        except ValueError:
            print("Please enter two positive integers (e.g. 5 5)")

def get_starting_position(room_width, room_depth):
    while True:
        parts = input("Enter starting position (x y direction):\n").split()
        if len(parts) != 3:
            print("Please enter exactly 3 values: x y direction (e.g. 1 2 N)")
            continue

        try:
            x, y = int(parts[0]), int(parts[1])
            direction = parts[2].upper()

            if not (0 <= x < room_width and 0 <= y < room_depth):
                print(f"Starting position must be within room bounds: 0 ≤ x < {room_width}, 0 ≤ y < {room_depth}")
                continue

            if direction not in VALID_DIRECTIONS:
                print("Direction must be one of: N, S, E, W")
                continue

            return x, y, direction
        except ValueError:
            print("x and y must be integers.")

def get_valid_commands():
    while True:
        commands = input("Enter commands to move the robot:\n").strip().upper()
        if all(c in VALID_COMMANDS for c in commands):
            return commands
        print("Commands must only contain the characters: L, R, F")

def main():
    room_width, room_depth = get_positive_ints("Enter room dimensions (width depth):\n")

    while True:
        x, y, direction = get_starting_position(room_width, room_depth)
        commands = get_valid_commands()

        try:
            robot = Robot(room_width, room_depth, x, y, direction)
            robot.execute_commands(commands)
            print(robot.report())
        except ValueError as e:
            print(f"Error: {e}")

        again = input("\nDo you want to run another command? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
