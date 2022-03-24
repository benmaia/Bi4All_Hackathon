BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "reservations" (
	"id_reservations"	SMALLINT UNSIGNED,
	"start"	DATETIME NOT NULL,
	"end"	DATETIME NOT NULL,
	"id_room"	SMALLINT UNSIGNED,
	PRIMARY KEY("id_reservations"),
	FOREIGN KEY("id_room") REFERENCES "room"("id")
);
CREATE TABLE IF NOT EXISTS "room" (
	"id"	SMALLINT UNSIGNED,
	"capacity"	SMALLINT UNSIGNED NOT NULL,
	PRIMARY KEY("id")
);
INSERT INTO "reservations" ("id_reservations","start","end","id_room") VALUES (1,'2022-03-23 10:00','2022-03-23 11:00',2);
INSERT INTO "room" ("id","capacity") VALUES (2,4),
 (3,8),
 (4,6),
 (1,4);
COMMIT;
