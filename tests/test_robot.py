import unittest
from robot import Robot

class TestRobot(unittest.TestCase):

    def test_example_case_1(self):
        robot = Robot(5, 5, 1, 2, 'N')
        robot.execute_commands('RFRFFRFRF')
        self.assertEqual(robot.report(), 'Report: 1 1 N')

    def test_example_case_2(self):
        robot = Robot(5, 5, 0, 0, 'E')
        with self.assertRaises(ValueError):
            robot.execute_commands('RFLFFLRF')

    def test_turning_left_right(self):
        robot = Robot(5, 5, 0, 0, 'N')
        robot.turn_right()
        self.assertEqual(robot.direction.name, 'E')
        robot.turn_left()
        self.assertEqual(robot.direction.name, 'N')

    def test_move_out_of_bounds(self):
        robot = Robot(5, 5, 0, 0, 'S')
        with self.assertRaises(ValueError):
            robot.move_forward()

    def test_invalid_command(self):
        robot = Robot(5, 5, 0, 0, 'N')
        with self.assertRaises(ValueError):
            robot.execute_commands('X')

if __name__ == '__main__':
    unittest.main()