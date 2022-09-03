from model.itens_pedido import ItemPedido
from model.produtos import Produto
from controller.controller_produto import Controller_Produto
from model.pedidos import Pedido
from controller.controller_pedido import Controller_Pedido
from model.fornecedores import Fornecedor
from controller.controller_fornecedor import Controller_Fornecedor
from conexion.oracle_queries import OracleQueries

class Controller_Item_Pedido:
    def __init__(self):
        self.ctrl_produto = Controller_Produto()
        self.ctrl_pedido = Controller_Pedido()
        self.ctrl_fornecedor = Controller_Fornecedor()
        
    def inserir_item_pedido(self) -> ItemPedido:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        
        # Lista os pedido existentes para inserir no item de pedido
        self.listar_pedidos(oracle, need_connect=True)
        codigo_pedido = str(input("Digite o número do Pedido: "))
        pedido = self.valida_pedido(oracle, codigo_pedido)
        if pedido == None:
            return None

        # Lista os produtos existentes para inserir no item de pedido
        self.listar_produtos(oracle, need_connect=True)
        codigo_produto = str(input("Digite o código do Produto: "))
        produto = self.valida_produto(oracle, codigo_produto)
        if produto == None:
            return None

        # Solicita a quantidade de itens do pedido para o produto selecionado
        quantidade = float(input(f"Informe a quantidade de itens do produto {produto.get_descricao()}: "))
        # Solicita o valor unitário do produto selecionado
        valor_unitario = float(input(f"Informe o valor unitário do produto {produto.get_descricao()}: "))

        # Recupera o cursor para executar um bloco PL/SQL anônimo
        cursor = oracle.connect()
        # Cria a variável de saída com o tipo especificado
        output_value = cursor.var(int)

        # Cria um dicionário para mapear as variáveis de entrada e saída
        data = dict(codigo=output_value, quantidade=quantidade, valor_unitario=valor_unitario, codigo_pedido=int(pedido.get_codigo_pedido()), codigo_produto=int(produto.get_codigo()))
        # Executa o bloco PL/SQL anônimo para inserção do novo item de pedido e recuperação da chave primária criada pela sequence
        cursor.execute("""
        begin
            :codigo := ITENS_PEDIDO_CODIGO_ITEM_SEQ.NEXTVAL;
            insert into itens_pedido values(:codigo, :quantidade, :valor_unitario, :codigo_pedido, :codigo_produto);
        end;
        """, data)
        # Recupera o código do novo item de pedido
        codigo_item_pedido = output_value.getvalue()
        # Persiste (confirma) as alterações
        oracle.conn.commit()
        # Recupera os dados do novo item de pedido criado transformando em um DataFrame
        df_item_pedido = oracle.sqlToDataFrame(f"select codigo_item_pedido, quantidade, valor_unitario, codigo_pedido, codigo_produto from itens_pedido where codigo_item_pedido = {codigo_item_pedido}")
        # Cria um novo objeto Item de Pedido
        novo_item_pedido = ItemPedido(df_item_pedido.codigo_item_pedido.values[0], df_item_pedido.quantidade.values[0], df_item_pedido.valor_unitario.values[0], pedido, produto)
        # Exibe os atributos do novo Item de Pedido
        print(novo_item_pedido.to_string())
        # Retorna o objeto novo_item_pedido para utilização posterior, caso necessário
        return novo_item_pedido

    def atualizar_item_pedido(self) -> ItemPedido:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do item de pedido a ser alterado
        codigo_item_pedido = int(input("Código do Item de Pedido que irá alterar: "))        

        # Verifica se o item de pedido existe na base de dados
        if not self.verifica_existencia_item_pedido(oracle, codigo_item_pedido):

            # Lista os pedido existentes para inserir no item de pedido
            self.listar_pedidos(oracle, need_connect=True)
            codigo_pedido = str(input("Digite o número do Pedido: "))
            pedido = self.valida_pedido(oracle, codigo_pedido)
            if pedido == None:
                return None

            # Lista os produtos existentes para inserir no item de pedido
            self.listar_produtos(oracle, need_connect=True)
            codigo_produto = str(input("Digite o código do Produto: "))
            produto = self.valida_produto(oracle, codigo_produto)
            if produto == None:
                return None

            # Solicita a quantidade de itens do pedido para o produto selecionado
            quantidade = float(input(f"Informe a quantidade de itens do produto {produto.get_descricao()}: "))
            # Solicita o valor unitário do produto selecionado
            valor_unitario = float(input(f"Informe o valor unitário do produto {produto.get_descricao()}: "))

            # Atualiza o item de pedido existente
            oracle.write(f"update itens_pedido set quantidade = {quantidade}, valor_unitario = {valor_unitario}, codigo_pedido = {pedido.get_codigo_pedido()}, codigo_produto = {produto.get_codigo()} where codigo_item_pedido = {codigo_item_pedido}")
            # Recupera os dados do novo item de pedido criado transformando em um DataFrame
            df_item_pedido = oracle.sqlToDataFrame(f"select codigo_item_pedido, quantidade, valor_unitario, codigo_pedido, codigo_produto from itens_pedido where codigo_item_pedido = {codigo_item_pedido}")
            # Cria um novo objeto Item de Pedido
            item_pedido_atualizado = ItemPedido(df_item_pedido.codigo_item_pedido.values[0], df_item_pedido.quantidade.values[0], df_item_pedido.valor_unitario.values[0], pedido, produto)
            # Exibe os atributos do item de pedido
            print(item_pedido_atualizado.to_string())
            # Retorna o objeto pedido_atualizado para utilização posterior, caso necessário
            return item_pedido_atualizado
        else:
            print(f"O código {codigo_item_pedido} não existe.")
            return None

    def excluir_item_pedido(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do item de pedido a ser alterado
        codigo_item_pedido = int(input("Código do Item de Pedido que irá excluir: "))        

        # Verifica se o item de pedido existe na base de dados
        if not self.verifica_existencia_item_pedido(oracle, codigo_item_pedido):            
            # Recupera os dados do novo item de pedido criado transformando em um DataFrame
            df_item_pedido = oracle.sqlToDataFrame(f"select codigo_item_pedido, quantidade, valor_unitario, codigo_pedido, codigo_produto from itens_pedido where codigo_item_pedido = {codigo_item_pedido}")
            pedido = self.valida_pedido(oracle, df_item_pedido.codigo_pedido.values[0])
            produto = self.valida_produto(oracle, df_item_pedido.codigo_produto.values[0])
            
            opcao_excluir = input(f"Tem certeza que deseja excluir o item de pedido {codigo_item_pedido} [S ou N]: ")
            if opcao_excluir.lower() == "s":
                # Revome o produto da tabela
                oracle.write(f"delete from itens_pedido where codigo_item_pedido = {codigo_item_pedido}")                
                # Cria um novo objeto Item de Pedido para informar que foi removido
                item_pedido_excluido = ItemPedido(df_item_pedido.codigo_item_pedido.values[0], df_item_pedido.quantidade.values[0], df_item_pedido.valor_unitario.values[0], pedido, produto)
                # Exibe os atributos do produto excluído
                print("Item do Pedido Removido com Sucesso!")
                print(item_pedido_excluido.to_string())
        else:
            print(f"O código {codigo_item_pedido} não existe.")

    def verifica_existencia_item_pedido(self, oracle:OracleQueries, codigo:int=None) -> bool:
        # Recupera os dados do novo pedido criado transformando em um DataFrame
        df_pedido = oracle.sqlToDataFrame(f"select codigo_item_pedido, quantidade, valor_unitario, codigo_pedido, codigo_produto from itens_pedido where codigo_item_pedido = {codigo}")
        return df_pedido.empty

    def listar_pedidos(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select p.codigo_pedido
                    , p.data_pedido
                    , c.nome as cliente
                    , nvl(f.nome_fantasia, f.razao_social) as empresa
                    , i.codigo_item_pedido as item_pedido
                    , prd.descricao_produto as produto
                    , i.quantidade
                    , i.valor_unitario
                    , (i.quantidade * i.valor_unitario) as valor_total
                from pedidos p
                inner join clientes c
                on p.cpf = c.cpf
                inner join fornecedores f
                on p.cnpj = f.cnpj
                left join itens_pedido i
                on p.codigo_pedido = i.codigo_pedido
                left join produtos prd
                on i.codigo_produto = prd.codigo_produto
                order by c.nome
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def listar_produtos(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select prd.codigo_produto
                    , prd.descricao_produto 
                from produtos prd
                order by prd.descricao_produto 
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def valida_pedido(self, oracle:OracleQueries, codigo_pedido:int=None) -> Pedido:
        if self.ctrl_pedido.verifica_existencia_pedido(oracle, codigo_pedido):
            print(f"O pedido {codigo_pedido} informado não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_pedido = oracle.sqlToDataFrame(f"select codigo_pedido, data_pedido, cpf, cnpj from pedidos where codigo_pedido = {codigo_pedido}")
            cliente = self.ctrl_pedido.valida_cliente(oracle, df_pedido.cpf.values[0])
            fornecedor = self.ctrl_pedido.valida_fornecedor(oracle, df_pedido.cnpj.values[0])
            # Cria um novo objeto cliente
            pedido = Pedido(df_pedido.codigo_pedido.values[0], df_pedido.data_pedido.values[0], cliente, fornecedor)
            return pedido

    def valida_produto(self, oracle:OracleQueries, codigo_produto:int=None) -> Produto:
        if self.ctrl_produto.verifica_existencia_produto(oracle, codigo_produto):
            print(f"O produto {codigo_produto} informado não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_produto = oracle.sqlToDataFrame(f"select codigo_produto, descricao_produto from produtos where codigo_produto = {codigo_produto}")
            # Cria um novo objeto Produto
            produto = Produto(df_produto.codigo_produto.values[0], df_produto.descricao_produto.values[0])
            return produto