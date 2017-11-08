# -*- coding: utf-8 -*-
#######################
## Norbert Suchojad  ##
##      ns294208	 ##
#######################

# kolko i krzyzyk

import numpy as np

class Plansza(object):
    #n-rozmiar boku planszy
    def __init__(self,n):
        #wersja slownikowa
        self.n=n
        self.plansza={}
        for i in range(self.n):
            for j in range(self.n):
                self.plansza[(i,j)]=Pole()                
        
    def __str__(self):
        return "Plansza do gry o rozmiarze "+str(self.n)

    def rysujPlansze(self):
        for i in range(self.n):
            linijka=''
            for j in range(self.n-1):
                linijka+=str(self.pole(i,j))+'|'
            linijka+=str(self.pole(i,n-1))
            print linijka
            if (i<n-1): print (self.n-1)*'-+'+'-'
            
    #zwraca obiekt klasy Pole
    def pole(self,i,j):
        return self.plansza[(i,j)]

    #wstawia podany znaw w zadane pole
    def wstawZnak(self,i,j,znak):
        if (i<0) or (i>self.n-1) or (j<0) or (i>self.n-1): return False
        return self.pole(i,j).wstawZnak(znak)
    
    #podaje znawe wygranego, None jezeli nikt nie wygraĹ�
    def wygrany(self):
        wygrane=set((self.n*'O',self.n*'X'))
        diag=''
        antydiag=''
        for i in range(self.n):
            poziomo=''
            pionowo=''
            for j in range(self.n):
                poziomo+=str(self.pole(i,j))
                pionowo+=str(self.pole(j,i))
            if set([poziomo,pionowo]).intersection(wygrane): return True
            diag+=str(self.pole(i,i))
            antydiag+=str(self.pole(i,n-1-i))
        if set([diag,antydiag]).intersection(wygrane): return True
        return False          

    def liczbaWolnychPol(self):
        wynik=0
        for i in range(self.n):
            for j in range(self.n):
                wynik+=int(self.pole(i,j).czyPusty())
        return wynik
    def liczbaZajetychPol(self):
        return self.n*self.n-self.liczbaWolnychPol()


##class Plansza(object):
##    #n-rozmiar boku planszy
##    def __init__(self,n):
##        #wersja listowa
##        self.plansza=[]
##        for i in range(n):
##            temp=[]
##            for j in range(n):
##                temp.append(Pole())
##            self.plansza.append(temp)
##    
##    def __str__(self):
##    
##    #zwraca obiekt klasy Pole
##    def pole(self,i,j):
##        return self.plansza[i][j]
##    
##    #wstawia podany znaw w zadane pole
##    def wstawZnak(self,i,j,znak):
##
##    #podaje znawe wygranego, None jezeli nikt nie wygraĹ�
##    def wygrany(self):
##    def liczbaWolnychPol(self):
##    def liczbaZajetychPol(self):




class Pole(object):
    def __init__(self):
        self.liczba=0
        
    def __str__(self):
        if self.liczba==1: return "O"
        if self.liczba==2: return "X"
        return " "

    def wstawZnak(self, znak):
        if self.liczba==0:
            if znak=="O":
                self.liczba=1
                return True
            if znak=="X":
                self.liczba=2
                return True
        return False
    
    def czyPusty(self):
        return self.liczba==0

##class Pole(object):
##    def __init__(self):
##        self.znak=" "
##
##    def __str__(self):
##        return self.znak
##
##    def wstawZnak(self, znak):
##        if self.znak==" ":
##            if (znak=="O" or znak=="X"):
##                self.znak=znak
##                return True
##        return False
##    
##    def czyPusty(self):
##        return self.znak==" "


def ruchGracza(gracz,plansza):
    #gracz='X' lub gracza='O'
    #sprawdzamy czy jest wolne pole
    if plansza.liczbaWolnychPol()<1: return False
    print 'Ruch gracza '+gracz
    while True:
        x=int(raw_input('podaj wsp pozioma (numeracja od zera)'))
        y=int(raw_input('podaj wsp pionowa (numeracja od zera)'))
        if plansza.wstawZnak(x,y,gracz): break

def ruchKomputera(plansza):
    gracz='O'

    #ofensywa
    diag=''
    antydiag=''
    for i in range(plansza.n):
        poziomo=''
        pionowo=''
        for j in range(plansza.n):
            poziomo+=str(plansza.pole(i,j))
            pionowo+=str(plansza.pole(j,i))
        if (poziomo.count('X')==0) and (poziomo.count(' ')==1):
            if plansza.wstawZnak(i,poziomo.find(' '),gracz): return
        if (pionowo.count('X')==0) and (pionowo.count(' ')==1):
            if plansza.wstawZnak(pionowo.find(' '),i,gracz): return
        diag+=str(plansza.pole(i,i))
        antydiag+=str(plansza.pole(i,n-1-i))
    if (diag.count('X')==0) and (diag.count(' ')==1):
        if plansza.wstawZnak(diag.find(' '),diag.find(' '),gracz): return
    if (antydiag.count('X')==0) and (antydiag.count(' ')==1):
        if plansza.wstawZnak(antydiag.find(' '),plansza.n-1-antydiag.find(' '),gracz): return

    #defensywa
    diag=''
    antydiag=''
    for i in range(plansza.n):
        poziomo=''
        pionowo=''
        for j in range(plansza.n):
            poziomo+=str(plansza.pole(i,j))
            pionowo+=str(plansza.pole(j,i))
        if (poziomo.count('O')==0) and (poziomo.count(' ')==1):
            if plansza.wstawZnak(i,poziomo.find(' '),gracz): return
        if (pionowo.count('O')==0) and (pionowo.count(' ')==1):
            if plansza.wstawZnak(pionowo.find(' '),i,gracz): return
        diag+=str(plansza.pole(i,i))
        antydiag+=str(plansza.pole(i,n-1-i))
    if (diag.count('O')==0) and (diag.count(' ')==1):
        if plansza.wstawZnak(diag.find(' '),diag.find(' '),gracz): return
    if (antydiag.count('O')==0) and (antydiag.count(' ')==1):
        if plansza.wstawZnak(antydiag.find(' '),plansza.n-1-antydiag.find(' '),gracz): return
    
    #sprawdz rogi
    rogi = [(0,0),(0,2),(2,0),(2,2)]
    pusteRogi = []
    zajeteRogi = []
    for rog in rogi:
		if plansza.pole(*rog).czyPusty(): pusteRogi.append(rog)
		else: zajeteRogi.append(rog)
    
    # sprawdz boki
    boki = [(0,1),(1,0),(1,2),(2,1)]
    pusteBoki = []
    zajeteBokii = []
    for bok in boki:
		if plansza.pole(*bok).czyPusty(): pusteBoki.append(bok)
		else: zajeteBokii.append(bok)
    
    # reakcja na 1 znak poza srodkiem: wstaw srodek
    if ((plansza.liczbaZajetychPol()==1) and plansza.pole(1,1).czyPusty()) :
		if plansza.wstawZnak(1,1,gracz): return
	
	# reakcja na 1 znak X w srodku: wstaw w rogi
	if (plansza.liczbaZajetychPol()==1) and not plansza.pole(1,1).czyPusty():
		losowyRog = random.choice(pusteRogi)
		if plansza.wstawZnak(losowyRog[0],losowyRog[1],gracz): return


  	
  	# wstaw w narozach
	if pusteRogi:
		losowyRog = random.choice(pusteRogi)
		if plansza.wstawZnak(losowyRog[0],losowyRog[1],gracz): return
        
    #jezeli poprzednie nie wstawily to ruch losowy
    while True:
        if plansza.wstawZnak(np.random.randint(plansza.n),np.random.randint(plansza.n),gracz): break
    
        
print 'Witaj w naszej pierwszej grze!'
n=3#int(raw_input('podaj rozmiar planszy'))
pl=Plansza(n)
gracz='X'
while True:
    pl.rysujPlansze()
    ruchGracza(gracz,pl)
    if pl.wygrany():
        pl.rysujPlansze()
        print 'GRATUALCJE!!! Gracza',gracz,'wygral'
        break
    if pl.liczbaWolnychPol()<1:
        pl.rysujPlansze()
        print 'REMIS!'
        break
    ruchKomputera(pl)
    if pl.wygrany():
        pl.rysujPlansze()
        print 'PRZEGRALES!!! ha ha ha'
        break
    if pl.liczbaWolnychPol()<1:
        pl.rysujPlansze()
        print 'REMIS!'
        break
    

