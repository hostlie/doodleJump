import pyxel

pyxel.init(128, 128)

pyxel.load("sample.pyxres")

data = {}
data["x"] = 0
data["y"] = 0

def update():
    global data

    if pyxel.btn(pyxel.KEY_UP):
        data['y'] -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        data['y'] += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        data['x'] -= 1
    if pyxel.btn(pyxel.KEY_RIGHT):
        data['x'] += 1
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    global data
    pyxel.cls(1)
    pyxel.blt(x=data['x'],y=data['y'],img=0,u=0,v=0,w=16,h=16,colkey=0,)

pyxel.run(update, draw)