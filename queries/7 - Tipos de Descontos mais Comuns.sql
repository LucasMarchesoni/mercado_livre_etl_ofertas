SELECT  
  UPPER(discount_type) as desconto,
  COUNT(*) AS total
FROM 
	products
WHERE
	discount_type IS NOT NULL
GROUP BY 
	UPPER(discount_type)
ORDER BY
	total
DESC;