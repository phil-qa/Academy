import unittest
import collections
from unittest.mock import TestCase

collections.Callable = collections.abc.Callable
from Tester import Tester


def get_input(value):
    return input(value)

class TestTheTester(unittest.TestCase):
    def test_initialisation(self):
        tester = Tester()
        self.assertGreater(len(tester.Tests), 0)  # add assertion here

    @patch('get a correct answer', return_value = ['int'])
    def test_a_test_is_run(self):
        tester = Tester()
        response = tester.run_test('001')




if __name__ == '__main__':
    unittest.main()
