# Changelog

Robot Invasion Defence II-pelin changelog.

Tämä changelog on tehty [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) ohjeiden mukaisesti.

## [viikko 5] - 2023-04-25

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
