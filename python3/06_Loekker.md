# Løkker

## Du lærer:
* Å bruke `while` løkker
* Å bruke `for` løkker
* Å bruke generatorer for til å lage lister


## Oppgaver:
* Lag en while løkke hvor du skriver ut navnet ditt 23 ganger
* Lag en while løkke hvor spør etter navn til brukeren skriver stopp og legger disse navnene til en liste
* Lag en for løkke for å skrive ut alle navnene du har samlet inn
* Bruk en generator til å lage en liste med tall fra 0 til 50


## Løkker
I oppgavene du har gjort til nå har du kanskje ofte skrevet
mange kodelinjer etter hverandre som gjør nesten det samme?
Dette føles kanskje litt dumt ut? Eller i alle fall lit tungvint
ut...

Eller du har kanskje trengt å gjøre en ting med alle elementene
i en liste?

Til dette trenger vi _løkker_!


### while
Den enkleste løkka i er while-løkka. Ei while løkke kjører den
samme kodeblokka i gjen og igjen så lenge valget i løkka er sant.
```python
i = 0
while i < 10:
    print(i)
    i += 1 # legger 1 til i for hver gang løkka kjøres
```

### for
Den kraftigste og mest brukte formen for løkke i Python er for-løkka.
For løkken kjører koden i løkka for alle elementene i ei list. 
```python
liste = "hei hå heter du Ola?".split()
for ord in liste:
    print(ord)
```


### Listegeneratorer
I Python er det også vanlig å bruke løkker for å lage lister
syntaksen for dette er slik:
```python
liste = [i for i in range(6)] # lager listen [0, 1, 2, 3, 4, 5]
liste01 = [i for i in liste]  # en kopi av liste
liste02 = [i * 3 for i in liste] # som liste, men alle elementene er ganget med 3
```
