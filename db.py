import mysql.connector
from config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def insert_dados(variavel1,variavel2,variavel3):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO dados_prensa (data_hora, pressao, posicao, status_digital)
            VALUES (NOW(), %s, %s, %s)
        """
        cursor.execute(sql, (
            variavel1,
            variavel2,
            variavel3
        ))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Erro ao inserir no banco: {e}")
