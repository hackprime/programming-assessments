#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
Paper Planes

Its spring :) Time for paper plane. Kasukabe Defence Group has decided to have a paper plane
competition. Masao and Bo, both Shinchan friends, are good at Origami,
a Japanese art of designing sculpture using flat sheet of paper.
They have designed very good paper planes which can fly for exactly t seconds and at a constant
speed and direction.
They, both, throw their plane in air simultaneously.
Bingo!!! Kazama gets another chance to show his superior mathematical skill.
Now he calculated the minimum distance between them during their flight of t seconds.
He knows the initial coordinate of Bo's plane and Masao's plane
and along with their speed and direction.

[Input]
First line of input contains an integer, t, time duration of flight.
Then in next line initial coordinate of Bo's plane (bx, by. bz) is given.
Next line contains another three space separated integers, (bvx, bvy, bvz). the speed of Bo's plane
in x-axis, y-axis and z-axis respectevely.
In next line, initial coordinate of Masao' Plane (mx, my, m2) is provided followed by its speed
(mvx, mvy mvz) in x-axis, y-axis and z-axis, respectively in next line.

[Output]
Print the minimum distance which Bo's and Masao's plane can get during the flight
with answer rounded off to exactly 6 digit after decimal point.

[Constraints]:
0 <= t <= 10000
-10000 <= bx, by, bz <= 10000
-10000 <= bvx, bvy, bvz <= 10000
-10000 <= mx, my, mz <= 10000
-10000 <= mvx, mvy, mvz <= 10000

Sample Input #0
20
10 10 10
-1 -1 -1
-10 -10 -10
1 1 1

Sample Output #0
0.000000

Sample Input #1
100
0 0 0
2 2 0
9 0 S
-2 2 O

Sample Output #1
5.000000

Explanation
Sample Case #0: After 10 second of their flights, both plane will have same coordinate (0, 0, 0).
So distance between them will be 0 at that point of time.

Sample Case #1: After 5 second, Masao's plane coordinate will be (4.5, 4.5, 0)
and Bo's (4.5, 4.5, 5).
"""
from math import sqrt


def get_int_triplet():
    return map(int, raw_input().split())


def distance_3d(p1, p2):
    summary = 0
    for i in xrange(3):
        summary += (p2[i] - p1[i]) ** 2
    return sqrt(summary)


if __name__ == '__main__':
    time = input()
    bo_initial_point = get_int_triplet()
    bo_speeds = get_int_triplet()
    masao_initial_point = get_int_triplet()
    masao_speeds = get_int_triplet()

    min_distance = float('inf')
    previous_distance = float('inf')

    for t in range(time+1):
        distance = distance_3d([bo_initial_point[i] + bo_speeds[i] * t for i in xrange(3)],
                               [masao_initial_point[i] + masao_speeds[i] * t for i in xrange(3)])
        if distance < min_distance:
            min_distance = distance

        if previous_distance > distance:
            previous_distance = distance
        else:
            break

    print "%.6f" % min_distance
