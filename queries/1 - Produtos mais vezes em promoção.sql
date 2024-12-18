SELECT  
  product_name as produto,
  COUNT(*) AS total
FROM 
	products
GROUP BY 
	product_name
ORDER BY
	total
DESC;