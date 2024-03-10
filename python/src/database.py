import sqlite3

con = sqlite3.connect('../data/blogs.sqlite')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS blogs (
                blog_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL UNIQUE,
                body TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                author INTEGER NOT NULL,
                FOREIGN KEY (author) REFERENCES users(user_id)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                fullname TEXT NOT NULL UNIQUE
           )''')

cur.execute('''CREATE TABLE IF NOT EXISTS comments (
                comment_id INTEGER PRIMARY KEY,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                author INTEGER NOT NULL,
                blog INTEGER NOT NULL,
                FOREIGN KEY (author) REFERENCES users(user_id),
                FOREIGN KEY (blog) REFERENCES blogs(blog_id)
           )''')

# enter starter user.
# comma after param means treat tuple as a single element.
cur.execute("INSERT INTO users (fullname) VALUES (?)",
            ("Tim Q",))

cur.execute("INSERT INTO users (fullname) VALUES (?)",
            ("Tony",))

# delete multiple user id query.
# cur.execute("DELETE FROM users WHERE user_id IN (1,2)")

# delete the whole table.
# cur.execute("DROP TABLE IF EXISTS users")
# cur.execute("SELECT * FROM users")
print(cur.fetchall())

con.commit()

con.close()
