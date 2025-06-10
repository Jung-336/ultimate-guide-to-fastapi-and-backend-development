import sqlite3
from typing import Any
from schemas import ShipmentRead, ShipmentCreate, ShipmentUpdate

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("sqlite.db", check_same_thread=False)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS shipment (
            id INTEGER PRIMARY KEY,
            content TEXT,
            weight REAL,
            status TEXT,
            destination INTEGER                          
        )
        """)


    def create(self, shipment: ShipmentCreate):
        # find a new id
        self.cur.execute("SELECT IFNULL(MAX(id), 0) + 1 FROM shipment")
        new_id = self.cur.fetchone()[0]

        self.cur.execute("""
        INSERT INTO shipment (id, content, weight, destination, status)
        VALUES(
                :id,
                :content,
                :weight,
                :destination,                        
                :status
               )
        """, {
                "id": new_id,
                **shipment.model_dump(),
                "status": "placed"
             }
        )
        self.conn.commit()

        return new_id
    

    def get(self, id: int) -> dict[str, Any] | None:
        self.cur.execute("""
            SELECT *
            FROM shipment
            WHERE id = ?
            """, (id,))
        
        row = self.cur.fetchone()

        return {
            "id": row[0],
            "content": row[1],
            "weight": row[2],
            "status": row[3],
            "destination": row[4],
        } if row else None


    def update(self, id: int, shipment: ShipmentUpdate) -> dict[str, Any]:
        self.cur.execute("""
        UPDATE shipment SET status = :status
        WHERE id = :id
        """, {
            "id": id,
            **shipment.model_dump()
        }) 
        self.conn.commit()

        return self.get(id)
    

    def delete(self, id: int):
        self.cur.execute("""
            DELETE shipment WHERE id = ?
        """, (id, ))
        self.conn.commit();
        return id
    
    def close_conn(self):
        self.conn.close()

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
# cursor.execute("""
# UPDATE shipment SET content = :content 
# WHERE id = :id
# """, {"id": 12702, "content":"요술봉"})
# connection.commit()


# # 99. reading records
# cursor.execute("""
# SELECT id, content, weight, status
# FROM shipment
# WHERE id = ?
# """, (12702,))


# for row in cursor:
#     print(row)


# cursor.close()
# connection.close()


