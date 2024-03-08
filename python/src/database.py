import sqlite3

con = sqlite3.connect('../data/blogs.sqlite')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS blogs (
                blog_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL UNIQUE,
                body TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                author INTEGER NOT NULL,
                FOREIGN KEY (author) REFERENCES users (user_id)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                fullname TEXT NOT NULL UNIQUE,
                owned_blogs INTEGER NOT NULL,
                owned_comments INTEGER NOT NULL
           )''')

cur.execute('''CREATE TABLE IF NOT EXISTS comments (
                comment_id INTEGER PRIMARY KEY,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                author INTEGER NOT NULL,
                blog INTEGER NOT NULL,
                FOREIGN KEY (author) REFERENCES users (user_id),
                FOREIGN KEY (blog) REFERENCES blogs (blog_id)
           )''')

# enter starter user.
cur.execute("INSERT INTO users (fullname, owned_blogs, owned_comments) VALUES (?, ?, ?)",
            ("Tim Q", 0, 0))

cur.execute("SELECT * FROM users")
print(cur.fetchall())

con.commit()

con.close()
