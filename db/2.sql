SELECT region,
       AVG(height) AS average_height
FROM
  (SELECT height,
          athlete_id,
          country,
          region,
          row_num
   FROM
     (SELECT height,
             athlete_id,
             country,
             region,
             ROW_NUMBER() OVER (PARTITION BY country,
                                             region
                                ORDER BY height DESC) row_num
      FROM
        (SELECT DISTINCT height,
                         country_id,
                         athlete_id,
                         country,
                         region,
                         YEAR
         FROM
           (SELECT a.*,
                   b.*,
                   c.*,
                   d.*
            FROM
              (SELECT *
               FROM summer_games sg
               UNION ALL SELECT *
               FROM winter_games) a
            LEFT JOIN athletes b ON b.id = a.athlete_id
            LEFT JOIN countries c ON c.id=a.country_id
            LEFT JOIN country_stats d ON d.country_id = a.country_id)) aaaa) bbbb
   WHERE row_num = 2 ) ccc
GROUP BY region;