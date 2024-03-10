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


user_tim_id = 1
user_tony_id = 2


def main():
    execute_query("INSERT INTO blogs (title, body, author) VALUES (?, ?, ?)",
                  ("My very first blog post here.",
                   "Hello all. My name is Tim and I am excited to post here for the very first time. Looking forward to reading your comments.", user_tim_id))

# blog with comment
    row = cur.execute(
        "SELECT blogs.title, blogs.body, comments.content FROM blogs LEFT JOIN comments ON blogs.blog_id = comments.blog ORDER BY comments.content DESC LIMIT 5;")
    for r in row:
        print(f"[blog]: {r[0]}\n")
        print(f"[comment]: {r[2]}")


execute_query("INSERT INTO comments (content, author, blog) VALUES (?, ?, ?)",
              ("Nice blog, I found it very informative.", user_tony_id, 1))

close_connection()


if __name__ == "__main__":
    main()
