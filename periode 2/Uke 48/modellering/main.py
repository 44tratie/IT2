from modeller.artist import Artist
from modeller.eier import Eier

# Oppsett av albumbibliotek
supermerk2 = Artist("Supermerk2")
supermerk2.registrer_cd("La Lata", "Magenta", 2003)

abba = Artist("ABBA")
abba.registrer_vinyl("Arrival", "Polar", 1976, 33, "Sort")
abba.registrer_cd("The Visitors", "Polar", 1981)

# Innlegging av album i platesamling
Ola = Eier("Ola Nordmann")
Ola.platesamling.legg_til_album(supermerk2.hent_album("La Lata"))
Ola.platesamling.legg_til_artist(abba)
