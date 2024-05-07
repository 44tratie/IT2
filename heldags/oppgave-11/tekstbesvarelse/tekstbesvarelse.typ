#let subject = "Informasjonsteknologi 2"
#let candidate = "Tien Tran"

#set text(size: 12pt, lang: "nb", font: "Calibri")
#set par(
  leading: 14pt,
  justify: true,
)
#show par: set block(above: 16pt)
#set math.equation(numbering: "(1)")

#set page(
  header: [
    #subject / #datetime.today().display("[day].[month].[year]")
    #h(1fr)
    #candidate
    #line(length: 100%)
  ],
  numbering: (..nums) => "Side " + nums.pos().map(str).join(" av ")
)

= Oppgave #11

== Oppgave 11a

Hvis dette er en modell for Python, er ikke `void` en gyldig type. De bør heller være ```python None```. Tallene på relasjonene er byttet om mellom bil og reservasjon. En bil skal ha 0 til 1 reservasjoner og en reservasjon skal kun tilhøre en bil. Videre er det litt rart at man kan ha maks 1 reservasjon per bil når man kan reservere forskjellige datoer. Bilklassen bør abstraheres til type bil: Fossilbil og Elbil, som kan arve felles metoder og attributter fra Bil-klassen. 

Min modell ble levert på ark i Del 1.
