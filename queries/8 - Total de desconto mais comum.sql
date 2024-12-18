SELECT  
  discount_percent as percentual,
  COUNT(*) AS total
FROM 
	products
WHERE
	discount_percent IS NOT NULL
GROUP BY 
	discount_percent
ORDER BY
	total
DESC;