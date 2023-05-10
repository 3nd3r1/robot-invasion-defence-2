import sqlite3
from utils.config import general


class Database:
    """Database class
        The database is stored locally. 
        The player info is stored in the player table under the player id 1
    """

    def __init__(self):
        self.__connection = sqlite3.connect(general["db_location"])
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = self.__connection.cursor()

        self.__create_database()

    def __del__(self):
        self.__cursor.close()
        self.__connection.close()

    def __create_database(self):
        """Creates the database sturcture if there is no previous one"""
        self.execute("""CREATE TABLE IF NOT EXISTS player (
                        id INTEGER PRIMARY KEY,
                        experience INTEGER,
                        coins INTEGER
                        )""")
        self.execute("""CREATE TABLE IF NOT EXISTS player_scores (
                        player_id INTEGER,
                        arena_id TEXT,
                        score INTEGER,
                        FOREIGN KEY (player_id) REFERENCES player(id)
                        )""")
        self.execute("""CREATE TABLE IF NOT EXISTS game_save (
                        id INTEGER PRIMARY KEY,
                        player_id INTEGER,
                        arena_id TEXT,
                        sprites_data TEXT,
                        player_data TEXT,
                        rounds_data TEXT,
                        FOREIGN KEY (player_id) REFERENCES player(id)
                        )""")
        self.commit()
        self.create_save()

    def execute(self, query, params=()):
        return self.__cursor.execute(query, params)

    def commit(self):
        self.__connection.commit()

    def create_save(self):
        """ Create a new save if there is no previous one"""
        if self.execute("SELECT EXISTS(SELECT 1 FROM player)").fetchone()[0]:
            return
        self.execute("INSERT INTO player (id, experience, coins) VALUES (?, ?, ?)",
                     (1, 0, 0))
        self.commit()


database = Database()


def reset_save():
    database.execute("DELETE player")
    database.execute("DELETE player_scores")
    database.execute("DELETE game_save")
    database.create_save()


def save_game(arena, sprites, player, rounds):
    database.execute("""INSERT INTO game_save (player_id, arena_id, sprites_data,
                        player_data, rounds_data) VALUES (?,?,?,?,?)""",
                     (1, arena, sprites, player, rounds))
    database.commit()


def get_game_save(save_id):
    return database.execute("""SELECT * FROM game_save WHERE id=?""", (save_id,)).fetchone()


def get_game_saves():
    saves = database.execute("""SELECT arena_id, id FROM game_save WHERE player_id=?""",
                             (1,)).fetchall()
    return {save[0]: save[1] for save in saves}


def get_player_info():
    return database.execute("SELECT * FROM player WHERE id=?", (1,)).fetchone()


def get_player_scores():
    """Get players highscore for each arena"""
    scores = database.execute("""SELECT arena_id, IFNULL(MAX(score), 0) FROM player_scores
                            WHERE player_id=? GROUP BY arena_id""", (1,)).fetchall()
    return {score[0]: score[1] for score in scores}


def add_player_experience(experience):
    database.execute("UPDATE player SET experience=experience+? WHERE id = ?",
                     (experience, 1))
    database.commit()


def add_player_score(arena, score):
    database.execute("""INSERT INTO player_scores (player_id, arena_id, score)
                    VALUES (?, ?, ?)""", (1, arena, score))
    database.commit()
