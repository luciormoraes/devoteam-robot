from robot import Robot

def main():
    print("Enter room dimensions (width depth):")
    width, depth = map(int, input().split())

    print("Enter starting position (x y direction):")
    x, y, dir = input().split()
    x, y = int(x), int(y)

    print("Enter commands:")
    commands = input().strip()

    robot = Robot(width, depth, x, y, dir)
    robot.execute_commands(commands)
    print(robot.report())

if __name__ == "__main__":
    main()