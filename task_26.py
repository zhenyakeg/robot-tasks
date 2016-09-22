#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.002)
def task_2_4():
    def star():
        move_right()
        fill_cell()
        move_right()
        move_down()
        fill_cell()
        move_down()
        move_left()
        fill_cell()
        move_up()
        fill_cell()
        move_left()
        fill_cell()
        move_up()
    move_right(36)
    for i in range (9):
        for j in range (4):
            star()
            move_down(4)
        star()
        move_up(16)
        move_left(4)
    for j in range(4):
        star()
        move_down(4)
    star()


if __name__ == '__main__':
    run_tasks()
