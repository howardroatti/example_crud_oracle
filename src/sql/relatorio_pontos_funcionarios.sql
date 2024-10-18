SELECT 
    f.codigo_funcionario,
    f.nome,
    f.cargo,
    COUNT(CASE WHEN TO_CHAR(p.hora_entrada, 'HH24:MI') > '08:00' THEN 1 END) AS dias_atraso,
    ROUND(240 - NVL(SUM(
        (TO_NUMBER(TO_CHAR(p.hora_saida, 'HH24')) * 60 + TO_NUMBER(TO_CHAR(p.hora_saida, 'MI')))
        - (TO_NUMBER(TO_CHAR(p.hora_entrada, 'HH24')) * 60 + TO_NUMBER(TO_CHAR(p.hora_entrada, 'MI')))
    ) / 60, 0), 1) AS horas_a_complementar
FROM
    LABDATABASE.FUNCIONARIOS f
LEFT JOIN 
    LABDATABASE.PONTOS p ON f.codigo_funcionario = p.codigo_funcionario
GROUP BY 
    f.codigo_funcionario, f.nome, f.cargo
ORDER BY 
    f.nome
