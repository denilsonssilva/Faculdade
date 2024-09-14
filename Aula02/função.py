def enigma1 (x,y):
    x += 20
    y += 50

def enigma2 ():
    x = 30
    y = 60

def enigma3 ():
    global x, y
    x += 40
    y += 70

x = 100
y = 200

enigma1 (x,y)
#120, 250

enigma2 ()
#30, 60

enigma3 ()
#