import sqlite3 from "sqlite3";
const db = new sqlite3.Database("./data/db.sqlite");

db.run(
  "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)"
);

db.run(
  "INSERT INTO users (name, email) VALUES (?, ?)",
  ["Tim Q", "t@gmail.com"],
  (err) => {
    if (err) {
      return console.log(err.message);
    }
    console.log("user added to db!");
  }
);

db.close();
