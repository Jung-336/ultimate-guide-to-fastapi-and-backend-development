import sqlite3
from typing import Any
from app_40.database.schemas import ShipmentRead, ShipmentCreate, ShipmentUpdate
from contextlib import contextmanager


class Database:
    def connect_to_db(self):
        self.conn = sqlite3.connect("sqlite.db", check_same_thread=False)
        self.cur = self.conn.cursor()


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
            "weight": row[1],
            "content": row[2],
            "status": row[3]
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


    def __enter__(self): 
        self.connect_to_db()
        self.create_table()
        return self

    def __exit__(self, *arg):
        self.close_conn()



@contextmanager
def managed_db():
    db = Database()
    # setup
    db.connect_to_db()
    db.create_table()
    
    yield db

    db.close_conn()

with managed_db() as db:
    print(db.get(12701))
    print(db.get(12702))


