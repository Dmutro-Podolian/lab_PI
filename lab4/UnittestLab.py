import unittest
from avl_priority_queue import AVLPriorityQueue


class TestAVLPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.new_queue = AVLPriorityQueue()

    def test_insert_single(self):
        self.new_queue.insert("task", 5)
        self.assertEqual(self.new_queue.peek(), ("task", 5))

    def test_insert_multiple_priorities(self):
        self.new_queue.insert("a", 1)
        self.new_queue.insert("b", 10)
        self.new_queue.insert("c", 5)

        self.assertEqual(self.new_queue.peek(), ("b", 10))

    def test_insert_equal_priorities(self):
        self.new_queue.insert("a", 5)
        self.new_queue.insert("b", 5)

        top = self.new_queue.peek()
        self.assertIn(top[0], ["a", "b"])
        self.assertEqual(top[1], 5)

    def test_extract_max(self):
        self.new_queue.insert("a", 1)
        self.new_queue.insert("b", 10)
        self.new_queue.insert("c", 5)

        value, priority = self.new_queue.extract_max()

        self.assertEqual(value, "b")
        self.assertEqual(priority, 10)

    def test_extract_order(self):
        self.new_queue.insert("a", 3)
        self.new_queue.insert("b", 7)
        self.new_queue.insert("c", 1)

        res = [
            self.new_queue.extract_max(),
            self.new_queue.extract_max(),
            self.new_queue.extract_max()
        ]

        self.assertEqual(res, [
            ("b", 7),
            ("a", 3),
            ("c", 1)
        ])

    def test_extract_empty(self):
        self.assertIsNone(self.new_queue.extract_max())

    def test_peek_does_not_remove(self):
        self.new_queue.insert("a", 10)
        self.new_queue.insert("b", 5)

        first = self.new_queue.peek()
        second = self.new_queue.peek()

        self.assertEqual(first, second)

    def test_peek_empty(self):
        self.assertIsNone(self.new_queue.peek())

    def test_many_insertions(self):
        for i in range(64):
            self.new_queue.insert(f"task{i}", i)

        value, priority = self.new_queue.peek()

        self.assertEqual(priority, 63)


if __name__ == "__main__":
    unittest.main()
