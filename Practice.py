from mysql.connector import MySQLConnection, Error
 
def insert_values(year, injuries):
    query = "INSERT INTO oh_ohs(year, injuries) " \
            "VALUES(%s, %s)"
    args = (year, injuries)
 
    try:
        config = {
        'user': 'root',
        'password': 'admin',
        'host': 'localhost',
        'database': 'Jesse'
        }
        conn = MySQLConnection(**config)
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        # Commit changes to the db
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
   # execute one
   insert_values('1974','76235')

if __name__ == '__main__':
    main()
