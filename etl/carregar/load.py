import sqlite3

class Load:
  def __init__(self, db_file):
    self.db_file = db_file

  def to_sqlite(self, df, table_name):
    conn = sqlite3.connect(self.db_file)
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()