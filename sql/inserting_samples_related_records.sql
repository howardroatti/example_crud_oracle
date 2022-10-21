/*INSERE DADOS NA TABELA DE PEDIDOS E ITENS*/
DECLARE
  VCOD_PEDIDO NUMBER;
  VCOD_ITEM_PEDIDO NUMBER;
  VCOD_PRODUTO NUMBER;
BEGIN
  VCOD_PEDIDO := LABDATABASE.PRODUTOS_CODIGO_PRODUTO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.PEDIDOS VALUES(VCOD_PEDIDO,    /*CODIGO_PEDIDO*/
                             SYSDATE,        /*DATA_PEDIDO*/
                             '43201234567',  /*CPF*/
                             '01234567891234'/*CNPJ*/
                             );
  
  VCOD_ITEM_PEDIDO := LABDATABASE.ITENS_PEDIDO_CODIGO_ITEM_SEQ.NEXTVAL;
  
  SELECT CODIGO_PRODUTO
    INTO VCOD_PRODUTO
    FROM LABDATABASE.PRODUTOS
   WHERE DESCRICAO_PRODUTO = 'IPHONE 11';
  
  INSERT INTO LABDATABASE.ITENS_PEDIDO VALUES(VCOD_ITEM_PEDIDO, /*CODIGO_ITEM_PEDIDO*/
                                  111,              /*QUANTIDADE*/
                                  3900,             /*VALOR*/
                                  VCOD_PEDIDO,      /*CODIGO_PEDIDO*/
                                  VCOD_PRODUTO      /*CODIGO_PRODUTO*/
                                  );
END;
--
DECLARE
  VCOD_PEDIDO NUMBER;
  VCOD_ITEM_PEDIDO NUMBER;
  VCOD_PRODUTO NUMBER;
BEGIN
  VCOD_PEDIDO := LABDATABASE.PRODUTOS_CODIGO_PRODUTO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.PEDIDOS VALUES(VCOD_PEDIDO,    /*CODIGO_PEDIDO*/
                             SYSDATE,        /*DATA_PEDIDO*/
                             '01234567891',  /*CPF*/
                             '01234567891234'/*CNPJ*/
                             );
  
  VCOD_ITEM_PEDIDO := LABDATABASE.ITENS_PEDIDO_CODIGO_ITEM_SEQ.NEXTVAL;
  
  SELECT CODIGO_PRODUTO
    INTO VCOD_PRODUTO
    FROM LABDATABASE.PRODUTOS
   WHERE DESCRICAO_PRODUTO = 'IPHONE 12';
  
  INSERT INTO LABDATABASE.ITENS_PEDIDO VALUES(VCOD_ITEM_PEDIDO, /*CODIGO_ITEM_PEDIDO*/
                                  122,              /*QUANTIDADE*/
                                  4500,             /*VALOR*/
                                  VCOD_PEDIDO,      /*CODIGO_PEDIDO*/
                                  VCOD_PRODUTO      /*CODIGO_PRODUTO*/
                                  );
END;
--
DECLARE
  VCOD_PEDIDO NUMBER;
  VCOD_ITEM_PEDIDO NUMBER;
  VCOD_PRODUTO NUMBER;
BEGIN
  VCOD_PEDIDO := LABDATABASE.PRODUTOS_CODIGO_PRODUTO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.PEDIDOS VALUES(VCOD_PEDIDO,    /*CODIGO_PEDIDO*/
                             SYSDATE,        /*DATA_PEDIDO*/
                             '87654320123',  /*CPF*/
                             '01234567891234'/*CNPJ*/
                             );
  
  VCOD_ITEM_PEDIDO := LABDATABASE.ITENS_PEDIDO_CODIGO_ITEM_SEQ.NEXTVAL;
  
  SELECT CODIGO_PRODUTO
    INTO VCOD_PRODUTO
    FROM LABDATABASE.PRODUTOS
   WHERE DESCRICAO_PRODUTO = 'IPHONE 13';
  
  INSERT INTO LABDATABASE.ITENS_PEDIDO VALUES(VCOD_ITEM_PEDIDO, /*CODIGO_ITEM_PEDIDO*/
                                  131,              /*QUANTIDADE*/
                                  6500,             /*VALOR*/
                                  VCOD_PEDIDO,      /*CODIGO_PEDIDO*/
                                  VCOD_PRODUTO      /*CODIGO_PRODUTO*/
                                  );
                                  
  VCOD_ITEM_PEDIDO := LABDATABASE.ITENS_PEDIDO_CODIGO_ITEM_SEQ.NEXTVAL;
  
  SELECT CODIGO_PRODUTO
    INTO VCOD_PRODUTO
    FROM LABDATABASE.PRODUTOS
   WHERE DESCRICAO_PRODUTO = 'SAMGUNG GALAXY S22';
  
  INSERT INTO LABDATABASE.ITENS_PEDIDO VALUES(VCOD_ITEM_PEDIDO, /*CODIGO_ITEM_PEDIDO*/
                                  100,              /*QUANTIDADE*/
                                  5500,             /*VALOR*/
                                  VCOD_PEDIDO,      /*CODIGO_PEDIDO*/
                                  VCOD_PRODUTO      /*CODIGO_PRODUTO*/
                                  );
END;
--
DECLARE
  VCOD_PEDIDO NUMBER;
  VCOD_ITEM_PEDIDO NUMBER;
  VCOD_PRODUTO NUMBER;
BEGIN
  VCOD_PEDIDO := LABDATABASE.PRODUTOS_CODIGO_PRODUTO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.PEDIDOS VALUES(VCOD_PEDIDO,    /*CODIGO_PEDIDO*/
                             SYSDATE,        /*DATA_PEDIDO*/
                             '32012345678',  /*CPF*/
                             '00001234567891'/*CNPJ*/
                             );
  
  VCOD_ITEM_PEDIDO := LABDATABASE.ITENS_PEDIDO_CODIGO_ITEM_SEQ.NEXTVAL;
  
  SELECT CODIGO_PRODUTO
    INTO VCOD_PRODUTO
    FROM LABDATABASE.PRODUTOS
   WHERE DESCRICAO_PRODUTO = 'IPHONE 11';
  
  INSERT INTO LABDATABASE.ITENS_PEDIDO VALUES(VCOD_ITEM_PEDIDO, /*CODIGO_ITEM_PEDIDO*/
                                  111,              /*QUANTIDADE*/
                                  3750,             /*VALOR*/
                                  VCOD_PEDIDO,      /*CODIGO_PEDIDO*/
                                  VCOD_PRODUTO      /*CODIGO_PRODUTO*/
                                  );
                                  
  VCOD_ITEM_PEDIDO := LABDATABASE.ITENS_PEDIDO_CODIGO_ITEM_SEQ.NEXTVAL;
  
  SELECT CODIGO_PRODUTO
    INTO VCOD_PRODUTO
    FROM LABDATABASE.PRODUTOS
   WHERE DESCRICAO_PRODUTO = 'MOTOROLA G50';
  
  INSERT INTO LABDATABASE.ITENS_PEDIDO VALUES(VCOD_ITEM_PEDIDO, /*CODIGO_ITEM_PEDIDO*/
                                  78,              /*QUANTIDADE*/
                                  2900,             /*VALOR*/
                                  VCOD_PEDIDO,      /*CODIGO_PEDIDO*/
                                  VCOD_PRODUTO      /*CODIGO_PRODUTO*/
                                  );
                                  
END;
--
DECLARE
  VCOD_PEDIDO NUMBER;
  VCOD_ITEM_PEDIDO NUMBER;
  VCOD_PRODUTO NUMBER;
BEGIN
  VCOD_PEDIDO := LABDATABASE.PRODUTOS_CODIGO_PRODUTO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.PEDIDOS VALUES(VCOD_PEDIDO,    /*CODIGO_PEDIDO*/
                             SYSDATE,        /*DATA_PEDIDO*/
                             '76543201234',  /*CPF*/
                             '00012345678912'/*CNPJ*/
                             );
  
  VCOD_ITEM_PEDIDO := LABDATABASE.ITENS_PEDIDO_CODIGO_ITEM_SEQ.NEXTVAL;
  
  SELECT CODIGO_PRODUTO
    INTO VCOD_PRODUTO
    FROM LABDATABASE.PRODUTOS
   WHERE DESCRICAO_PRODUTO = 'IPHONE 14';
  
  INSERT INTO LABDATABASE.ITENS_PEDIDO VALUES(VCOD_ITEM_PEDIDO, /*CODIGO_ITEM_PEDIDO*/
                                  50,              /*QUANTIDADE*/
                                  8000,             /*VALOR*/
                                  VCOD_PEDIDO,      /*CODIGO_PEDIDO*/
                                  VCOD_PRODUTO      /*CODIGO_PRODUTO*/
                                  );
                                  
  VCOD_ITEM_PEDIDO := LABDATABASE.ITENS_PEDIDO_CODIGO_ITEM_SEQ.NEXTVAL;
  
  SELECT CODIGO_PRODUTO
    INTO VCOD_PRODUTO
    FROM LABDATABASE.PRODUTOS
   WHERE DESCRICAO_PRODUTO = 'MOTOROLA G50';
  
  INSERT INTO LABDATABASE.ITENS_PEDIDO VALUES(VCOD_ITEM_PEDIDO, /*CODIGO_ITEM_PEDIDO*/
                                  30,              /*QUANTIDADE*/
                                  2900,             /*VALOR*/
                                  VCOD_PEDIDO,      /*CODIGO_PEDIDO*/
                                  VCOD_PRODUTO      /*CODIGO_PRODUTO*/
                                  );
                                  
END;