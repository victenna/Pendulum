import turtle,time
wn=turtle.Screen()
wn.setup(900,900)
wn.bgpic('bground0.gif')
turtle.tracer(2)

t1=turtle.Turtle('turtle')
t1.hideturtle()
t1.color('blue')
t1.penup()
t1.begin_poly()
t1.fd(400)
t1.left(90)
t1.circle(30.358)
t1.fd(4)
t1.left(90)
t1.fd(400)
t1.end_poly()
wn.addshape('pend',t1.get_poly())
t2=turtle.Turtle(shape='pend')
t2.up()
t2.color('blue')

FONT=('Times New Roman',20,'bold')
angle=float(wn.textinput('Колебания маятника',\
                         'Введите угол отклонения'))
angle=-angle
t2.right(angle)
q=0
N=110

wn.bgpic('bground1.gif')
while True:
    for i in range(N):
        q=q+0.01*angle/60
        t2.lt(q)
        time.sleep(0.01)
        
    for i in range(N):
        q=q-0.01*angle/60
        t2.lt(q)
        time.sleep(0.01)
        
    for i in range(N):
        q=q+0.01*angle/60
        t2.lt(-q)
        time.sleep(0.01)
        
    for i in range(N):
        q=q-0.01*angle/60
        t2.lt(-q)
        time.sleep(0.01)
    
