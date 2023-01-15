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