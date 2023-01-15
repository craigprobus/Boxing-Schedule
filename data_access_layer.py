import psycopg2

from db_init import Database
from parsers.boxer_card_parser import BoxerCardParser

class DataAccessLayer:
    def insert_boxer(self, weight_division: str, bcp: BoxerCardParser):
        conn = None
        cursor = None
        try:
            db = Database()
            conn = db.get_db_connection(conn)
            cursor = conn.cursor()
            insert_script = 'INSERT INTO boxer (name, profile_url, weight_division, rank_weight_division) ' \
                            'VALUES (%s, %s, %s, %s)'
            insert_values = [bcp.boxer_name, bcp.url, weight_division, str(bcp.boxer_ranking.replace("C", "0"))]
            cursor.execute(insert_script, insert_values)
            conn.commit()
        except Exception as e:
            print (e)
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def update_boxer_p4p_ranking(self, record_id: int, ranking: int):
        conn = None
        cursor = None
        try:
            db = Database()
            conn = db.get_db_connection(conn)
            cursor = conn.cursor()
            sql = 'UPDATE boxer ' \
                  'SET rank_pound_for_pound = %s ' \
                  'WHERE id = %s'
            cursor.execute(sql, (ranking, record_id))
            conn.commit()
        except Exception as e:
            print(e)
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def get_p4p_boxers(self, boxer_name: str):
        conn = None
        cursor = None
        try:
            db = Database()
            conn = db.get_db_connection(conn)
            cursor = conn.cursor()
            sql = 'SELECT Id, name, rank_pound_for_pound ' \
                  'FROM boxer ' \
                  'WHERE name = %s'
            cursor.execute(sql, (boxer_name,))
            return cursor.fetchall()
        except Exception as e:
            print(e)
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()