# Moduler

## Du lærer:
* Å importere moduler og bruke dem i dine programmer
* Å bruke en modul for dato og tid
* Å buke denne modulen for å sammenligne tidspunkter og å regne ut hvor mange
  dager gammel du er
* Å bruke en modul for å trekke tilfeldige tall og elementer i en liste


## Oppgaver:
* Ta tiden på hvor lang tid koden din bruker med hjelp av time modulen
* Gjør en pause i koden din med `time.sleep()` funksjonen
* Bruk datetime modulen til å beregne hvor mange dager det er siden du ble født
* Finn ut hvor mange timer er det siden du ble født
* Lag en liste med ord og bruk `random` modulen til å trekke et tilfeldig element


## Moduler
For å lage mer avanserte programmer bruker vi moduler som er kode andre
allerede har skrevet. Python kommer med mange slike moduler, i tillegg finnes
det mange andre frie moduler som vi kan bruke i koden vår for å løse mere
avanserte problemer.

I Python henter vi inn moduler utenfra med kommandoen `import`
```python
import time
```

Etter å ha gjort dette har vi tilgang til funksjoner i den importerte pakken med
å bruke `.` etter den importerte modulen. 
```python
time.sleep(1) # progammet tar pause i 1 sekund
```
For å se hvilke funksjoner som finnes i en modul kan du bruke `help()`
funksjonen.
```python
> help(time)
``

Ofte så har moduler sub-moduler eller enkelt funksjoner eller objekter som vi kan
ønsker å bruke uten å skrive så mye. Da kan vi bruke kommandoen `from`.
```python
from datetime import datetime
```

Når du har laster inn `datetime` modulen kan du finne hvilket tidspunkt nå
med kommandoen:
```python
naa = datetime.now()
```
Her brukte vi funksjonen `now()` i `datetime.datetime` modulen.


## Datetime og tidspunkter
`datetime` modulen som vi importerte i koden over har flere funksjoner for å holde
orden på og regne med datoer og tidspunkter. Vi kan også finne tidsdifferanser
med å trekke `datetime` objekter fra hverandre.
```python
tid_siden = datetime.now() - datetime(2004, 1, 24)
print(tid_siden.days)
``

Du kan begynne å utforske `datetime` med
```python
> help(datetime)
```

## Trekke tilfeldige tall
Med `random` modulen kan du trekke tilfeldige tall, trekke tilfeldige elementer
fra lister dette kan du bruke til
å lage dine egne lotto-rekker, gjøre ting i tilfeldig rekkefølge, og mye mer.

For å trekke et tilfeldig heltall kan du
```python
import random
tilfeldig_tall = random.randint(0, 10) # trekker et tilfeldig tall fra 0 til 10
print(tilfeldig_tall)
print(random.randint(0, 10))
```

Modulen har også flere funksjoner for å jobbe med lister
```pytho`
liste = "hei på deg sier jeg til deg".split()

# trekke tilfeldige elementer
tilf_element = random.choice(liste)
print(tilf_element)
tilf_elementer = random.sample(list, 3) # 3 tilfeldige elementer i en ny liste
print(tilf_elementer)

# stokke om på lista
print(random.shuffle(liste))
```
