#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase, main as run_tests
from task_1 import main as run_task_1, compare_tasks
from task_2 import main as run_task_2, scalar_product, vector_product, vector_abs


class TestTask1(TestCase):
    def test_main(self):
        # sample input
        result = run_task_1(1, [[[1, 2, 1], [2, 3, 1], [4, 1, 2],
                                 [10, 10, 10], [15, 13, 10], [15, 7, 5]]])
        self.assertEqual(result, [20])

        # additional input
        result = run_task_1(2, [[[3, 2, 2], [4, 1, 3]], [[10, 4, 9], [8, 5, 8]]])
        self.assertEqual(result, [2, 5])

    def test_utils(self):
        task_1 = [4, 5, 1]
        task_2 = [2, 5, 2]
        task_3 = [6, 0, 4]
        task_4 = [2, 6, 2]
        task_5 = [4, 0, 3]
        self.assertEqual(compare_tasks(task_4, task_2), 1)
        self.assertEqual(compare_tasks(task_3, task_1), -1)
        self.assertEqual(compare_tasks(task_5, task_3), 1)
        self.assertEqual(compare_tasks(task_2, task_1), -1)
        self.assertEqual(compare_tasks(task_3, task_3), 0)


class TestTask2(TestCase):
    def test_main(self):
        # sample input 1
        result = run_task_2(20, [10, 10, 10], [-1, -1, -1], [-10, -10, -10], [1, 1, 1])
        self.assertAlmostEqual(result, 0.000000, places=6),

        # sample input 2
        result = run_task_2(100, [0, 0, 0], [2, 2, 0], [9, 0, 5], [-2, 2, 0])
        self.assertAlmostEqual(result, 5.000000, places=6),

    def test_utils(self):
        zero_vector = [0, 0, 0]
        vector_1 = [2, 2, 1]
        vector_2 = [4, 0, 3]

        self.assertEqual(vector_abs(zero_vector), 0)
        self.assertEqual(vector_abs(vector_1), 3)
        self.assertEqual(vector_abs(vector_2), 5)

        self.assertEqual(vector_product([1, 2, 3], [2, 1, -2]), [-7, 8, -3])
        self.assertAlmostEqual(vector_abs(vector_product([-1, 2, -2], [2, 1, -1])), 7.07, places=2)

        self.assertEqual(scalar_product(zero_vector, zero_vector), 0)
        self.assertEqual(scalar_product(vector_1, vector_1), vector_abs(vector_1) ** 2)
        self.assertEqual(scalar_product(vector_2, vector_1),
                         scalar_product(vector_1, vector_2))

if __name__ == '__main__':
    run_tests()
