from turtle import *
import random, os

os.system('mode con: cols=25 lines=7')

bsize = random.randint(25,80)
girth = random.randint(25,bsize)
length = random.randint(150,450)
xoffset = 0 - (length/2)

print('Ball size:',bsize)
print('Girth:',girth)
print('Length:',length)

setup(length + bsize + 225, bsize*4 + 195)
title('Dick Window')
speed(15)

bgcolor('black')
color('black')
setx(xoffset)

print('Drawing...')
color('#ffdbaf')

#balls
begin_fill()
circle(bsize)
circle(0 - bsize)
end_fill()

#shaft 1
begin_fill()
sety(0 - girth)
forward(length)
end_fill()

#head
color('pink')
begin_fill()
circle(girth,180)
end_fill()

#shaft 2
color('#ffdbaf')
begin_fill()
forward(length)
sety(0)

#shaft fill
setpos(length + xoffset, 0 - girth)
setpos(length + xoffset, girth)
setpos(xoffset,0)
end_fill()

print('Complete.')
done()