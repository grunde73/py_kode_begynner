# Moduler

## Du lærer:
* Å importere moduler og bruke dem i dine programmer
* Å bruke en modul for dato og tid
* Å buke denne modulen for å sammenligne tidspunkter og å regne ut hvor mange
  dager gammel du er


## Oppgaver:
* Ta tiden på hvor lang tid koden din bruker med hjelp av time modulen
* Gjør en pause i koden din med `time.sleep()` funksjonen
* Bruk datetime modulen til å beregne hvor mange dager det er siden du ble født
* Finn ut hvor mange timer er det siden du ble født


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
orden på og regne med datoer og tidspunkter.


JOBBER HER
## Ekstra utfordring
* Å bruke en modul for å lese nettsider
* Bruke en modul for å hente tekst ut av nettsiden du har lest
