#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
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
    move_right()
    move_down()
    star()




if __name__ == '__main__':
    run_tasks()
