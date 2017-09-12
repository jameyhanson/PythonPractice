USE default;

DROP TABLE sample_date;

CREATE EXTERNAL TABLE sample_date ( -- cannot use OR REPLACE
    uuid STRING,
    rand_word STRING,
    random_int STRING,
    year_month STRING,
    datetime_ddmonyyyy STRING,
    datetime_iso TIMESTAMP) -- NOTE:  Cannot accept time-portion delimiter of 'T'
COMMENT 'sample data from https://github.com/jameyhanson/PythonPractice'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
LOCATION '/user/jamey/sample_date/';

SELECT *
FROM sample_date
LIMIT 10;

-- How to get the nth month
-- LIMITATIONS:
--     cannot have a LIMIT clause in a subquery
SELECT DISTINCT year_month
FROM sample_date
ORDER BY 1
LIMIT 10;
    
-- 10th month with inline view  
SELECT max(year_month) FROM
    (SELECT DISTINCT year_month
    FROM sample_date
    ORDER BY 1
    LIMIT 10) AS inline_view;
    
-- 10th month with row_number() windowing function
SELECT year_month
FROM (
    SELECT
        year_month,
        row_number() OVER (ORDER BY year_month) AS month_rank
    FROM (
        SELECT DISTINCT year_month
        FROM sample_date) AS inline_view) AS inline_view
WHERE month_rank = 10;    
    
-- 10th month using a windowing function window
SELECT
    max(year_month) OVER (
        ORDER BY year_month
        ROWS BETWEEN UNBOUNDED PRECEDING AND 9 FOLLOWING) AS jim2
FROM (
    SELECT DISTINCT year_month
    FROM sample_date) AS inline_view
LIMIT 1;