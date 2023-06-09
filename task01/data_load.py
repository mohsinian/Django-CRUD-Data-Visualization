import json
import sqlite3
import uuid
conn = sqlite3.connect('task01/db.sqlite3')
stock_json = json.load(open('task01/stock_market_data.json'))
columns = []
column = []
for data in stock_json:
    column = list(data.keys())
    for col in column:
        if col not in columns:
            columns.append(col)

value = []
values = []
for data in stock_json:
    id = uuid.uuid4()
    value.append(str(id))
    for i in columns:
        value.append(str(dict(data).get(i)))
    values.append(list(value))
    value.clear()

create_query = 'create table if not exists table_stock_data (id,date,trade_code,high,low,open,close,volume)'
insert_query = 'insert into table_stock_data values (?,?,?,?,?,?,?,?)'
c = conn.cursor()
c.execute(create_query)
c.executemany(insert_query, values)
conn.commit()
c.close()
