import MySQLdb


def create_db():
    leaderboards_db = MySQLdb.connect("localhost", "asicoder", "ItupgradesaocDB", "LEADERBOARD{}".format())
    cursor = leaderboards_db.cursor()
    cursor.execute("DROP TABLE IF EXISTS LEADERBOARD")

    table_leaderboards = """CREATE TABLE LEADERBOARD (
                            NAME_OF_CONTESTANT CHAR(100) NOT NULL,
                            POINTS INT NOT NULL,
                            STARS INT NOT NULL)"""
    cursor.execute(table_leaderboards)



#def insert_new_leaderboard():


#def update_db():


#def erase_contestant():

