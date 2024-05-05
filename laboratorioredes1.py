class Dispositivo:
    def __init__(self, puerto):
        self.puerto = puerto

    def topologia_malla(self,n): #Duplex
        cables = n* (n-1)/2
        
        return cables
    
    def puertos_e_s(self,n): #simplex
        puerto = n -1
        
        return puerto


#d = Dispositivo(6)
#cantidad_cables = d.topologia_malla(6)
#print("Cantidad de cables necesarios:", cantidad_cables)

d = Dispositivo(6)
cantidad_puertos = d.puertos_e_s(6)
print("cantidad de puertos :",cantidad_puertos)