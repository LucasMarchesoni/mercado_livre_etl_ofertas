SELECT  
  total_installments as parcelas,
  COUNT(*) AS total
FROM 
	products
WHERE
	total_installments IS NOT NULL
GROUP BY 
	total_installments
ORDER BY
	total
DESC;