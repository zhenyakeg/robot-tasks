#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.005)
def task_4_11():
    move_right()
    move_down()
    k=13
    for i in range (13):
        for j in range (k):
            fill_cell()
            move_down()
        if i==12:
            break
        move_up(12-i)
        move_right()
        k-=1
    move_left(12)


if __name__ == '__main__':
    run_tasks()
