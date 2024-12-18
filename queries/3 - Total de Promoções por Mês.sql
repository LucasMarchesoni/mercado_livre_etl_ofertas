SELECT 
   STRFTIME('%m', datetime) AS mes, 
   COUNT(*) AS total,
   SUM(new_amount) AS valor
FROM 
   products
GROUP BY 
    STRFTIME('%m', datetime)
