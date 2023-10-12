class Veiculo:
    def __init__(self, 
                 idCarro:int=None,
                 modelo:str=None,
                 cor:str=None,
                 anoCarro:int=None,
                 chassiCarro:int=None,
                 tipoCambio:str=None,
                 fabricante:str=None,
                 ):
        self.set_idCarro(idCarro)
        self.set_modelo(modelo)
        self.set_cor(cor)
        self.set_anoCarro(anoCarro)
        self.set_chassiCarro(chassiCarro)
        self.set_tipoCambio(tipoCambio)
        self.set_fabricante(fabricante)

#Getters
    def get_idCarro(self) -> int:
        return self.get_idCarro

    def get_modelo(self) -> str:
        return self.get_modelo
    
    def get_cor(self) -> str:
        return self.get_cor
    
    def get_anoCarro(self) -> int:
        return self.get_anoCarro
    
    def get_chassiCarro(self) -> int:
        return self.get_chassiCarro
    
    def get_tipoCambio(self) -> str:
        return self.get_tipoCambio
    
    def get_fabricante(self) -> str:
        return self.get_fabricante

#Setters

    def set_idCarro(self, idCarro:int):
        self.idCarro = idCarro

    def set_modelo(self, modelo:str):
        self.modelo = modelo
    
    def set_cor(self, cor:str):
        self.cor = cor

    def set_anoCarro(self, anoCarro:str):
        self.anoCarro = anoCarro

    def set_chassiCarro(self, chassiCarro:str):
        self.chassiCarro = chassiCarro
    
    def set_tipoCambio(self, tipoCambio:str):
        self.tipoCambio = tipoCambio

    def set_fabricante(self, fabricante:str):
        self.fabricante = fabricante    

    

    def to_string(self) -> str:
        return f"idCarro: {self.get_idCarro()} | modelo: {self.get_modelo()}| cor: {self.get_cor()} | anoCarro: {self.get_anoCarro()} | chassiCarro: {self.get_chassiCarro()} | tipoCambio: {self.get_tipoCambio()} | fabricante: {self.get_fabricante()}"