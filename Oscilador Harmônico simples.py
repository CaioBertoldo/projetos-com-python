from vpython import*

#Cenário
cena = canvas(title='Oscilador Harmônico simples', width=600, height=300, center=vector(5,0,0), background=color.black)

#Objetos
parede = box(pos=vector(-20,0,0), size = vector(1,10,10), color = color.blue)
bloco = box(pos=vector(5,-3,0), size = vector(4,4,4), color = color.red)
solo = box(pos=vector(0,-5,0), size = vector(50,0.5,10), color = color.blue)
mola = helix(pos=vector(-20.5,-3,0), radius = 1.5, thickness = 0.5, coils = 5, color = color.yellow)

#Vínculo
mola.axis = bloco.pos - mola.pos

#Condições iniciais
bloco.vel = vector(0,0,0)
k = 400
m = 5
t = 0
dt = 0.001

#Equações
while True:
    rate(500)
    f = vector(-bloco.pos.x * k,0,0)
    acel = f / m
    bloco.pos = bloco.pos + (bloco.vel * dt)
    bloco.vel = bloco.vel + (acel * dt)
    mola.axis = bloco.pos - mola.pos
    t = t + dt
