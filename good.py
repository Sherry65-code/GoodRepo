from time import time
from subprocess import run, PIPE

st = 0
et = 0
t1 = 0
t2 = 0
def sleep(timeforsleep):
    s = time()
    while s+timeforsleep>time():
        pass

def sleepTk(timeforsleep, windowname):
    s = time()
    while s+timeforsleep>time():
        windowname.update()

def StartTimer():
    global st
    st = time()

def EndTimer():
    global et,t1,t2
    et = time()
    t1 = time()
    t2 = time()
    left = t2-t1
    return (et-st)-left

def cmd(cmd):
    p1 = run(cmd.split(" "), capture_output=True)
    return p1.stdout.decode()