# Lister

## Du lærer:
* Å lage lister
* Å legge til og slette elementer i lister
* Å få tak i enkelt elementer og deler av lister
* Å bruke noen Python funksjoner for lister
* Forskjellen på lister og "tupler"

## Oppgaver:
* Lag en tom liste
* Lag en liste med navnet på noen som går i klassen din
* Skriv ut listen
* Legg til et navn med å bruke `input()` og `liste.append()`
* Skriv ut første og de to siste navnet i lista
* Skriv ut lista baklengs

## Lister
Når vi koder bruker vi data-typer og strukturer som finnes i språket, en av
dem vi bruker aller mest er lister. Lister er en ordnet samling av objekter,
et objekt i lista kaller vi et _element_.
En liste kan inneholde alle mulige typer objekter, og alle elementene i
lista trenger _ikke_ å være av samme type.


### Lage lister
Man lager lister ved å skrive elementer inni `[]` med komma i mellom.
```python
en_liste = [1, 3, "test"]
```
Eller ved å bruke `list()` funksjonen
```python
en_annen_liste = list(2, 2, True, None, "tull")
```
Vi kan også lage tomme lister
```python
lst = []  # lst er nå en tom liste
```
For å lage en liste med heltall kan vi bruke `list()` og
`range()` funksjonene sammen
```python
lst = list(range(10)) # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Vi kan også lage lister fra tekst med å bruke `split()`
funksjonen.
```python
en_liste_til = "det er gøy med koding altså".split()
```

### Legge til og slette elementer
For å legge til elementer på slutten av ei liste kan vi bruke
`lst.append(elm)` funksjonen og for å slette kan vi bruke
`lst.remove(elm)`, hvor `lst` er lista (variabelen altså) og
`elm` er elementet vi vil legge til eller fjerne.
```python
lst.append("hei")
lst.append("futt og fart")
print(lst)
lst.remove("hei")
print(lst)
```
Vi kan også legge sammen lister med `+`
```python
lst = lst + en_liste + en_liste_til
print(lst)
```


### Indekser
For å få tak i et spesielt element i lista bruker vi nummeret til
elementets plass i lista i `[]`
```python
print(en_liste[2]) # printer ut 3de element i lista
```
legg merke til at vi i Python begynner å telle med 0 (du husker kanskje
også dette fra en tidligere oppgave?).

Vi kan også bruke indekser til å hente ut deler eller utvalg av lister
ved å indeksere slik: `[start:slutt]` da får man listen far start til
elementer _før_ slutt:
```python
# prøv dette
print(lst[2:5])
print(lst[4:])
print(lst[:4])
```
Hva skjer når du utelater `start` eller `slutt` indeksen?


## Innebygde funksjoner for lister
Python har mange funksjoner for å jobbe med lister.
Her er noen eksempler som dere kan eksperimentere med.
```python
lst_sortert = sorted(lst) # sorterer listen i stigende rekkefølge
print(lst_sortert)

lst_baklengs = reversed(lst) # snur rekkefølgen på elementene
print(lst_baklengs)

siste_elem = lst.pop() # gir siste element i lista og sletter det fra lista
print(siste_elem)

i = lst.index("futt og fart") # gir index til elemented "futt og fart"
```


## Python tuple
I Python har lister en fetter som vi kaller for `tuple`, tupler lager du mer `()`
og komma istedenfor `[]` og komma.
```python
ett_tuple = (1, 2, "hei", 14)
```

Tupler er veldig lik lister, men det er en viktig forskjell, tupler kan _ikke_
endres når de først er laget.


## Komme videre
Kidsa koder har også en
[oppgave med lister](http://oppgaver.kidsakoder.no/python/lister_og_indekser/lister_og_indekser.html)
