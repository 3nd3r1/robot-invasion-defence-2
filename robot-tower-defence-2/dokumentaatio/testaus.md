# Testausdokumentti

Ohjelmaa on testattu automaattisilla unittesteilla sekä manuaalisilla järjestelmätesteillä.

## Unittestit

### Robotit

Robot-luokan toimintaa on testattu _TestRobot_-luokalla. Luokka alustetaan luomalla uusi _Game_-instanssi areenalla _grass_fields_ ja luomalla yksi _minx_-robotti ja _turret_-torni.

Testit varmistavat, että robotit kuolevat ja pelaajan elämä vähenee, kun robotit pääsevät polun loppuun.

### Tornit

_Tower_-luokan toimintaa on testattu _TestTower_-luokalla. Luokka alustetaan luomalla uusi _Game_-instanssi areenalla _grass_fields_ ja luomalla yksi _minx_-robotti ja _turret_-torni.

Testit varmistavat, että tornit voidaan asettaa kentälle vain hyväksyttyihin sijainteihin. Lisäksi testataan tornien ampumista ja kohdentamista.

### Peli

Pelin eli _Game_-luokan yleistä toimintaa on testattu _TestGame_-luokalla.
Testi käyttää .env.test-tiedostoa, jotta voidaan käyttää erillistä tietokantaa testaamiseen sen sijaan, että käytettäisiin varsinaista tietokantaa.
Luokka alustetaan tyhjentämällä tietokanta, luomalla uusi _Game_-instanssi areenalla _grass_fields_, luomalla 3 eri tyyppistä robottia ja tornia, ja vähentämällä pelaajan elämäpisteitä 20:llä ja lisäämällä rahaa 50:llä.

Ensimmäinen testi varmistaa, että peli voidaan tallentaa ja tallennus voidaan ladata ilman virheitä. Lisäksi testi varmistaa, että ladattu tallennus vastaa pelin tilaa tallennuksen tekohetkellä.

Toinen testi varmistaa, että peli häviää, kun pelaajan elämäpisteet tippuvat nollaan.

### Testauskattavuus

Testien haarautuvuus ilman käyttöliittymää on 72%.

![Testikattavuus](./assets/coverage-report.png)

_main.py_-tiedosto on jätetty automaattisen testauksen ulkopuolelle, sillä se on ohjelman ns. entry point.

Pygame näyttöön liittyvä logiikka on jäänyt automaattisen testauksen ulkopuolelle. Tämän osalta voitaisiin tehdä testejä esimerkiksi manuaalisesti klikkaamalla näyttöä ja piirtämällä eri pelitilanteita. Click-moduulia voitaisiin käyttää manuaalisten klikkausten simuloimiseen pygame-näytöllä.

## Järjestelmätestaus

Järjestelmätestaus on suoritettu manuaalisesti sekä Windows- että Linux-ympäristöissä varmistaaksemme, että sovellus toimii kunnolla eri käyttöjärjestelmissä.

Kaikki [vaatimusmäärittelyssä](./vaatimusmaarittely.md) määritellyt toiminnallisuudet on testattu manuaalisesti. Lisäksi on testattu eri tilanteita ja klikkauksia, mahdollisten virheiden varalta.

## Jääneet ongelmat

Sovellus ei anna mitään virheilmoituksia käyttäjälle tuotantoympäristössä. Tämä voi aiheuttaa käyttäjälle hämmennystä, jos jokin osa sovelluksesta ei toimi oikein.
Tämä voidaan korjata lisäämällä virheilmoituksen ikkunaan, joka kertoo käyttäjälle, mikä estää pelin suorittamisen, jos jokin menee pieleen.

Lisäksi konfiguraatioita voisi parantaa. Tällä hetkellä konfiguraatiot ovat vain kahdessa kentässä .env-tiedostossa. Voitaisiin harkita muita konfiguraatiomahdollisuuksia, jotta sovellus olisi helpompi muokata ja ylläpitää.
