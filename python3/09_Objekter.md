# Objektorientert programmering

## Du lærer:
* Å lage dine egne objekter
* Å lage metoder som bruker data i objektene dine


## Oppgaver:
* Lag et Person-objekt med `etternavn`, `fornavn`, og `fødselsdag`.
* Lag en metode for Person objekter som beregner antall dager siden personen ble født.


## Objekter og klasser
Litt om Python objekter og klasser

### `class`
```python
class MinKlasse(object):
    pass
```
En helt tom klasse


### `__init__`
Fylle objekter med innhold
```python
class Bok(object):
    def __init__(self, tittel, forfatter):
        self.tittel = tittel
        self.forfatter = forfatter

emil = Bok(tittel="Emil i Lønneberget", forfatter="Astrid Lindgren")


### Instansmetoder
```python
pass
```
### Spesialmetoder
`__repr__()` etc.
