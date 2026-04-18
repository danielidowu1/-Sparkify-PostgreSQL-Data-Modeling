import psycopg2
from Sql_table_queries.py import create_table_queries, drop_table_queries

def create_database():
    conn = psycopg2.connect(
    host= "localhost",
    database="postgres",
    user="postgres",
    password="Belinbos1996",
    port="5432"
    )

    conn.set_session(autocommit = True)
        
    cur = conn.cursor()
        
    cur.execute("DROP DATABASE IF EXISTS sparkifydb;")
        
    cur.execute("CREATE TABLE IF NOT EXISTS sparkifydb;")
        
    conn.close()
        
    conn = psycopg2.connect(
    host= "localhost",
    database="sparkifydb",
    user="postgres",
    password="Belinbos1996",
    port="5432"
    )
    cur = conn.cursor()
        
    return cur, conn

def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    cur, conn = create_database()
    drop_tables(cur, conn)
    create_tables(cur, conn)
    conn.close()


if __name__ == "__main__":
    __main__
    