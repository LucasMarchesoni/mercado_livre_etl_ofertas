SELECT 
   STRFTIME('%m', datetime) AS mes,
   AVG(discount_percent) AS desconto_medio,
   AVG(original_amount - new_amount) AS valor_medio
FROM 
   products
GROUP BY 
   STRFTIME('%m', datetime)