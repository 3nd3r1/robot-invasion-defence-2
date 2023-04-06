# Robot Invasion Defence 2 - Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on klassinen Tower Defence peli, jossa asettamalla torneja kentälle pelaaja yrittää suojautua robottien hyökkäykseltä.

Sovelluksessa on monta tornia, joita pelaaja voi käyttää pelin pelaamiseen. Esimerkiksi: tykki, liekinheitin jne.

Sovelluksessa on eri robotti tyyppejä eli robotteja joilta pelaaja yrittää suojautua.

Sovelluksessa on monta areenaa eli pelikenttää, joissa robottien polku on eri. Areenoilla voi olla myös muita eroja, jotka vaikuttavat pelattavuuteen.

## Käyttöliittymäluonnos

![Käyttöliittymäluonnos](/robot-tower-defence-2/dokumentaatio/kayttoliittymaluonnos.png)

## Perusversion toiminnallisuus

### Tietojen tallennus

-   Käyttäjän tiedot tallennetaan lokaalisti tiedostoon tietokoneella
    -   Tämä tiedosto sisältää käyttäjän nimen, tason ja valuutat.
    -   Jos tiedostoa ei löydy, sovellus kysyy käyttäjältä nimen ja luo tiedoston.

### Menu

-   Menu näkymässä näkyy käyttäjän perustiedot (nimi, valuutat ja taso)
-   Menu näkymästä pääsee asetuksiin
    -   Asetuksissa voi vaihtaa äänenvoimakkuutta.
    -   Asetuksissa voi poistaa tallennus tiedoston.
-   Menu näkymästä voi valita tason jossa aloittaa pelin.

### Peli

-   Käyttäjällä on peli kohtaiset elämät (HP)
    -   Elämät näkyvät näkymässä
    -   Elämät vähenevät robottien päästessä läpi.
-   Käyttäjällä on peli kohtainen valuutta (rahaa)
    -   Valuutta näkyy näkymässä
    -   Valuutta kasvaa tuhotessa robotteja
-   Käyttäjä voi laittaa pelin tauolle
    -   Tauko näkymässä pelin voi lopettaa
-   Käyttäjä voi voittaa ja hävitä pelin
    -   Käyttäjä häviää, kun elämät tippuvat nollaan
    -   Käyttäjä voittaa, kun pääsee tasolle 100
-   Käyttäjä voi asettaa torneja (tehty)
    -   Tornit toimivat
-   Käyttäjä voi poistaa/myydä torneja

## Jatkokehitysideoita

Perusversioita täydennetään seuraavilla toiminnallisuuksilla

-   Lisää eri torneja:
    -   Liekinheitin
    -   Tykki
-   Lisää eri areenoita
-   Lisää eri robotteja
-   Torneille voi ostaa eri asuja (skin)
-   Käyttäjän tallentaminen pilveen.
-   Kauppa-sivu
-   Pikakelaus nappi peleihin
