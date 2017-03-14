# Komme i gang med Python

## Du lærer:
* Noen Python funksjoner
* Kommentarer og dokumentasjon i kode
* Variabler
* Tall (heltall og flyt-tall)
* Tekst i Python
* Bolske variable (sant og usant)
* None

## Oppgaver:
* Lag en Python kommentar
* Lag to variabler med tall og skriv dem ut
* Legg sammen disse tallene og skriv ut summen du får
* Gang sammen disse tallene og skriv ut tallet du får
* Spør om navnet ditt og lagre svaret i en variabel
* Skriv ut navnet ditt
* Print ut hvor mange bokstaver det er i navnet ditt


## Noen funksjoner
Python har masse kraftige innebygde funksjoner, her en noen som du trenger i denne
oppgaven og som kommer til å være kjekke å kunne.

`print()` : skriver ut ting
```python
print("Hei alle på Konnerud skole!")
```

`len()` : gir lende av objekt, fungerer på mange forskjellige objekter, for tekst gir
funksjonen antall karakterer i teksten (inkludert blanke tegn).
```python
print(len("Hei på deg"))
```

`input()` : spør etter informasjon fra brukeren av programmet ditt
```python
navnet_ditt = input("Hva heter du?")
```

`dir()` : gir en liste over funksjoner i et objekt eller modul
```python
print(dir(list))
```

## Kommentarer
Python leser en og en linje av koden din, tomme linjer ignoreres. For å lage en
kommentar begynner du med å skrive `#` tegnet. Python vil da ignorere alt
som kommer etter dette tegnet.

Kommentarer er nyttig for å forklare (dokumentere) hva programmet ditt gjør og
hvordan du har tenkt.

Eksempler:
```python
# Dette er en Python kommentar

tall = 10 # Dette er også en kommentar
```

## Variabler

For å ta vare på informasjon og bruke denne videre i programmet bruker vi variabler.

Du kan tenke på variabler er "bokser" med navn som vi har gitt et navn, vi kan putte
informasjon (data) i disse boksene, og ved hjelp av navnet på boksen få tak i
dataene igjen. 

I Python lager man variabler ved å skrive navnet (som du bestemmer selv) etterfulgt
av et "=" og verdien du vil putte i variabelen.

```python
antall_gutter = 10
antall_jenter = 11
gjennomsnittsalder = 12.6
navnet_mitt = "Grunde Løvoll"

print("Jeg heter ", navnet_mitt)
```
Hvis du putter en ny verdi inn i en variabel du har brukt før vil Python glemme den gamle verdien.
```python
gjennomsnittsalder = 10.17
```

Du kan _ikke_ bruke hvilke som helst tegn og ord som variabelnavn.
Dette er lov til:
* Å bruke bokstaver fra det engelske alfabetet, tall og understrek "_"
Dette er ikke lov til å:
* Bruke spesialtegn som #@$()? osv.
* Gi variabler navn som er det samme som reserverte ord og innebygde funksjoner i
  Python (f.eks. for, while, len, dir, open, try, osv. Dere vil lære mer om dette
  senere i kurset).

Du finner en liste over innebygde Pyrthon funksjoner her:
[https://docs.python.org/3.5/library/functions.html](https://docs.python.org/3.5/library/functions.html)
og reserverte ord her:
[https://www.programiz.com/python-programming/keyword-list](https://www.programiz.com/python-programming/keyword-list) 


## Tall og matte
Python skjønner tall og kan regne, vi skiller ofte mellom hele tall (heltall)
og tall med desimaler etter komma (komma-tall eller flyt-tall).
Vær obs. på at i Python så bruker vi "." og ikke "," i komma-tall, det la du kanskje også merke til
i eksemplene over. 

Du kan regne med +, -, * og /
```python
antall_barn = antall_gutter + antall_jenter
alder_tilsammen = antall_barn * gjennomsnittsalder
```


## Tekst
I Python skriver du tekst ved hjelp av fnutter:
```python
"dette er en Python tekst"

'dette er også en Python tekst'

# Tekst inn i en variabel
test_tekst = "Dette er en liten Test"
```
Tekst er egentlig en liste av bokstaver, og vi kan få tak i enkelt bokstaver ved å spørre
etter bokstav nummer (legg merke til at vi starter å telle med 0)
```python
forste_bokstav = test_tekst[0]
```

Python har mange innebygde funksjoner for å jobbe med tekst her er noen du kan test ut:
```python
print(len(test_tekst))
print(test_tekst.upper())
print(test_tekst.lower())
```

## Bolske varabler
For å avgjøre om ting er sant eller usant bruker vi bolske variabler (boolean på engelsk).
I Python heter disse "True" og "False". Vi lager ofte slike ved å sammenligne objekter,
eller vi har funksjoner som svarer med `True` eller `False`.
```python
10 == 11 # -> False
10 > 9   # -> True

test_tekst.startswith("Hei") # -> False
```


## Tomme variable
Python har en spesiell verdi som for ingenting, `None`.
```python
ingenting = None
```
Vi skal lære mer om dette når vi kommer til funksjoner senere i kurset.
