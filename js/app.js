import sqlite3 from "sqlite3";
const db = new sqlite3.Database("./data/db.sqlite");

db.run(
  "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, fullname TEXT NOT NULL UNIQUE)"
);

db.run(
  "CREATE TABLE IF NOT EXISTS blogs (blog_id INTEGER PRIMARY KEY, title TEXT NOT NULL, body TEXT NOT NULL, author INTEGER NOT NULL, FOREIGN KEY (author) REFERENCES users(user_id))"
);

db.run(
  "CREATE TABLE IF NOT EXISTS comments (comment_id INTEGER PRIMARY KEY, comment TEXT NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, author INTEGER NOT NULL, blog INTEGER NOT NULL, FOREIGN KEY (author) REFERENCES users(user_id), FOREIGN KEY (blog) REFERENCES blogs(blog_id))"
);

function insertUser(fullname) {
  db.run(
    "INSERT INTO users (fullname) VALUES (?)",
    [fullname],
    (err) => {
      if (err) {
        console.error("Error inserting user:", err.message);
      }
    }
  );
}

insertUser("tom");

function insertBlog(title, body, author) {
  db.run(
    "INSERT INTO blogs (title, body, author) VALUES (?, ?, ?)",
    [title, body, author],
    (err) => {
      if (err) {
        console.error("Error inserting blog:", err.message);
      }
    }
  );
}

insertBlog("blog by Tim", "this is a blog by tim", 1);

function insertComment(comment, author, blog_id) {
  db.run(
    "INSERT INTO comments (comment, author, blog) VALUES (?, ?, ?)",
    [comment, author, blog_id],
    (err) => {
      if (err) {
        console.error("Error inserting comment:", err.message);
      }
    }
  );
}

insertComment("this is tom", 3, 6);

db.each(
  "SELECT blog_id,title, body, blogs.author " +
    "FROM blogs " +
    "JOIN comments ON blogs.author = comments.author",
  (err, row) => {
    if (err) {
      console.error("Error selecting users:", err.message);
    }
    console.log(row);
  }
);

//blogs with comments

db.each(
  "SELECT blogs.blog_id, blogs.title, blogs.body, blogs.author FROM blogs JOIN comments ON blogs.blog_id = comments.blog",
  (err, row) => {
    if (err) {
      console.error("Error selecting users:", err.message);
    }
    console.log(row);
  }
);

db.close();
