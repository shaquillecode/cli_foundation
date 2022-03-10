"""Simple Music Database"""
import sqlite3

def create_database(NEW_DB):
    """Creating the Database"""
    conn = sqlite3.connect(NEW_DB)
    cursor = conn.cursor()

    # create a table
    cursor.execute("""CREATE TABLE albums
                          (title text, artist text, release_date text,
                           publisher text, media_type text)
                       """)
    # insert some data
    cursor.execute("INSERT INTO albums VALUES "
                   "('Glow', 'Andy Hunter', '7/24/2012',"
                   "'Xplore Records', 'MP3')")

    # save data to DATABASE
    conn.commit()

    # insert multiple records using the more secure "?" method
    albums = [('Exodus', 'Andy Hunter', '7/9/2002',
               'Sparrow Records', 'CD'),
              ('Until We Have Faces', 'Red', '2/1/2011',
               'Essential Records', 'CD'),
              ('The End is Where We Begin', 'Thousand Foot Krutch',
               '4/17/2012', 'TFKmusic', 'CD'),
              ('The Good Life', 'Trip Lee', '4/10/2012',
               'Reach Records', 'CD')]
    cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)",
                       albums)
    conn.commit()

def delete_artist(NEW_DB, artist):
    """
    Delete an artist from the Database
    """
    conn = sqlite3.connect(NEW_DB)
    cursor = conn.cursor()

    sql = """
    DELETE FROM albums
    WHERE artist = ?
    """
    cursor.execute(sql, [(artist)])
    conn.commit()
    cursor.close()
    conn.close()


def update_artist(NEW_DB, artist, new_name):
    """
    Update the artist name
    """
    conn = sqlite3.connect(NEW_DB)
    cursor = conn.cursor()

    sql = """
    UPDATE albums
    SET artist = ?
    WHERE artist = ?
    """
    cursor.execute(sql, (new_name, artist))
    conn.commit()
    cursor.close()
    conn.close()


def select_all_albums(NEW_DB, artist):
    """
    Query the database for all the albums by a particular artist
    """
    conn = sqlite3.connect(NEW_DB)
    cursor = conn.cursor()

    sql = "SELECT * FROM albums WHERE artist=?"
    cursor.execute(sql, [(artist)])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


if __name__ == '__main__':
    import os
    NEW_DB = "music_database.db"
    if not os.path.exists(NEW_DB):
        create_database(NEW_DB)

    delete_artist(NEW_DB, 'Andy Hunter')
    update_artist(NEW_DB, 'Red', 'Redder')

    print(select_all_albums(NEW_DB,'Redder'))
    print(select_all_albums(NEW_DB,'Thousand Foot Krutch'))
    print(select_all_albums(NEW_DB,'Trip Lee'))
    