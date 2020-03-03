import MySQLdb

number_db = MySQLdb.connect("localhost", "asicoder", "Itupgradesnumber", "NUMBEROFDBS")
cursor = number_db.cursor()


def create_db():
    table_num = """CREATE TABLE NUMBEROFDBS (
                        NUMBER INT NOT NULL)"""
    cursor.execute(table_num)


def insertnum_db():
    cursor.execute("INSERT")


def getnum_db():
    cursor.execute("SELECT NUMBER FROM NUMBEROFDBS")
