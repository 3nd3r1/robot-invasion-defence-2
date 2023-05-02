# Arkkitehtuurikuvaus

## Rakenne

### Pelin rakennetta kuvaana pakkausrakenne

![Pakkauskaavio](/dokumentaatio/pakkauskaavio.png)

_ui_ sisältää käyttöliittymä koodia
_game_ sisältää pelin koodia
_towers_ sisältää eri tyyppisten tornien koodia
_robots_ sisältää eri typpisten robottien koodia

### Pelin rakennetta kuvaava luokka-diagrammi:

```mermaid
classDiagram
    Game ..> Util
    Game "*" -- "1" Map
    Game "*" -- "1" Ui
    Game "*" -- "1" RoundManager
    Game "*" -- "1" Player
    Game "*" -- "*" Sprite
    Sprite <-- Tower
    Sprite <-- Robot
    Sprite <-- Projectile
    Sprite <-- Particle
    Tower <-- Turret
    Tower <-- Cannon
    Tower <-- MissileLauncher
    Robot <-- Minx
    Robot <-- Nathan
    Robot <-- Archie
    Projectile <-- TurretProjectile
    Projectile <-- CannonProjectile
    Projectile <-- MissileLauncherProjectile
    Particle <-- MissileLauncherParticle
    Ui "*" -- "1" Sidebar
    class Util {
    }
    class Game {
    }
    class Player {
        int money
        int health

    }
    class Map {
    }
    class Sprite {
    }
    class Tower {
        int health
        int damage
        int shoot_interval
        Robot target

    }
    class Robot {
        int health
        int speed
        int bounty

    }
    class Projectile {
        Robot target
        Tower tower
    }
    class Particle {

    }
    class Ui {
    }
    class Sidebar {
    }
    class RoundManager {
        int round
    }
```

## Päätoiminnallisuudet

### Tornin asettaminen kentälle

Kun pelaaja valitsee käyttöliittymästä uuden tornin ja klikkaa pelikenttää, sovellus etenee seuraavasti:

```mermaid
sequenceDiagram
    actor User
    participant Game
    participant GameUi
    participant __new_tower
    participant Player
    participant Map

    User ->> Game: click on the "Turret"-tower on the sidebar
    Game ->> GameUi: on_click(pos)
    GameUi ->> Game: get_state()
    Game -->> GameUi: "game"
    GameUi ->>+ Game: create_tower("turret")
    Game ->> __new_tower: Turret(self)
    Game -->>- GameUi: __new_tower

    User ->> Game: click somewhere on the map
    Game ->> Player: get_money()
    Player -->> Game: 300
    Game ->>  __new_tower: get_cost()
    __new_tower -->> Game: 250
    Game ->>+ __new_tower: place(pos)
    __new_tower ->> Game: get_towers()
    Game -->> __new_tower: []
    __new_tower ->> Game: get_map()
    Game -->> __new_tower: Map
    __new_tower ->> Map: is_in_obstacle(hitbox)
    Map -->> __new_tower: False
    __new_tower ->> Map: is_in_path(hitbox)
    Map -->> __new_tower: False
    __new_tower ->> Map: is_in_water(hitbox)
    Map -->> __new_tower: False
    __new_tower ->> Map: is_in_map(hitbox)
    Map -->> __new_tower: False
    __new_tower -->>- Game: True
    Game ->> Player: spend_money(cost)
    Player -->> Game: None

```

Ensimmäisessä vaiheessa käyttäjä klikkaa pelin sivupalkissa olevaa "Turret"-tornia, jolloin tapahtumaketju käynnistyy. Käyttäjän klikkaus välittyy pelille, joka välittää sen edelleen pelin käyttöliittymälle. Käyttöliittymä pyytää peliltä sen tilan, jonka jälkeen peli luo uuden tornin käyttöliittymän pyynnöstä.

Toisessa vaiheessa käyttäjä klikkaa kartalla paikkaa, johon uusi torni halutaan sijoittaa. Pelin täytyy tarkistaa, onko pelaajalla tarpeeksi rahaa tornin ostamiseen. Pelaaja antaa pelille tiedon saatavilla olevasta rahasummasta. Pelin täytyy myös selvittää, mikä on uuden tornin hinta. Tämän jälkeen peli pyytää uutta tornia sijoittumaan haluttuun paikkaan. Ennen kuin torni sijoitetaan, pelin täytyy varmistaa, että paikka on sallittu, eli että se ei ole esteen tai polun päällä tai vedessä. Kartta vastaa näihin kyselyihin, ja kun kaikki tarkistukset on tehty, torni sijoitetaan kartalle. Peli veloittaa pelaajalta tornin hinnan.

## Ohjelman heikkoudet

### Käyttöliittymä

Staattiset Menu-luokat eivät ole mieleiset. Ne saisi toteuttaa yhdessä tiedostossa.
