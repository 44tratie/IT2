def shift(tekst: str, n: int) -> str:
  """Krypterer en streng ved å skifte deres unicode kode med n

  Parameters
  ----------
  tekst : str
      Teksten som skal krypteres
  n : int
      Antall "steg" som skal tas

  Returns
  -------
  str
      Den krypterte teksten
  """  
  nytekst = ""

  for bokstav in tekst:
    tallkode = ord(bokstav)
    tallkode += n
    nytekst += chr(tallkode)

  return nytekst

def shift_baklengs(tekst: str, n: int) -> str:
  """Krypterer en streng ved å skifte deres unicode kode med -n

  Parameters
  ----------
  tekst : str
      Teksten som skal krypteres
  n : int
      Antall "steg" som skal tas bakover

  Returns
  -------
  str
      Den krypterte teksten
  """  
  nytekst = ""

  for bokstav in tekst:
    tallkode = ord(bokstav)
    tallkode -= n
    nytekst += chr(tallkode)

  return nytekst