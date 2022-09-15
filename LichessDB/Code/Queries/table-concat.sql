-- THIS IS FOR CONCATENATING SUMS FROM MULTIPLE TABLES
SELECT "Time Control", SUM(Number) AS Total FROM
(
    SELECT "Time Control", COUNT(*) AS Number
    FROM "2013-01"
    GROUP BY "Time Control"

    UNION ALL

    SELECT "Time Control", COUNT(*) AS Number
    FROM "2013-02"
    GROUP BY "Time Control"

    UNION ALL

    SELECT "Time Control", COUNT(*) AS Number
    FROM "2013-03"
    GROUP BY "Time Control"

    UNION ALL

    SELECT "Time Control", COUNT(*) AS Number
    FROM "2013-04"
    GROUP BY "Time Control"

    UNION ALL

    SELECT "Time Control", COUNT(*) AS Number
    FROM "2013-05"
    GROUP BY "Time Control"

    UNION ALL

    SELECT "Time Control", COUNT(*) AS Number
    FROM "2013-06"
    GROUP BY "Time Control"

    UNION ALL

    SELECT "Time Control", COUNT(*) AS Number
    FROM "2013-07"
    GROUP BY "Time Control"

    UNION ALL

    SELECT "Time Control", COUNT(*) AS Number
    FROM "2013-08"
    GROUP BY "Time Control"

    UNION ALL

    SELECT "Time Control", COUNT(*) AS Number
    FROM "2013-09"
    GROUP BY "Time Control"

    UNION ALL

    SELECT "Time Control", COUNT(*) AS Number
    FROM "2013-10"
    GROUP BY "Time Control"

    UNION ALL

    SELECT "Time Control", COUNT(*) AS Number
    FROM "2013-11"
    GROUP BY "Time Control"
)
GROUP BY "Time Control" HAVING Total > 50 ORDER BY Total DESC;