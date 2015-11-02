#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
Maximizing Bonus

You work at an ecommerce based company. Since you are working for a long time, being tired
of your work you decided to go on vacation to Amsterdam for couple of days.
You came back to office and found a pile of tasks waiting for you.
In particular you have n tasks T1, T2, ..., Tm.
Each task Ti has a deadline Di, bonus Bi and time you will take to complete it is Pi.

Now, you want to schedule these tasks in such a way that you can maximize your bonus.
You will only get bonus if you complete your job within the deadline.

[Input]
First line of input contains integer t denoting number of test cases.
First line of each test case begins With a line containing integer n denoting number of tasks.
Next n lines of each test case contains 3 integers D, B, P
denoting deadline, bonus and time you will take to complete that task.

[Output]
For each test case print a single line containing maximum bonus that you can get.

[Constraints]
1<=t<=10
1<=n<=1000
1<=D<=1000
1<=P<=D
1<=B<=1000

Sample Input
1
6
1 2 1
2 3 1
4 1 2
10 10 10
15 13 10
15 7 5

Sample Output
20
"""


def compare_tasks(task1, task2):
    # bonus should be maximal
    if task1[1] > task2[1]:
        return 1
    elif task1[1] < task2[1]:
        return -1
    # duration should be minimal
    if task1[2] > task2[2]:
        return -1
    elif task1[2] < task2[2]:
        return 1
    return 0


def main(cases_count, cases):
    """
    Algorithm: Sort tasks by bonus (greather first) and deadline (greather last),
    then iterate throgh sorted tasks calculate maximal bonus that I can get in limited time.

    NOTE: Python uses stable merge sort algorithm, so I can sort by several values simultaneously.

    Time complexity: ~O(N1 + N2 + ... + Nn)
    where N1, N2, ..., Nn - number of tasks on every test case
    n - number of test cases
    """
    case_bonuses = []
    for case_tasks in cases:
        # assuming that max value of deadline is a whole time for tasks processing
        time = max(task[0] for task in case_tasks)
        bonuses = 0

        sorted_tasks = sorted(case_tasks, cmp=compare_tasks, reverse=True)

        for deadline, bonus, duration in sorted_tasks:
            if time - duration < 0:
                continue
            time -= duration
            bonuses += bonus

        case_bonuses.append(bonuses)

    return case_bonuses


if __name__ == '__main__':
    cases_count = input()
    cases = []
    for _ in xrange(cases_count):
        taks_count = input()
        tasks = []
        for i in xrange(taks_count):
            tasks.append(map(int, raw_input().split()))
        cases.append(tasks)

    print main(cases_count, cases)
