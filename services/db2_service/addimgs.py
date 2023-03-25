import pathlib
import sqlite3
from sqlite3 import Error

def get_db_connection(db_file):
    con = None
    try:
        con = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return con


def update_image(db, name, path):
    cur = db.cursor()
    cur.execute('update flower set image = "'+str(path)+'" where name = "'+name+'"')
    db.commit()


def main():
    database = r"C:\\Users\\Nestor\\Desktop\\Files\\3\\microservices\\serviceFinal\\service\\flowers2.db"
    db = get_db_connection(database)

    source='C:\\Users\\Nestor\\Desktop\\flowers' # folder with images (Name.jpg)
    namepaths = []
    for filepath in pathlib.Path(source).glob('**/*'):
        namepaths.append(filepath.absolute())
    for path in namepaths:
        with db:
            update_image(db, pathlib.Path(path).stem, path)

if __name__ == '__main__':
    main()