import unittest

from task_1.solution import strict


class TestStringMethods(unittest.TestCase):

    def test_sum_two(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        self.assertEqual(sum_two(1, 2), 3)
        self.assertEqual(sum_two(a=1, b=2), 3)
        self.assertEqual(sum_two(1, b=2), 3)
        self.assertEqual(sum_two(b=2, a=1), 3)
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)
        with self.assertRaises(TypeError):
            sum_two(2.4, 1)
        with self.assertRaises(TypeError):
            sum_two(2.4, 2.4)
        with self.assertRaises(TypeError):
            sum_two(a=1, b=2.4)
        with self.assertRaises(TypeError):
            sum_two(b=1, a=2.4)
        with self.assertRaises(TypeError):
            sum_two(b=2.4, a=2.4)

    def test_sum_empty(self):
        @strict
        def empty():
            return 1

        self.assertEqual(empty(), 1)

    def test_all_types(self):
        @strict
        def all_types(a: bool, b: int, c: float, d: str) -> str:
            return str(a) + str(b) + str(c) + d

        self.assertEqual(all_types(True, 1, 1.1, "1"), "True11.11")
        self.assertEqual(all_types(a=True, b=1, c=1.1, d="1"), "True11.11")
        self.assertEqual(all_types(c=1.1, a=True, d="1", b=1), "True11.11")
        self.assertEqual(all_types(True, 1, c=1.1, d="1"), "True11.11")
        with self.assertRaises(TypeError):
            all_types(1, 1, 1.1, "1")
        with self.assertRaises(TypeError):
            all_types(a=True, b=1.1, c=1, d="1")
        with self.assertRaises(TypeError):
            all_types(True, 1, c=1.1, d=1)
        with self.assertRaises(TypeError):
            all_types(b=True, a=1, d=1.1, c=1.1)


if __name__ == "__main__":
    unittest.main()
