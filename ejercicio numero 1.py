"""Info: Puntaje de jugador;
Datos: llego 1 FR llego 3
        llego 2FA FAm 
Estrategia: FR *** 3 + 2 * FA - FAm **2"""

#aca estas las lineas de Fichas Rojas;
FR = int(input("Ingresa cantidad fichas rojas:"))


#aca estan las lineas de Fichas Azules;
FA = int(input("Ingresa cantidad fichas azules:"))


#aca van las fichas de color amarillo;
FAm = int(input("cantidad de fichas amarrilas:"))


#aca va la expresion aricmetica; 
puntaje = FR**3+2*FA-FAm**2
print("tu puntaje total es :", puntaje)