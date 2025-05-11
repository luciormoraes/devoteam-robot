# Project Architecture: Devoteam Robot

## Overview
The Robot Controller is a command-line Python application that simulates a robot navigating a grid-based room based on user input. It follows a clean separation of concerns, making it easy to maintain, test, and expand (e.g., add a web or GUI layer later).

## Directory Structure
```bash
robot-controller/
├── src/
│   ├── robot.py        # Core robot logic: position, direction, movement
│   ├── cli.py          # Command-line interface: input handling, session loop
│   └── main.py         # Entry point that launches the CLI
├── tests/
│   └── test_robot.py   # Unit tests for core logic
├── README.md           # Documentation and usage guide
├── .gitignore          # Ignores Python artifacts, editor files, etc.
```

## Application Flow
1. main.py

- Entry point.

- Calls run_cli() from cli.py.

2. cli.py

- Prompts the user for:

    - Room dimensions

    - Starting position and direction

    - Command string

- Validates all input (room size, direction, position, commands).

- Instantiates a Robot and executes the command sequence.

- Prints the final report or error message.

- Allows the user to repeat the process in a loop.

3. robot.py

- Contains:

    - Direction Enum: handles orientation logic (left/right)

    - Robot class: maintains position, executes movement, handles bounds

- Clean separation from CLI logic — easily testable and reusable.

4. test_robot.py

- Tests:

    - Command execution correctness

    - Turning behavior

    - Movement logic

    - Error handling (invalid command, out-of-bounds)

## Key Components
Robot class (robot.py)
- Tracks x, y, and direction

- Executes commands (L, R, F)

- Validates bounds

- Reports current state

Direction Enum
- Defines movement vectors per direction (N, E, S, W)

- Implements left/right rotation logic

CLI interface (cli.py)
- Manages user input loop

- Validates room and command inputs

- Connects input to robot logic

Testability
- Core logic is decoupled from user I/O

- Unit tests written using built-in unittest module

- CLI can be extended or replaced (e.g., with web or GUI interface)

## Extensibility Ideas
- Add obstacle detection or dynamic rooms

- Add a web API layer (FastAPI or Flask)

- Add persistent history of moves or logs