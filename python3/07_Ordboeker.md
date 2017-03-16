# Ordbøker

## Du lærer:
* Å lage og bruke "ordbøker"
* Å lage ordbøker fra lister med `zip()` funksjonen
* Å lage løkker som bruker ordbøker

## Oppgaver:
* Lag en "ordbok" med ditt fornavn, etternavn, og fødselsdag
* Lag en venne-liste med ordbøker. Hvor hver ordbok er som
  den du laget for deg selv, men for noen venner i tillegg til din ordbok.
* Lag en løkke hvor du skriver ut informasjon om alle vennene i lista


## Ordbøker
Ordbøker (i Python heter de dictionaries) er er som lister en data struktur
man bruker veldig _mye_ når man koder i Python.
Ordbøker ligner på lister, det er en slags boks som man kan putte alle mulige
ting inn i sammen med en nøkkel for å få tak i tingen igjen. Vanligvis er nøkkelen
en tekst, men det kan være en hvilken som helst "uforanderlig" data type.

Ordbøker lages med `{}` eller `dict()` funksjonen.
```python
ordbok = {'navn': 'Ola Nordmann', 'alder': 42}
```
Her er 'navn' og 'alder' nøkler i ordboka, mens 'Ola Nordmann' og 42 er verdiene
som hører til nøklene.
```python
ordbok = dict([('navn', 'Ola Nordmann'), ('alder', 42)])
```
gir akkurat det samme som om vi hadde brukt `{}` (du kommer til å få bruk for denne
varianten når vi skal lære om `zip()` funksjonen).

For å få tak i et element i en ordbok indekserer vi med nøkkelen du har
gitt elementet.
```python
print(ordbok['navn'])
```
Hvis du prøver å hente et element som ikke finnes i ordboken vil Python gi en
feil, prøv:
```python
print(ordbok['ettenavn'])
```
For hvis du ikke er sikker på at elementet du spør etter finnes i ordboken
men ikke vil få en feil hvis det ikke finnes bør du bruke `ordbok.get()`
funksjonen:
```python
print(ordbok.get('etternavn'))
print(ordbok.get('fornavn', 'finner ikke fornavn')
```
`ordbok.get()` funksjonen gir `None` hvis elementet ikke finnes eller
verdien du ba om å få.

For å legge til et element eller bytte ut et element som finnes i
ordboka bruker du indeks og `=`
```python
ordbok['by'] = 'Andeby'
ordbok['navn'] = 'Skrue McDuck'

print(ordbok['navn'], 'bor i', ordbok['by'])
```

For å slette elementer i ordbøker bruker vi `del` kommandoen
```python
del ordbok['by']
print(ordbok)
```

### Finne ut hva som er i ordboka
Orbøker har tre veldig nyttige funksjoner for å få tak i
det som er lagret i den:
* **`ordbok.keys()`** som gir en liste med alle nøklene i ordboka
```python
> ordbok.keys()
=> dict_keys(['alder', 'navn'])
```

* **`ordbok.values()`** som gir en liste med alle elementene i ordboka
```python
> ordbok.values()
=> dict_values([42, 'Skrue McDuck'])
```

* **`ordbok.items()`** som gir en liste av alle nøkkel - element par
```python
> ordbok.items()
=> dict_items([('alder', 42), ('navn', 'Skrue McDuck')])
```

Det er verdt å merke seg at det ikke er garantert at du får nøklene og
elementene i samme rekkefølge som du puttet dem inn!

### Løkker med ordbøker
Hvis vi bruker funksjonene over kan vi også lage for-løkker med ordbøker,
da kan du f.eks. gjøre det det samme med alle nøklene og elementene i ordboka.
```python
ordbok['fornavn'] = 'Skrue'
ordbok['etternavn'] = 'McDuck'
for noekkel, element in ordbok.items():
    print(noekkel, element)
```

### Ordbok og zip
Python har en innebygd glidelås-funksjon som heter `zip()`,
denne slår sammen to lister til en liste av tupler.
```python
noekler = ['fornavn', 'etternavn', 'by']
info = ['Donald', 'Duck', 'Andeby']

print(zip(noekler, info))
```

Dette kan vi nå bruke til å lage en ordbok av to lister, hvor den ene lista
er nøklene i ordboka og den andre er elementene.
```python
donald_ordb = dict(zip(noekler, info))

print(donald_ordb)
```
