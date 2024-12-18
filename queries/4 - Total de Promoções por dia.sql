SELECT 
   STRFTIME('%d', datetime) AS dia, 
   COUNT(*) AS total,
   SUM(new_amount) AS valor
FROM 
   products
GROUP BY 
    STRFTIME('%d', datetime)