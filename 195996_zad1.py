# -*- coding: utf-8 -
import random
ZAKRES=6
def utworz_haslo():
	"""Funkcja tworzy hasło"""
	kolory = [x for x in range(1,ZAKRES)]
	haslo = (random.choice(kolory), random.choice(kolory),random.choice(kolory),random.choice(kolory))
	return haslo

def pobierz_liczby():
	"""Funkcja pobiera liczby od gracza"""
	dane = list()
	ilosc = 0
	while(len(dane)<4):
		try:
			liczba = int(raw_input('Podaj liczbe: '))
			if liczba >= ZAKRES:
				print("Zakres liczb (1-6)")
			else:
				dane.append(liczba)
		except ValueError:
			print("Niepoprawna liczba!")
	return dane

def sprawdz_haslo(haslo, gracz):
	"""Funkcja sprawdza poprawność wprowadzonego przez gracza hasła"""
	czarne = 0
	biale = 0
	for k,l in zip(haslo, gracz):
		if(k==l):
			czarne += 1
		elif(l in haslo):
			biale += 1
	return czarne, biale

def main():
	haslo = utworz_haslo()
	print haslo
	koniec = 1
	proby = 1
	while(koniec and proby<=10):
		print '#{0} Próba'.format(proby)
		gracz = pobierz_liczby()
		czarne, biale = sprawdz_haslo(haslo, gracz)
		print 'Czarne: {0}, Białe: {1}'.format(czarne, biale)
		if(czarne == 4):
			print "WYGRAŁEŚ!"
			koniec = 0
		proby += 1

if __name__ == "__main__":
    main()
