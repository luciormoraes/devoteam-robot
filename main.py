'''
This is a simple robot simulation program that allows the user to control a robot
in a rectangular room. The robot can move forward, turn left or right, and report its position.
The program includes error handling for invalid inputs and out-of-bounds movements.
'''

from robot import Robot

def main():
    print("Enter room dimensions (width depth), format example '4 5': ")
    while True:
        try:
            width, depth = map(int, input().split())
            if width <= 0 or depth <= 0:
                print("Room size must be at least 1x1.")
                continue
            break
        except ValueError:
            print("Please enter two integers for room dimensions, like: 5 5")

    while True:
        # Get starting position safely
        while True:
            print("\nEnter starting position (x y direction), format example '3 3 E':")
            parts = input().split()
            if len(parts) != 3:
                print("Please enter exactly 3 values: x y direction (e.g. 1 2 N)")
                continue
            try:
                x, y = int(parts[0]), int(parts[1])
                dir = parts[2].upper()
                break
            except ValueError:
                print("x and y must be integers.")

        print("Enter commands: example 'RFRFFRFRF'")
        commands = input().strip().upper()

        try:
            robot = Robot(width, depth, x, y, dir)
            robot.execute_commands(commands)
            print(robot.report())
        except ValueError as e:
            print(f"Error: {e}")

        print("\nDo you want to run another command? (yes/no):")
        answer = input().strip().lower()
        if answer != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()