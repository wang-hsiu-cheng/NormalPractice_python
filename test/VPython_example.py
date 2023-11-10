"""
 VPython教學: 3.等速度直線運動
 Ver. 1: 2018/2/18
 Ver. 2: 2019/9/5
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 0.1   # 木塊邊長
L = 1        # 地板長度
v = -0.003     # 木塊速度
t = 0        # 時間
dt = 0.01    # 時間間隔
g = -9.8

"""
 2. 畫面設定
"""
scene = canvas(title="1D Motion", width=800, height=600, x=0, y=0, center=vec(0, 0.1, 0), background=vec(0, 0.6, 0.6))
floor = box(pos=vec(0, -1, 0), size=vec(L, 0.1*size, 0.5*L), color=color.yellow)
cube = box(pos=vec(-0.5*L + 0.5*size, 0.55*size, 0), size=vec(size, size, size), color=color.red, v=vec(v, 0, 0))
#cube = box(pos=vec(-0.5*L + 0.5*size, 0.55*size, 0), length=size, height=size, width=size, color=color.red, v=vec(v, 0, 0))
gd = graph(title="x-t plot", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="x(m)")
gd2 = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
yt = gcurve(graph=gd, color=color.red)
vt = gcurve(graph=gd2, color=color.red)

"""
 3. 物體運動部分, 木塊到達地板邊緣時停止執行
"""
print("cube.pos.y = ", cube.pos.y)
while(cube.pos.y >= -1*L+ 0.55*size):
    rate(1000)
    cube.pos.y += v*dt+g*dt**2/2
    yt.plot(pos = (t, cube.pos.y))
    vt.plot(pos = (t, cube.v.y))
    t += dt
    

print("t = ", t)

