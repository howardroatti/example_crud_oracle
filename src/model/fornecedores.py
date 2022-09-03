class Fornecedor:
    def __init__(self, 
                 CNPJ:str=None, 
                 razao_social:str=None, 
                 nome_fantasia:str=None
                 ):
        self.set_CNPJ(CNPJ)
        self.set_razao_social(razao_social)
        self.set_nome_fantasia(nome_fantasia)

    def set_CNPJ(self, CNPJ:str):
        self.CNPJ = CNPJ

    def set_razao_social(self, razao_social:str):
        self.razao_social = razao_social

    def set_nome_fantasia(self, nome_fantasia:str):
        self.nome_fantasia = nome_fantasia

    def get_CNPJ(self) -> str:
        return self.CNPJ

    def get_razao_social(self) -> str:
        return self.razao_social

    def get_nome_fantasia(self) -> str:
        return self.nome_fantasia

    def to_string(self) -> str:
        return f"CNPJ: {self.get_CNPJ()} | Razão Social: {self.get_razao_social()} | Nome Fantasia: {self.get_nome_fantasia()}"