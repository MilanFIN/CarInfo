TODO
- custom komennot, esim 0146 pitäisi olla ambient temp
	- rakenne MODE + wikisivun eka sarake
	- https://en.wikipedia.org/wiki/OBD-II_PIDs#Standard_PIDs
	- komentoja, voisi tarkastaa käsin
		- 01A4, vaihde, vaihtuuko tämä vaihteen kanssa?
		- 0146, ulkolämpötila
		- 015E, 019D, , fuel rate





# main.py tiedosto
- luo mapin, jossa on tallessa viewit id:llä
- luo screenin
- luo obd objektin, mahdolliseti debug arvolla
- kutsuu aktiivisen viewin funktioita, ja tarvittaessa
  vaihtaa aktiivista viewiä
- vain aktiivista päivitetään, muut idlaa

# obd-yhteys objekti
- ottaa async yhteyden
- debug parametri käskee että ei tehdä yhteyttä
  vaan käytetään mock arvoja
- subscribe ("command")
	- laittaa kuuntelemaan
- status ("command")
	- palauttaa arvon
- oletettu koko 800x480

# view kantaluokka
- saa yhteys objectin, ja ilmoittaa mitä tarvitsee
- render
- update (päivittää datan)
	- voi palauttaa view id:n, jos tehdään siirtymää
- click (koordinaatit)
	- voi palauttaa view id:n, jos tehdään siirtymää

# view periytetty luokka
- toteuttaa viewin palikoilla

# palikka
- koko
- sijainti
- update (data)
	- vain yksi value per palikka?