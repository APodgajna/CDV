print("cdv")
print(2)
'''
komentarz blokowy
'''
#potęgowanie
potega = 2 ** 10
print(potega)
#pobieranie danych z klawiatury
print("Podaj imie")
imie =  input()
#konkatenacja +
print("Twoje imię podane z klawiatury:" + imie)


nazwisko = input("Podaj nazwisko:")
print("Twoje nazwisko podane z klawiatury:" + nazwisko)

#twoje imie:... twoje nazwisko:....
print("Twoje imie: " + imie + ", Twoje nazwisko: " + nazwisko)

'''
uzytkownik podaje wiek z klawiatury,
wyswietl dane w formacie: Twoj wiek: ... lat
'''

print("Podaj swoj wiek",end="")
wiek = input()
print(type(wiek)) #str
print("Twoj wiek: ", wiek, " lat")

wiek1 = 21
print(type(wiek1)) #int
print("Twoj wiek: ", wiek1, " lat")

nazwisko = "Kowalski"
pierwszyZnak = nazwisko[0]
print(pierwszyZnak)


dlugosc = len(nazwisko)
print(dlugosc)

ostatniZnak = nazwisko[len(nazwisko) - 1]
print(ostatniZnak)

ostatniZnak = nazwisko[-1]
print(ostatniZnak)

#konwersja
x = "5"
print(type(x))
x = int(x)
print(type(x))

print()
