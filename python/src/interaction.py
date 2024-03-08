import sqlite3

conn = sqlite3.connect('../data/blogs.sqlite')
cur = conn.cursor()


def execute_query(query, params):
    try:
        cur.execute(query, params)
        commit_changes()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
        conn.rollback()


# def fetch_query(query):
#     cur.execute(query)
#     cur.fetchall()
#     print(cur.fetchall())
#     close_connection()
def fetch_query(query):
    try:
        cur.execute(query)
        commit_changes()
        print(cur.fetchall())
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
        conn.rollback()


def close_connection():
    conn.close()


def commit_changes():
    conn.commit()


def main():
    execute_query("INSERT INTO blogs (title, body, author) VALUES (?, ?, ?)",
                  ("My very first blog post here.",
                   "Hello all. My name is Tim and I am excited to post here for the very first time. Looking forward to reading your comments.", 1))

    fetch_query("SELECT * FROM blogs")

    close_connection()


if __name__ == "__main__":
    main()
