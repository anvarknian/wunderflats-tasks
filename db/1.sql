SELECT b.name AS name,
       a.*
FROM
  (SELECT COUNT(Gold) AS gold_count,
          athlete_id
   FROM
     (SELECT *
      FROM summer_games
      UNION ALL SELECT *
      FROM winter_games) ft
   GROUP BY ft.athlete_id
   HAVING gold_count >= 3
   ORDER BY gold_count DESC) a
LEFT JOIN athletes b ON a.athlete_id = b.id;