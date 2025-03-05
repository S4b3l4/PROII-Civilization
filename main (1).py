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
    for civilizacion in lista:
        civilizacion.collect_resources
        print({civilization.name}, " Resources: ", {civilization.resources})
        for clase in ["Worker", "Archer", "Cavalry", "Infantry"]:
            print(clase, end= " : ")
            for individuo in civilizacion.units:
                if individuo._hp > 0:
                    if individuo._unit_type == clase : 
                        print(individuo._name, " (", individuo._hp, "/", individuo._total_hp,")", end= ", ")
                
 # def production(civilization1, civilization2):
    

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

    recoleccion(civ1, civ2)
