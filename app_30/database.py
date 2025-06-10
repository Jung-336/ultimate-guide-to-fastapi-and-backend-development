import sqlite3

connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()


# 1. Create a table
# cursor.execute("""
# CREATE TABLE shipment (
#     id INTEGER PRIMARY KEY,
#     content TEXT,
#     weight REAL,
#     status TEXT                          
# )
# """)


# 12701: {"weight": 10.6, "content": "rubber ducks", "status": 0},
# 12702: {"weight": 12.3, "content": "magic wands", "status": 1},
# 12703: {"weight": 11.1, "content": "unicorn horns", "status": 2},
# 12704: {"weight": 13.5, "content": "dragon eggs", "status": 2},
# 12705: {"weight": 10.9, "content": "wizard hats", "status": 1},


# 2. Add shipment record
# cursor.execute("""INSERT INTO shipment values(12701, 10.6, 'rubber ducks', 'placed')""")
# cursor.execute("""INSERT INTO shipment values(12702, 12.3, 'magic wands', 'in_transit')""")
# cursor.execute("""INSERT INTO shipment values(12703, 11.1, 'unicorn horns', 'placed')""")
# connection.commit()

# 3. update 
# cursor.execute("""
# UPDATE shipment SET content = '고무 오리' 
# WHERE id = ?
# """, (12701,))

# named parameters
cursor.execute("""
UPDATE shipment SET content = :content 
WHERE id = :id
""", {"id": 12702, "content":"요술봉"})
connection.commit()


# 99. reading records
cursor.execute("""
SELECT id, content, weight, status
FROM shipment
WHERE id = ?
""", (12702,))


for row in cursor:
    print(row)


cursor.close()
connection.close()


