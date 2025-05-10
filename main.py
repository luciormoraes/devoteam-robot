from robot import Robot

def main():
    print("Enter room dimensions (width depth):")
    width, depth = map(int, input().split())

    while True:
        # Clean start each loop
        x = y = 0
        dir = ''
        commands = ''

        print("\nEnter starting position (x y direction):")
        x, y, dir = input().split()
        x, y = int(x), int(y)

        print("Enter commands:")
        commands = input().strip()

        try:
            robot = Robot(width, depth, x, y, dir)
            robot.execute_commands(commands)
            print(robot.report())
        except ValueError as e:
            print(e)

        print("\nDo you want to run another command? (yes/no):")
        answer = input().strip().lower()
        if answer != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()