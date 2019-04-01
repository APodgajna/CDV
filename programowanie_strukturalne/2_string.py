tekst = "Anna, pawel, JulIA"
lista = tekst.split(", ")
print(tekst)
print(lista)
print(type(lista))

imie1 = lista[0]
print(imie1) #Anna


imieDuze = imie1.upper()
print(imieDuze) #ANNA


imieMale = imie1.lower()
print(imieMale) #anna

#spradzenie zawartosci
print("\nPodaj swoje nazwisko: ", end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc) #true or false

nazwisko = ""
print(nazwisko.isalpha()) #false

text1 = "\nJulia\n"
text2 = "Nowak"
print(text1 + text2)

text1 = text1.rstrip()
print(text1 + text2)
print(text1 + " " + text2)
#wyswietlenie lanchucha znakow
#wszystkie wersje pythona
text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowsze wersje pythona >2.6
text = "{1}, Java i {0}".format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisanie danych
rok = 2019
miesiac = "kwiecien"
dzien = 1

print("\nData: ", end="")
print(dzien, miesiac, rok)

print("\nData: ", end="")
print(dzien, miesiac, rok, sep="-")


