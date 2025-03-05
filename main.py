"""
Autoría: Sabela Fiaño García (sabela.fgarcia@udc.es) y Sara Gende Longueira (sara.gende@udc.es)
"""
import sys
import random
import pandas
from civilization import civilization
from unit import *

def recoleccion(civilization1, civilization2):
    lista = [civilization1, civilization2]
    print( "\n","PHASE 1: REPORT", "\n", "----------------------------------------")
    for civilizacion in lista:
        
        civilizacion.collect_resources()
        print("\n", f'{civilizacion.name} Resources: {civilizacion.resources}')
        for clase in ["Worker", "Archer", "Cavalry", "Infantry"]:
            print(clase, end= " : ")
            for individuo in civilizacion.units:
                if individuo._hp > 0:
                    if individuo._unit_type == clase : 
                        print(f"{individuo.name} ({individuo.hp}/{individuo.total_hp})", end=", ")
            print()


def produccion(civilization1, civilization2, turno):
    lista = [civilization1, civilization2]
    print( "\n","PHASE 2: REPORT", "\n", "----------------------------------------")
    for civilizacion in lista:
        
        if civilizacion.resources >= 30:
            print( "\n",f"{civilizacion.name} creates ", end=" ")
            if turno % 4 == 0:
                print (civilizacion.train_unit("Archer"))
            elif turno % 4 == 1:
                print(civilizacion.train_unit("Cavalry"))
            elif turno % 4 == 2:
                print(civilizacion.train_unit("Infantry"))
            if turno % 4 == 3:
                print(civilizacion.train_unit("Worker"))
            
        else:
            print(f"{civilizacion.name} cannot create any unit right now.")    
            
def selec_objetivo(atacante, civ_oponente):
    n_und_vivas = 0     
    n_work_vivos = 0
    
    for oponente in civ_oponente.units:
        if oponente.hp > 0:
            n_und_vivas += 1
            if oponente.unit_type != "Worker" :
                efecto = atacante.effectiveness(oponente)
                if efecto == 1 :
                    return(oponente)
                elif efecto == 0 :
                    return(oponente)
                elif efecto == -1 :
                   return(oponente)
            else:
                n_work_vivos += 1
    if n_und_vivas == n_work_vivos:            
        for oponente in civ_oponente.units:      
            if oponente.hp > 0 and oponente.unit_type == "Worker":
                return (oponente)
    return None
                
               

def batalla(civilizacion1, civilizacion2):
    lista = [civilizacion1, civilizacion2]
    print( "\n","PHASE 3: REPORT", "\n", "----------------------------------------")
    if civilizacion1.all_debilitated == True:
        return(f"{civilizacion1} está fuera de combate, el ganador es {civilizacion2} ")
    elif civilizacion2.all_debilitated == True:
        return(f"{civilizacion2} está fuera de combate, el ganador es {civilizacion1} ")
    
    n_medio_ind = min(len(civilizacion1.units), len(civilizacion2.units))
        
    for pos_atack in range(n_medio_ind):
        if  civilizacion1.units[pos_atack].unit_type != "Worker":
            individuo1 = civilizacion1.units[pos_atack]
            oponente_civ2 = selec_objetivo(individuo1, civilizacion2)
            if oponente_civ2.is_debilitated == False:
                daño = individuo1.attack(oponente_civ2)
                oponente_civ2.hp -= daño
            else:
                print(f"No se pudo seleccionar objetivo para el atacante {individuo1}. No se realizará ataque.")
            
        if  civilizacion2.units[pos_atack].unit_type != "Worker":            
            individuo2 = civilizacion2.units[pos_atack]
            oponente_civ1 = selec_objetivo(individuo2, civilizacion1)
            if oponente_civ1.is_debilitated == False:
                daño = individuo2.attack(oponente_civ1)
                oponente_civ1.hp -= daño
            else:
                print(f"No se pudo seleccionar objetivo para el atacante {individuo2}. No se realizará ataque.")

    #falta atacar con worker y atacar tropas auxiliares 
    
    

if __name__ == "__main__":

    # Leer el archivo de configuración desde la línea de comandos o usar el predeterminado
    config_file = sys.argv[1] if len(sys.argv) > 1 else "battle0.txt"

    # Intentar abrir el archivo especificado
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: El archivo '{config_file}' no existe.", file=sys.stderr)
        sys.exit(1)

    # Resto del código de la simulación...
    print(f"Leyendo configuración desde: {config_file}")

    civ1_data = lines[0].split(":")
    civ1_name = civ1_data[0]
    resources1 = int(civ1_data[1])
    
    civ2_data = lines[1].split(":")
    civ2_name = civ2_data[0]
    resources2 = int(civ2_data[1])
    
    turns_line = lines[2]
    parts = turns_line.replace(":", ",").split(",")
    turns = int(parts[1].strip())

    # Leer la cantidad inicial de cada tipo de unidad
    workers_line = lines[3]
    workers = int(workers_line.split(":")[1].strip())


    archers_line = lines[4]
    archers = int(archers_line.split(":")[1].strip())

    cavalry_line = lines[5]
    cavalry = int(cavalry_line.split(":")[1].strip())

    infantry_line = lines[6]
    infantry = int(infantry_line.split(":")[1].strip())

    # Crear instancias de civilización
    civ1 = civilization(civ1_name, resources1)    
    civ2 = civilization(civ2_name, resources2)
    
    for i in range (workers):
        civ1.train_unit("Worker")
        civ2.train_unit("Worker")
    
    for i in range (archers):
        civ1.train_unit("Archer")
        civ2.train_unit("Archer")
    
    for i in range (cavalry):
        civ1.train_unit("Cavalry")
        civ2.train_unit("Cavalry")
    
    for i in range (infantry):
        civ1.train_unit("Infantry")
        civ2.train_unit("Infantry") 
        
    print (f"[TODO: Create civilization: {civ1_name} with {resources1} initial resources]")
    print (f"[TODO: Create civilization: {civ2_name} with {resources2} initial resources]")

    # Crear unidades según la cantidad especificada en el fichero de batalla escogido
    print (f"[TODO: Create {workers} workers for {civ1_name}]")
    print (f"[TODO: Create {workers} workers for {civ2_name}]")
    print (f"[TODO: Create {archers} archers for {civ1_name}]")
    print (f"[TODO: Create {archers} archers for {civ2_name}]")
    print (f"[TODO: Create {cavalry} cavalry for {civ1_name}]")
    print (f"[TODO: Create {cavalry} cavalry for {civ2_name}]")
    print (f"[TODO: Create {infantry} infantry for {civ1_name}]")
    print (f"[TODO: Create {infantry} infantry for {civ2_name}]")
    
    #empieza la batalla turno 1 recursos
    for turno in range (1,turns):
        print("\n", "****************************************************", "\n", "TURNO_",turno , "\n", "****************************************************" )
        recoleccion(civ1, civ2)
        produccion(civ1, civ2, turno)
        batalla(civ1, civ2)