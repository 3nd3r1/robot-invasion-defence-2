# Changelog

Changelog for Robot Invasion Defence II game.

This changelog follows the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) guidelines.

## [1.1.0]() - 2023-08-25

### Added
- Added new arena Peaky Mountains

### Fixed

- Fixed waypoints so robots move more centered.

## [1.0.0](https://github.com/3nd3r1/ot-harjoitustyo/releases/tag/1.0.0) - 2023-05-13

### Added

-   Added persistent storage using a local SQLite database.
-   Added information about arenas to the game start menu.
-   Saving the game when quitting to allow resuming later.
-   Added user-specific currencies: money and experience.
-   Clicking on a tower shows its range.

### Changed

-   Increased the size of icon buttons.

### Fixed

-   Robots are drawn in level order (minx, nathan, archie).
-   Cancelling tower placement if the game is paused.

## [Week 6](https://github.com/3nd3r1/ot-harjoitustyo/releases/tag/viikko6) - 2023-05-02

### Added

-   Added winning and losing conditions, with corresponding menus.
-   Added a return to main menu button in the pause menu.

### Changed

-   UI improvements:
    -   Tower price is displayed in red if the user cannot afford it.
    -   Towers cannot be selected if the user cannot afford them.
-   Modified statistics for robots.

### Fixed

-   Centered text in the pause menu.
-   Restart button in the pause menu works.

## [Week 5](https://github.com/3nd3r1/ot-harjoitustyo/releases/tag/viikko5) - 2023-04-25

### Added

-   Added a menu where the game can be started.
-   Added displays for lives, money, and round information in the game view.
-   Added the ability to pause the game.

### Changed

-   Modified statistics for robots and towers.

### Fixed

-   Increased the explosion of the Missile Launcher tower.

## [Week 4] - 2023-04-18

### Added

-   Robots spawn on the field according to the defined configuration.
-   Towers can rotate and shoot at robots.
-   Added 3 different robot types: ARCHIE, NATHAN, and MINX.
-   Added 3 different tower types: Turret, Cannon, and Missile Launcher.
-   Added the Projectile class to handle tower projectiles.
-   Added the Particle class to handle different particles.

## [Week 3] - 2023-04-04

### Added

-   User can place one type of tower on the field.
-   Added the Game class to handle game logic.
-   Added the Map class to handle arena creation.
-   Added the Player class to handle player information.
-   Added the Tower class to handle towers.
-   Added the Robot class to handle robots.
-   Added the Ui class to handle the game view's user interface.
-   Added the Turret class as a subclass of Tower.
