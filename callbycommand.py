from askinternet.shortsol import quickres
from tellcommand import talk


def write():
    talk("sir, please write your query ")
    command = input("enter query: ")
    quickres(command)

