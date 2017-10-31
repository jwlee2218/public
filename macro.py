from apscheduler.schedulers.blocking import BlockingScheduler
from pymouse import PyMouse
from pynput import keyboard

m=PyMouse()
x=785
y=580
a=132
b=481
c=132
d=557
e=635
f=581

def on_release(key):
    print('{0} has been pressed'.format(key))
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.left:
        subject1()
        number()
    if key == keyboard.Key.up:
        subject2()
        number()
    if key == keyboard.Key.shift_r:
        submit()

def click():
    m.click(x,y)
    with keyboard.Listener(
        on_release=on_release) as listener:
        listener.join()

def subject1():
    m.click(a,b)

def subject2():
    m.click(c,d)

def number():
    m.click(e,f)

def submit():
    m.click(x,y)


sched=BlockingScheduler()

sched.add_job(click,'cron',hour='0',minute='21',second='30')
sched.start()

            
