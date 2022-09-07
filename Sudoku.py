from turtle import *
import turtle

#tehdaan olio
tausta = turtle.Turtle()
tausta.speed(0)
tausta.hideturtle()
tausta.penup()
tausta.fillcolor("white")

kirrivit = [False,False,False,False,False,False,False,False,False]
numrivit = [False,False,False,False,False,False,False,False,False]
neliot = [False,False,False,False,False,False,False,False,False]

#maaritellaan muuttujat
gameon = True
kirjain = ["A","B","C","D","E","F","G","H","I"]
tyhja = 10
numerovali = 50
xalku = -185
yalku = 155



#maaritellaan pelin alkupiste
alkupiste = [3,10,10,10,10,4,10,9,10,9,1,10,2,10,7,10,3,10,10,8,10,10,10,1,6,10,7,5,7,10,8,10,10,10,1,3,2,10,10,10,10,10,10,10,10,8,3,10,4,2,10,10,7,10,10,2,10,1,10,9,10,8,10,1,10,10,10,7,2,5,6,9,10,10,3,5,10,10,10,2,1]
ruudukkonum = alkupiste


#alkutekstit
print("Tervetuloa sudokuun")

#tehdaan ruudukko
def ruudukko(turt,x,y,ruudut,vali,pituus):
    xcor = x 
    ycor = y
    for i in range(ruudut+1):
        turt.penup()
        turt.goto(x,ycor)
        turt.pendown()
        turt.forward(pituus)
        ycor -= vali
    turt.right(90)
    for i in range(ruudut+1):
        turt.penup()
        turt.goto(xcor,y)
        turt.pendown()
        turt.forward(pituus)
        xcor += vali

#tehdaan coordinaatti kirjaimet ruudukkoon
def kirjaimet(turt,x,y,vali,maara,kirjain):
    miinusy = y
    for z in range(maara):
        turt.penup()
        turt.goto(x,miinusy)
        turt.pendown()
        turt.write(kirjain[z], font=("Times New Roman",20))
        miinusy = miinusy - vali

#tehdaan coordinaatti numerot
def numerot(turt,x,y,vali,maara):
    miinusx = x
    for z in range(maara):
        turt.penup()
        turt.goto(miinusx,y)
        turt.pendown()
        turt.write(z+1, font=("Times New Roman",20))
        miinusx = miinusx + vali

#piirretaan pelin aloituspisteessa olevat numerot
def ruudukkoalkupiste(turt,numerot,xalku,yalku,vali):
    xcor = 0
    ycor = 0
    turt.penup()
    turt.goto(xalku,yalku)
    for i in range(len(numerot)):
        if numerot[i] <= 9 and numerot[i] >= 1:#tarkistetaan onko numero tarkoitus kirjoittaa(1-9)vai ei
            turt.write(numerot[i],font=("New Times Roman",20))
        if xcor < 8:#lasketaan seuraavalle numerolle uusi paikka
            xcor += 1
        elif xcor >= 8:
            ycor += 1
            xcor = 0
        turt.goto(xalku + (xcor*vali), yalku - (ycor*vali))

#paivitetaan uusinumero vanhan tilalle
def paivitys(turt,listanumero,vali):
    xcor = 0
    ycor = 0
    for i in range(listanumero):
        if xcor < 8:
            xcor += 1
        elif xcor >= 8:
            ycor += 1
            xcor = 0
    turt.goto(xalku + (xcor*vali), yalku - (ycor*vali)) #piirretaan vanhan numeron paalle valkoinen nelio
    turt.goto(turt.xcor(),turt.ycor()+30)
    turt.begin_fill()
    turt.goto(turt.xcor(),turt.ycor()-30)
    turt.goto(turt.xcor()+30,turt.ycor())
    turt.goto(turt.xcor(),turt.ycor()+30)
    turt.goto(turt.xcor()-30,turt.ycor())
    turt.end_fill()
    turt.goto(xalku + (xcor*vali), yalku - (ycor*vali))
    turt.write(ruudukkonum[listanumero],font=("Arial",15)) #piirretaan uusi numero

#tarkastetaan mahdolliset input errorit ja kysytaan taulukkoon uusi numero
def userinput():
    while True:
        try: # kysytaan kayttajalta tarvittavat tiedot seka tarkistetaan mahdolliset errorit
            testi1 = False
            testi2 = False
            x = int(input("Anna x coordinaatti mita haluasit muuttaa: "))
            y = str(input("Anna y coordinaatti mita haluasit muuttaa: "))
            if y in kirjain:
                testi1 = True
            else:
                print("y coordinaatti on kirjain valilta A-I")
            if x <10 and x >0:
                testi2 = True
            else:
                print("x coordinaatti on numero välilta 1-9")
            if testi1 == True and testi2 == True:
                vaihtonum = int(input("Mihin numeroon haluat vaihtaa: "))
                if vaihtonum <= 9 and vaihtonum >=1:
                    break
                else:
                    print("Numeron pitää olla valilla 1-9")
        except:
            print("x coordinaatti on numero valilta 1-9, y kirjain väliltä A-I ja numero väliltä 1-9")
    listanumero = (kirjain.index(y)*9) + x -1 #maaritetaan uuden numeron paikka listassa
    ruudukkonum[listanumero] = vaihtonum #muutetaan uuden numeron paikka
    paivitys(tausta, listanumero, numerovali)

def numerotarkistus(lista):
    tarkistus = set(lista)
    return len(lista) == len(tarkistus)


def oikeintarkistus(ruudukko):
    #tarkistetaan x akseli
    tarkistus = []
    rivinumero = 0
    global gameon
    for i in range(len(numrivit)):
        for c in range(9):
            t = ruudukko[(rivinumero+(9*c))]
            tarkistus.append(t)
        if numerotarkistus(tarkistus) == True:
            numrivit[i-1] = True
        else:
            numrivit[i-1] = False
        rivinumero =+ 1
        tarkistus = []
    rivinumero = 0
    #tarkistetaan y akseli
    for i in range(len(kirrivit)):
        for c in range(9):
            t = ruudukko[rivinumero]
            tarkistus.append(t)
            rivinumero = rivinumero + 1
        if numerotarkistus(tarkistus) == True:
            kirrivit[i-1] = True
        else:
            kirrivit[i-1] = False
        tarkistus = []
    rivinumero = 0
        
        
        

    if all(kirrivit) == True and all(numrivit) == True:
        print ("voitit")
        gameon = False


def taynna(ruudukko):
    valmis = 0
    for i in range(len(ruudukko)):
        if ruudukko[i] > 0 and ruudukko[i] < 10:#tarkistetaan onko numero kirjoitettu vai ei(1-9)vai ei
            valmis = valmis + 1
    if valmis == len(ruudukko):
        oikeintarkistus(ruudukko)

    


ruudukko(tausta,-200,200,9,50,450)
kirjaimet(tausta,-225,yalku,numerovali,9,kirjain)
numerot(tausta,xalku,205,numerovali,9)
ruudukkoalkupiste(tausta, alkupiste, xalku, yalku, numerovali)
while gameon == True:
    userinput()
    taynna(ruudukkonum)
