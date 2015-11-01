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
1<=n<=10^3
1<=D<=10^3
1<=P<=D
1<=B<=10^3

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
    # comparing deadlines
    if task1[0] > task2[0]:
        return 1
    elif task1[0] < task2[0]:
        return -1
    # comparing bonuses
    if task1[1] > task2[1]:
        return 1
    elif task1[1] < task2[1]:
        return -1
    return 1


if __name__ == '__main__':
    cases = input()
    for case in xrange(cases):
        taks_count = input()
        tasks = []
        for i in xrange(taks_count):
            tasks.append(map(int, raw_input().split()))

        # assuming that max value of deadline is a whole time for tasks processing
        time = max(item[0] for item in tasks)
        bonuses = 0

        sorted_tasks = sorted(tasks, cmp=compare_tasks, reverse=True)

        for deadline, bonus, duration in sorted_tasks:
            if time - duration < 0:
                continue

            time -= duration
            bonuses += bonus

        print bonuses
