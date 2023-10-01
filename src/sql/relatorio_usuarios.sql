select usuario.id_usuario
     , usuario.nome 
     , usuario.email 
     , usuario.telefone
  from usuarios usuario
 order by usuario.id_usuario