import pygame as pg
import random
import math
pg.init()
brojbombi=10
button=[]
bombe=[]
zastave=[]
slike=[]
kraj=[]
duzina=7
visina=13
x=0
y=0
varijabla=0
varijabla2=0
zastava=0
slika=0
pobeda=0
D=1000
W=30*duzina
H=30*visina
FPS=60
RW=W/duzina
RH=H/visina
screen=pg.display.set_mode((W,H))
clock=pg.time.Clock()
running=True
def crtanjeslika(k,button):
    file_path='./minolovac/'+str(k)+'.png'
    slika = pg.image.load(file_path)
    slika_rect=slika.get_rect()
    slika_rect.center=button.center       
    screen.blit(slika,slika_rect)
def pravljenjeliste(duzina,visina,bombe):
    for i in range(duzina):
        lista=[]
        for j in range(visina):
            lista.append(j)
        bombe.append(lista)
# pravimo polja
for i in range(1,duzina+1):
    lista2=[]
    for j in range(1,visina+1):
        c=j+i
        if c%2==0:
            rc=(100,255,100)
        else:
            rc=(100,150,100)
        pg.draw.rect(screen,rc,(x,y,RW,RH))
        lista2.append(pg.Rect(x,y,RW,RH))
        y=RH*j
    button.append(lista2)
    x=RW*i
    y=0
# pravimo listu x y
pravljenjeliste(duzina,visina,kraj)
pravljenjeliste(duzina,visina,bombe)
pravljenjeliste(duzina,visina,zastave)
pravljenjeliste(duzina,visina,slike)
pg.display.update()
while varijabla2<1:
    for event in pg.event.get():
        for i in  range(duzina):
            for j in range(visina):
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and button[i][j].collidepoint(event.pos):
                    bombe[i][j]='mc'
                    okoi=i-1
                    mx=i
                    my=j
                    slike[i][j]='slika'
                    slika+=1
                    while okoi<i+2:
                        okoj=j-1
                        while okoj<j+2:
                            if okoi>=0 and okoj>=0 and okoi<duzina and okoj<visina:
                                bombe[okoi][okoj]='mc'
                            okoj+=1
                        okoi+=1
                    varijabla2+=1
#pravimo bombe
while varijabla<brojbombi:
    x=random.randint(0,duzina-1)
    y=random.randint(0,visina-1)
    if bombe[x][y]!="bomba" and bombe[x][y]!='mc':
        bombe[x][y]="bomba"
        varijabla+=1
#pravimo brojeve
for i in range(duzina):
    for b in range (visina):
        brojbombioko=0
        j=i-1
        while j<i+2:
            g=b-1
            while g<b+2:
                if j>=0 and g>=0 and j<duzina and g<visina :
                    if bombe[i][b]!="bomba":
                        if bombe[j][g] == "bomba":
                            brojbombioko+=1
                g+=1
            j+=1
        if bombe[i][b]!="bomba":
            bombe[i][b]=brojbombioko
#petlja
crtanjeslika(bombe[mx][my],button[mx][my])
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPEA:
                running=False
        for i in  range(duzina):
            for j in range(visina):
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    if button[i][j].collidepoint(event.pos) and zastave[i][j]!='zastava' and slike[i][j]!='slika':
                        crtanjeslika(bombe[i][j],button[i][j])
                        slike[i][j]='slika'
                        slika+=1
                elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                    if button[i][j].collidepoint(event.pos) and zastave[i][j]!='zastava' and slike[i][j]!='slika' and zastava<=brojbombi:
                        zastave[i][j]='zastava'
                        zastava+=1
                        crtanjeslika('zastava',button[i][j])
                    elif button[i][j].collidepoint(event.pos) and zastave[i][j]=='zastava':
                        zastave[i][j]=0
                        zastava-=1
                        pg.draw.rect(screen,rc,(RW*i,RH*j,RW,RH))
                if bombe[i][j]==0 and slike[i][j]=='slika':
                    okoi=i-1
                    while okoi<i+2:
                        okoj=j-1
                        while okoj<j+2:
                            if okoi>=0 and okoj>=0 and okoi<duzina and okoj<visina:
                                if slike[okoi][okoj]!='slika':
                                    crtanjeslika(bombe[okoi][okoj],button[okoi][okoj])
                                    slike[okoi][okoj]='slika'
                                    slika+=1
                            okoj+=1
                        okoi+=1             
                if bombe[i][j]=='bomba' and slike[i][j]=='slika':
                    pg.display.update()
                    pg.time.delay(D)
                    running=False
                if slika+zastava==visina*duzina and pobeda<1:
                    print('pobeda')
                    text = pg.font.SysFont('freesansbold', 60).render('Pobeda', True, 'Yellow')
                    text_rect = text.get_rect()
                    text_rect.center = W/2,H/4
                    screen.blit(text, text_rect)
                    pobeda+=1
    pg.display.update()
    clock.tick(FPS)
pg.quit()