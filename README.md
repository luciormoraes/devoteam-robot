# Robot Controller

This repository contains a simple robot controller written in Python. The robot can navigate a room using the commands `L` (turn left), `R` (turn right), and `F` (move forward). If the robot moves out of bounds, program shows the message `out of bound` .

- `L`  : the robot turns left 90 degrees and remains on the current grid point.
- `R` : the robot turns right 90 degrees and remains on the current grid point.
- `F` : the robot moves forward one grid point in the direction of the current orientation and maintains the same orientation.
- Starting Position: must be: X, Y, Direction. Direction will be `N`, `S`, `E`, `W`. X and Y must be integers.
- Report: after the command execution, report will show the final position.

## Project Structure

```
robot.py        # Core robot logic
main.py          # Command-line interface runner
test_robot.py # Unit tests
```

## Requirements
- Python 3.7+

## Running the App

To start the robot controller in command-line mode:

```bash
python main.py
```

### Example Run
```
Enter room dimensions (width depth):
5 5
Enter starting position (x y direction):
1 2 N
Enter commands to robot move in the grid:
RFRFFRFRF
Report: 1 1 N

Do you want to run another command? (yes/no):
yes
Enter starting position (x y direction):
0 0 E
Enter commands:
RFLFFLRF
Report: out of bound

Do you want to run another command? (yes/no):
no
Exiting the program.
```

## Running Tests

This project uses Python's built-in `unittest` framework. To run the tests:

```bash
python -m unittest test_robot.py
```

## Notes
- The core logic is isolated in `robot.py` to make testing and potential future UI development easy.
- Invalid commands or out-of-bound movements will raise a `ValueError`.
- Supports running multiple commands in a single session until the user chooses to exit.

---

