-- THIS IS FOR RESULTS @ EACH TC
SELECT
    COUNT(CASE WHEN "Result" = '1-0' THEN 1 END) AS 'White wins',
    COUNT(CASE WHEN "Result" = '1/2-1/2' THEN 1 END) AS 'Draw',
    COUNT(CASE WHEN "Result" = '0-1' THEN 1 END) AS 'Black Wins'
FROM testable WHERE "Time Control" = '60+0';
SELECT
    COUNT(CASE WHEN "Result" = '1-0' THEN 1 END) AS 'White wins',
    COUNT(CASE WHEN "Result" = '1/2-1/2' THEN 1 END) AS 'Draw',
    COUNT(CASE WHEN "Result" = '0-1' THEN 1 END) AS 'Black Wins'
FROM testable WHERE "Time Control" = '120+1';
SELECT
    COUNT(CASE WHEN "Result" = '1-0' THEN 1 END) AS 'White wins',
    COUNT(CASE WHEN "Result" = '1/2-1/2' THEN 1 END) AS 'Draw',
    COUNT(CASE WHEN "Result" = '0-1' THEN 1 END) AS 'Black Wins'
FROM testable WHERE "Time Control" = '180+0';
SELECT
    COUNT(CASE WHEN "Result" = '1-0' THEN 1 END) AS 'White wins',
    COUNT(CASE WHEN "Result" = '1/2-1/2' THEN 1 END) AS 'Draw',
    COUNT(CASE WHEN "Result" = '0-1' THEN 1 END) AS 'Black Wins'
FROM testable WHERE "Time Control" = '180+2';
SELECT
    COUNT(CASE WHEN "Result" = '1-0' THEN 1 END) AS 'White wins',
    COUNT(CASE WHEN "Result" = '1/2-1/2' THEN 1 END) AS 'Draw',
    COUNT(CASE WHEN "Result" = '0-1' THEN 1 END) AS 'Black Wins'
FROM testable WHERE "Time Control" = '300+0';
SELECT
    COUNT(CASE WHEN "Result" = '1-0' THEN 1 END) AS 'White wins',
    COUNT(CASE WHEN "Result" = '1/2-1/2' THEN 1 END) AS 'Draw',
    COUNT(CASE WHEN "Result" = '0-1' THEN 1 END) AS 'Black Wins'
FROM testable WHERE "Time Control" = '300+3';
SELECT
    COUNT(CASE WHEN "Result" = '1-0' THEN 1 END) AS 'White wins',
    COUNT(CASE WHEN "Result" = '1/2-1/2' THEN 1 END) AS 'Draw',
    COUNT(CASE WHEN "Result" = '0-1' THEN 1 END) AS 'Black Wins'
FROM testable WHERE "Time Control" = '600+0';
SELECT
    COUNT(CASE WHEN "Result" = '1-0' THEN 1 END) AS 'White wins',
    COUNT(CASE WHEN "Result" = '1/2-1/2' THEN 1 END) AS 'Draw',
    COUNT(CASE WHEN "Result" = '0-1' THEN 1 END) AS 'Black Wins'
FROM testable WHERE "Time Control" = '900+15';