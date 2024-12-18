WITH vendas AS (
  SELECT 
    UPPER(supplier) AS fornecedor,
    COUNT(*) AS total_vendas,
    SUM(new_amount) AS valor
  FROM 
    products
  WHERE 
    supplier IS NOT NULL
  GROUP BY 
    UPPER(supplier)
)
SELECT 
  fornecedor, 
  total_vendas, 
  valor, 
  valor / CAST(total_vendas AS FLOAT) AS media_valor
FROM 
  vendas
ORDER BY 
  total_vendas 
DESC;