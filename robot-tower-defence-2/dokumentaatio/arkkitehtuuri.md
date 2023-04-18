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
