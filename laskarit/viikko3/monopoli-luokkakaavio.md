```mermaid
    classDiagram
        Monopoly "*" -- "1" Pelilauta
        Monopoly "*" -- "2..8" Pelaaja
        Monopoly "*" -- "2" Noppa
        Pelilauta "*" -- "40" Ruutu
        Pelaaja "*" -- "1" Pelinappula
        Pelinappula "*" -- "1" Ruutu
        class Monopoly{
        }
        class Pelilauta{
        }
        class Ruutu{
            seuraavaRuutu
        }
        class Pelinappula{
        }
        class Noppa{
            luku
        }
        class Pelaaja{
        }

```
