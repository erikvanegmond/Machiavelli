import unittest

from game import utils


class TestUtilsMethods(unittest.TestCase):
    def test_generate_question_with_options(self):
        options = ["option 1", "option 2"]
        correct_response = ("option 1(press 0) option 2(press 1) ", [0,1])
        actual_response = utils.generate_question(options)
        self.assertEqual(actual_response, correct_response)

    def test_generate_question_without_options(self):
        options = []
        correct_response = ("", [])
        actual_response = utils.generate_question(options)
        self.assertEqual(actual_response, correct_response)


if __name__ == '__main__':
    unittest.main()
