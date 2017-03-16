# Funksjoner

## Du lærer:
* Å gjenbruke kode ved å lage dine egne funksjoner
* Å bruke navngitte variabler i funksjoner
* Om verdien funksjoner returnerer


## Oppgaver:
* Lag en funksjon som tar en fødselsdag (aar, maaned, dag) og returnerer antall
  dager siden de ble født
* Lag en funksjon som tar en liste med tall og ganger alle tallene med 3
  og returnerer den nye listen

## Funksjoner
Smart å slippe å skrive den samme koden igjen og igjen, for å løse dette problemet
kan vi lage funksjoner.

I Python lager man funksjoner med det reserverte ordet `def`
```python
def min_funksjon():
    print("Hei dette er min_funksjon")
```

### Retur verdier
Alle Python funksjoner returnerer en verdi, for å kontrollere hvilken verdi som returneres
bruker vi `return` kommandoen. Hvis du ikke har med `return` vil funksjonen svare
med verdien `None`.
```python
def gange_med2(tall):
    return(tall * 2)
```


### Navngi variabler
```python
def gange_med(tall, med):
    return(tall * med)

print(gange_med(med=3, tall=10))
```


### Forvalgte variabler
```python
def gange_med(tall, med=2):
    return(tall * med)

print(gange_med(tall=3))
print(gange_med(med=10)) # Denne vil gi en feil!
```
