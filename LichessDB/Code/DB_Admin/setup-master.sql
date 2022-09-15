CREATE TABLE "Master" (
	"Event" TEXT,
	"Site (URL)" TEXT PRIMARY KEY,
	"White" TEXT,
	"Black" TEXT,
	"Result" TEXT,
	"Date (UTC)" TEXT,
	"Time (UTC)" TEXT,
	"White Elo" INTEGER,
	"Black Elo" INTEGER,
	"White Rating Change" TEXT,
	"Black Rating Change" TEXT,
	"ECO Code" TEXT,
	"Opening Name" TEXT,
	"Time Control" TEXT,
	"Termination" TEXT,
	"Game Length (Ply)" INTEGER,
	"Moves" TEXT,
	"Download Month" INTEGER
);

CREATE INDEX "Event Index" ON Master("Event");
CREATE INDEX "Result Index" ON Master("Result");
CREATE INDEX "Date Index" ON Master("Date (UTC)");
CREATE INDEX "Time Index" ON Master("Time (UTC)");
CREATE INDEX "White Elo Index" ON Master("White Elo");
CREATE INDEX "BLack Elo Index" ON Master("Black Elo");
CREATE INDEX "ECO Code Index" ON Master("ECO Code");
CREATE INDEX "Time Control Index" ON Master("Time Control");
CREATE INDEX "Termination Index" ON Master("Termination");
CREATE INDEX "Game Length Index" ON Master("Game Length (Ply)");
CREATE INDEX "Download Month Index" ON Master("Download Month");

INSERT INTO "Master" SELECT * FROM "2013-01";