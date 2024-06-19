# Eksamen | IT2 (REA3049) | Vår 2024

## Installasjon

Denne besvarelsen krever [Python 3.12](https://www.python.org/downloads/release/python-3120). (Dette er blant annet for oppdatert type hinting)

Denne besvarelsen krever pakkene under `requirements.txt`.

Du kan installere pakkene ved hjelp av:

```sh
pip install -r requirements.txt
```

## Kjøring av kode

Alle "entry points" for oppgavene er i main.py.

For å kjøre denne koden fra terminalen kan du bruke:

```sh
cd oppgave-data
python3 main.py
```

## Kommentarer til oppgaver


### Oppgave 9

Datasettet inneholdt hoved og underkategorier av aktiviteter. For eksempel hovedkategorien "Inntektsgivende arbeid, arbeidsreiser mv." har underkategorien "Inntektsgivende arbeid". Når oppgaven ba om ulike aktiviteter, har jeg tolket dette som underkategorier.

### Oppgave 10

Jeg har valgt å ikke inkludere "private" (altså metoder med _) i klassediagrammet siden disse metodene er kun ment til å abstrahere koden i klassen. De skal altså ikke kalles i noen andre filsteder. Jeg sier "privat" fordi medlemsvariabler i Python ikke er ordentlig private :p.