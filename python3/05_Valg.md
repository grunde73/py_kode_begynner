# Valg

## Du lærer:
* Å bestemme hva du skal gjøre med if, elif og else
* Hvordan man lager kodeblokker med "innrykk" i Python
* Tomme kodeblokker i Python


## Oppgaver:
* Lag et program som spør om alder
* Skriv ut alderen
* Skriv en beskjed hvis de er under 12 år, og en annen beskjed hvis de er eldre


## Valg
For å velge hva programmet skal gjøre kan vi bruke if-setninger, det er veldig
nyttig hvis vi f.eks. ønsker å kjøre ulik kode med forskjellige data
fra de som bruker programmet.

## Enkle valg med if
```python
alder = int(input("Hvor gammel er du?"))
if alder > 18:
    print("Du er", alder, "år, og er voksen")
```
Denne koden kan deles opp i tre deler.

`if` forteller datamaskinen at nå kommer det en if-setning
`alder > 18` tester om alder-variabelen er større enn 18
`:` betyr at vi er ferdig med testen vår, og nå kommer koden som skal kjøres hvis testen er sann.
Innrykket før print sørger for at Python vet at det er denne koden som skal kjøres hvis
if-setningen er sann.


## if, elif og else
For å ha flere valg en bare med `if` bruker vi `if`, `elif` og `else`.
Syntaksen for dette er slik:
```python
valg = int(input("gi et heltall"))

if valg > 10:
    print("valg > 10")
elif valg < 3:
    print("valg < 3")
else:
    print("3 >= valg <= 10")
```
Det er lov til å droppe `elif` og `else` etter `if` og du
kan ha så mange `elif` valg du bare vil i koden din.

## Kodeblokker og innrykk
I kode eksempelet over la du kanskje merke til at koden etter `if` hadde innrykk?
Dette er en veldig viktig detalj fordi Python bruker innrykk for å bestemme
hva som hører til `if` valget. Dette kaller vi en _kodeblokk_ og Python bruker
innrykk for alle typer kodeblokker, så dette vil du også se når vi kommer
til _løkker_, _funksjoner_ og _objekter_ senere i kurset.

Det er vanlig å bruke 4 blanke tegn (space) som innrykk når vi
skriver kode, repl.it bruker 2. Det som er viktig er at innrykket
må være _det samme_ for alle linjene i en kodeblokk. Og det er
lurt å bruke samme type innrykk i alle kodeblokker i en fil.

## Tomme linjer i Python
Vanligvis vil Python ganske enkelt ignorere tomme eller blanke
kodelinjer. Men det finnes tilfeller hvor dette ikke er lov, det
er f.eks. ikke lov med en tom kodeblokk etter `if`.
Så hvis du skal gjøre ingenting i en kodeblokk må du bruke
det reserverte ordet `pass`.
```python
if valg != 2:
    pass # vi gjør ingenting
else:
    print("valg var ikke 2 men", valg)
``

## Lære mer?
[If hos Kidsa koder](http://oppgaver.kidsakoder.no/python/if-setninger/if-setninger.html)
