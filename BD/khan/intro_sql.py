# /** Grocery list: 
# Bananas (4)
# Peanut Butter (1)
# Dark Chocolate Bars (2)
# **/

# CREATE TABLE groceries (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER );

# INSERT INTO groceries VALUES (1, "Bananas", 4);
# INSERT INTO groceries VALUES (2, "Peanut Butter", 1);
# INSERT INTO groceries VALUES (3, "Dark chocolate bars", 2);
# SELECT * FROM groceries;



# Quais são os seus livros favoritos? Você pode criar uma tabela no banco de dados e guardá-los lá! Nesse primeiro passo, crie uma tabela para guardar a sua lista de livros. Esta deverá conter colunas para id, name, e rating (identificador, nome e avaliação - é preciso que você use os nomes em inglês para que o programa possa verificar se está tudo ok).

# CREATE TABLE books(id INTEGER PRIMARY KEY, name TEXT, stars INTEGER);

# INSERT INTO books VALUES (1, "Harry Potter", 10);
# INSERT INTO books VALUES (2, "Walden", 10);
# INSERT INTO books VALUES (3, "Flow", 9);
# SELECT * FROM books;



'''
CREATE TABLE groceries (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, aisle INTEGER);
INSERT INTO groceries VALUES (1, "Bananas", 56, 7);
INSERT INTO groceries VALUES(2, "Peanut Butter", 1, 2);
INSERT INTO groceries VALUES(3, "Dark Chocolate Bars", 2, 2);
INSERT INTO groceries VALUES(4, "Ice cream", 1, 12);
INSERT INTO groceries VALUES(5, "Cherries", 6, 2);
INSERT INTO groceries VALUES(6, "Chocolate syrup", 1, 4);

SELECT aisle, SUM(quantity) FROM groceries GROUP BY aisle;

RESULTADO:

aisle     SUM(quantity)
2         9
4         1
7         56
12        1











CREATE TABLE shoes (id INTEGER PRIMARY KEY, name TEXT, nationality TEXT, color TEXT, value INTEGER);

INSERT INTO shoes VALUES (1, "DCSHOES", "EUA", "blue, pink or grey", 500);
INSERT INTO shoes VALUES (2, "VANS", "EUA", "red, green or orange", 600);
INSERT INTO shoes VALUES (3, "NIKE", "EUA", "black or white", 800);
INSERT INTO shoes VALUES (4, "ADIDAS", "GERMANY", "Yellow, black or red", 750);
INSERT INTO shoes VALUES (5, "PUMA", "SOUTH AFRICA", "PURPLE", 400);
INSERT INTO shoes VALUES (6, "ASICS", "ENGLAND", "Blue or red", 299);
INSERT INTO shoes VALUES (7, "UNDER ARMOUR", "HAWAI", "grey", 359);
INSERT INTO shoes VALUES (8, "REBOOK", "BR", "Green or Yellow", 290);
INSERT INTO shoes VALUES (9, "BULLS", "JAPAN", "White or Red", 199);
INSERT INTO shoes VALUES (10, "LAKERS", "PETU", "BROWN", 387);
INSERT INTO shoes VALUES (11, "PEPE", "URUGUAY", "BLUE", 78262);
INSERT INTO shoes VALUES (12, "HAVAIANAS", "BRASIL", "WHITE OR GREEN", 8236);
INSERT INTO shoes VALUES (13, "JHDHS", "HGDHS", "JLSDSKH", 36825);
INSERT INTO shoes VALUES (14, "dsdsds", "dsdsdsd", "dsdds", 65);
INSERT INTO shoes VALUES (15, "DSDS", "DSDSDS", "WDFSGFGF", 7545);
SELECT * FROM shoes ORDER BY value;

SUM(value) FROM shoes GROUP BY value;















CREATE TABLE exercise_logs
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    minutes INTEGER, 
    calories INTEGER,
    heart_rate INTEGER);


INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("biking", 30, 100, 110);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("biking", 10, 30, 105);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("dancing", 15, 200, 120);

SELECT * FROM exercise_logs WHERE calories > 50 ORDER BY calories;

/* AND */
SELECT * FROM exercise_logs WHERE calories > 50 AND minutes < 30;

/* OR */
SELECT * FROM exercise_logs WHERE calories > 50 OR heart_rate > 100;





CREATE TABLE exercise_logs
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    minutes INTEGER, 
    calories INTEGER,
    heart_rate INTEGER);

INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("biking", 30, 100, 110);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("biking", 10, 30, 105);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("dancing", 15, 200, 120);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("tree climbing", 30, 70, 90);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("tree climbing", 25, 72, 80);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("rowing", 30, 70, 90);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("hiking", 60, 80, 85);

SELECT * FROM exercise_logs WHERE type = "biking" OR type = "hiking" OR type = "tree climbing" OR type = "rowing";

/* IN */
SELECT * FROM exercise_logs WHERE type IN ("biking", "hiking", "tree climbing", "rowing");

CREATE TABLE drs_favorites
    (id INTEGER PRIMARY KEY,
    type TEXT,
    reason TEXT);

INSERT INTO drs_favorites(type, reason) VALUES ("biking", "Improves endurance and flexibility.");
INSERT INTO drs_favorites(type, reason) VALUES ("hiking", "Increases cardiovascular health.");

SELECT type FROM drs_favorites;

SELECT * FROM exercise_logs WHERE type IN (
    SELECT type FROM drs_favorites);
    
SELECT * FROM exercise_logs WHERE type IN (
    SELECT type FROM drs_favorites WHERE reason = "Increases cardiovascular health");
    
/* LIKE */

SELECT * FROM exercise_logs WHERE type IN (
    SELECT type FROM drs_favorites WHERE reason LIKE "%cardiovascular%");









CREATE TABLE exercise_logs
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    minutes INTEGER, 
    calories INTEGER,
    heart_rate INTEGER);

INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("biking", 30, 100, 110);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("biking", 10, 30, 105);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("dancing", 15, 200, 120);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("tree climbing", 30, 70, 90);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("tree climbing", 25, 72, 80);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("rowing", 30, 70, 90);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("hiking", 60, 80, 85);

SELECT * FROM exercise_logs WHERE type = "biking" OR type = "hiking" OR type = "tree climbing" OR type = "rowing";

/* IN */
SELECT * FROM exercise_logs WHERE type IN ("biking", "hiking", "tree climbing", "rowing");

CREATE TABLE drs_favorites
    (id INTEGER PRIMARY KEY,
    type TEXT,
    reason TEXT);

INSERT INTO drs_favorites(type, reason) VALUES ("biking", "Improves endurance and flexibility.");
INSERT INTO drs_favorites(type, reason) VALUES ("hiking", "Increases cardiovascular health.");

SELECT type FROM drs_favorites;

SELECT * FROM exercise_logs WHERE type IN (
    SELECT type FROM drs_favorites);
    
SELECT * FROM exercise_logs WHERE type IN (
    SELECT type FROM drs_favorites WHERE reason = "Increases cardiovascular health");
    
/* LIKE */

SELECT * FROM exercise_logs WHERE type IN (
    SELECT type FROM drs_favorites WHERE reason LIKE "%cardiovascular%");




'''

