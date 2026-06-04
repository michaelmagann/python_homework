import sqlite3

try:
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id)
                REFERENCES publishers(publisher_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id)
                REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id)
                REFERENCES magazines(magazine_id)
        )
    """)

    def add_publisher(name):
        try:
            cursor.execute(
                "INSERT INTO publishers (name) VALUES (?)",
                (name,)
            )
        except sqlite3.IntegrityError:
            pass

    def add_magazine(name, publisher_id):
        try:
            cursor.execute(
                "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
                (name, publisher_id)
            )
        except sqlite3.IntegrityError:
            pass

    def add_subscriber(name, address):
        try:
            cursor.execute("""
                SELECT *
                FROM subscribers
                WHERE name = ? AND address = ?
            """, (name, address))

            if cursor.fetchone() is None:
                cursor.execute("""
                    INSERT INTO subscribers (name, address)
                    VALUES (?, ?)
                """, (name, address))

        except sqlite3.Error:
            pass

    def add_subscription(subscriber_id, magazine_id, expiration_date):
        try:
            cursor.execute("""
                SELECT *
                FROM subscriptions
                WHERE subscriber_id = ? AND magazine_id = ?
            """, (subscriber_id, magazine_id))

            if cursor.fetchone() is None:
                cursor.execute("""
                    INSERT INTO subscriptions
                    (subscriber_id, magazine_id, expiration_date)
                    VALUES (?, ?, ?)
                """, (subscriber_id, magazine_id, expiration_date))

        except sqlite3.Error:
            pass

    add_publisher("Slam Media Inc.")
    add_publisher("Minute Media")
    add_publisher("Modern Dog Magazine")

    add_magazine("Slam", 1)
    add_magazine("Sports Illustrated", 2)
    add_magazine("Modern Dog", 3)

    add_subscriber("Jayson Tatum", "0 Causeway Street")
    add_subscriber("Mike Magann", "450 Worcester Street")
    add_subscriber("Chase Dog", "123 Woof Road")

    add_subscription(1, 1, "1998-3-3")
    add_subscription(2, 2, "1984-3-30")
    add_subscription(3, 3, "2016-6-20")

    conn.commit()
    
    print("\nSubscribers")
    cursor.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)

    print("\nMagazines Sorted By Name")
    cursor.execute("""
        SELECT *
        FROM magazines
        ORDER BY name
    """)
    for row in cursor.fetchall():
        print(row)

    print("\nMagazines Published By Minute Media")
    cursor.execute("""
        SELECT magazines.name
        FROM magazines
        JOIN publishers
            ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = 'Minute Media'
    """)
    for row in cursor.fetchall():
        print(row)

    conn.close()

except sqlite3.Error as e:
    print(f"Database error: {e}")