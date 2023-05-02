# Changelog

Robot Invasion Defence II-pelin changelog.

Tämä changelog on tehty [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) ohjeiden mukaisesti.

## [viikko 6](https://github.com/3nd3r1/ot-harjoitustyo/releases/tag/viikko6) - 2023-05-02

### Lisätty

-   Pelin voi voittaa ja hävitä. Molempia tilanteita kuvaa vastaava valikko.
-   Pause-valikkoon lisätty päävalikkoon paluu näppäin.

### Muutettu

-   Käyttöliittymän parannuksia:
    -   Jos torniin ei ole varaa sen hinta on punainen.
    -   Tornia ei voi valita jos siihen ei ole varaa.
-   Robottien tilastoja muutettu

### Korjattu

-   Tauko valikon teksti keskitetty.
-   Tauko valikon restart-nappi toimii

## [viikko 5](https://github.com/3nd3r1/ot-harjoitustyo/releases/tag/viikko5) - 2023-04-25

### Lisätty

-   Lisätty Menu-valikko, josta voi aloittaa pelin
-   Lisätty elämät, rahat ja kierros tiedot lisätty pelinäkymään
-   Pelin voi laittaa tauolle.

### Muutettu

-   Robottien ja tornien tilastoja muutettu.

### Korjattu

-   MissileLaucher-tornin räjähdystä suurennettu

## [viikko 4] - 2023-04-18

### Lisätty

-   Kentälle syntyy robotteja kierrosten mukaan. (Määritelty config tiedostossa)
-   Tornit voivat kääntyä ja ampua robotteja
-   Lisätty 3 eri robotti-tyyppiä: ARCHIE, NATHAN ja MINX
-   Lisätty 3 eri torni-tyyppiä: Turret, Cannon ja Missile Launcher
-   Lisätty Projectile-luokka, joka vastaa tornien ampumista ammuksista.
-   Lisätty Particle-luokka, joka vastaa eri partikkeleista

## [viikko 3] - 2023-04-04

### Lisätty

-   Käyttäjä voi asettaa yhden tyyppisen tornin kentälle
-   Lisätty Game-luokka, joka vastaa pelilogiikan koodista.
-   Lisätty Map-luokka, joka vastaa areenan luonnin koodista.
-   Lisätty Player-luokka, joka vastaa pelaajan koodista.
-   Lisätty Tower-luokka, joka vastaa tornien koodista.
-   Lisätty Robot-luokka, joka vastaa robottien koodista.
-   Lisätty Ui-luokka, joka vastaa peli-näkymän käyttöliittymästä
-   Lisätty Turret-luokka, joka on Tower-alaluokka
