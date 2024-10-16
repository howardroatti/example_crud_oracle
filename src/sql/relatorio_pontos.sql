SELECT p.codigo_ponto,
       p.data_ponto,
       p.hora_entrada,
       p.hora_saida,
       p.codigo_funcionario 
FROM LABDATABASE.PONTOS p 
ORDER BY p.data_ponto
