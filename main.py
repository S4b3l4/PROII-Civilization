"""
Autoría: Sabela Fiaño García (sabela.fgarcia@udc.es) y Sara Gende Longueira (sara.gende@udc.es)
"""
import sys
import random
import pandas
from civilization import civilization
from unit import Archer, Infantry, Cavalry, Worker

def recoleccion(civilization1, civilization2):
    """Esta función llama a la funcion collect_resources e imprime las unidades que se crean con su hp.
    Parameters
    ----------
    civilization1 : instancia
    Llama a la clase civilización con sus atributos
    civilization2 : instancia
    Llama a la clase civilización con sus atributos
    Returns
    -------
    string
    Devuelve una cadena de texto con la información de cada unidad creada.
    """
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
    """Esta función llama a la funcion train_unit para crear unidades dependiendo del turno
    Parameters
    ----------
    civilization1 : instancia
    Llama a la clase civilización con sus atributos
    civilization2 : instancia
    Llama a la clase civilización con sus atributos
    turno: int
    A través de un bucle recorre los valores de 1 hasta el valor de turns.
    Returns
    -------
    string
    Devuelve una cadena de texto con la información de cada unidad creada.
    """
    lista = [civilization1, civilization2]
    print( "\n","PHASE 2: REPORT", "\n", "----------------------------------------")
    for civilizacion in lista:
        
        if civilizacion.resources >= 30:
            print(f"{civilizacion.name} creates ", end="")
            if turno % 4 == 0:
                print(civilizacion.train_unit("Archer"))
            elif turno % 4 == 1:
                print(civilizacion.train_unit("Cavalry"))
            elif turno % 4 == 2:
                print(civilizacion.train_unit("Infantry"))
            if turno % 4 == 3:
                print(civilizacion.train_unit("Worker"))
            
        else:
            print(f"{civilizacion.name} cannot create any unit right now.")    
            
def selec_objetivo(atacante, civ_oponente):
    """Esta función selecciona el oponente de cada civilización.
    Parameters
    ----------
    atacante : instancia
    Representa la unidad de la civilizacion que va atacar.
    civ_oponente : instancia
    Representa la civilizacion a la que se va atacar.
    Returns
    -------
    oponente : instancia o None
    Devuelve el oponente que selecciona el atacante o nada si no encuentra oponente.
    """
    n_und_vivas = 0     
    n_work_vivos = 0
    
    for oponente in civ_oponente.units:
        if oponente.hp > 0:
            n_und_vivas += 1
            if oponente.unit_type != "Worker" :
                efecto = atacante.effectiveness(oponente)
                if efecto == 1 or efecto == 0 or efecto == -1:
                    return oponente
            else:
                n_work_vivos += 1
                
    if n_und_vivas == n_work_vivos:            
        for oponente in civ_oponente.units:      
            if oponente.hp > 0 and oponente.unit_type == "Worker":
                return oponente
    return None
                
def vivas_no_workers(civilizacion):
    """Esta función comprueba si quedan unidades vivas que no sean worker.
    Parameters
    ----------
    civilizacion : instancia
    Contiene los atributos de la civilizacion.
    Returns
    -------
    bool
    Devuelve True si quedan unidades vivas diferentes de worker y False en caso contrario.
    """
    for unidad in civilizacion.units:
        if unidad.hp > 0 and unidad.unit_type != 'Worker':
            return True  
    return False              

def batalla(civilizacion1, civilizacion2): 
    
    """Esta función desarrolla la fase de batalla entre las dos civilizaciones.
    Parameters
    ----------
    civilization1 : instancia
    Llama a la clase civilizacion con los atributos de la civilizacion 1
    civilization2 : instancia
    Llama a la clase civilizacion con los atributos de la civilizacion 2
    Returns
    -------
    string
    Devuelve una cadena de texto que indica el estado de la batalla, las unidades que quedan, quien ataca y si gana alguien.
    """
    
    print( "\n","PHASE 3: REPORT", "\n", "----------------------------------------")
    n_medio_ind = min(len(civilizacion1.units), len(civilizacion2.units))
        
    for pos_atack in range(n_medio_ind):
        #Ataque civ1
        if  civilizacion1.units[pos_atack].unit_type != "Worker" and civilizacion1.units[pos_atack].hp > 0:
            individuo1 = civilizacion1.units[pos_atack]
            oponente_civ2 = selec_objetivo(individuo1, civilizacion2)
            
            if oponente_civ2 and not oponente_civ2.is_debilitated():
                daño1 = individuo1.attack(oponente_civ2)
                oponente_civ2.hp -= daño1
                print(f"{civilizacion1.name} - {individuo1.name} attacks {civilizacion2.name} - {oponente_civ2.name} with damage {daño1} (hp={oponente_civ2.hp}/{oponente_civ2.total_hp}).")
            else:
                print(f"No se seleccionó objetivo para el atacante {individuo1.name} de la civilización {civilizacion1.name}. No se realizará ataque.")
        
        #Ataque civ2
        if  civilizacion2.units[pos_atack].unit_type != "Worker" and civilizacion1.units[pos_atack].hp > 0:            
            individuo2 = civilizacion2.units[pos_atack]
            oponente_civ1 = selec_objetivo(individuo2, civilizacion1)
            
            if oponente_civ1 and not oponente_civ1.is_debilitated():
                daño2 = individuo2.attack(oponente_civ1)
                oponente_civ1.hp -= daño2
                print(f"{civilizacion2.name} - {individuo2.name} attacks {civilizacion1.name} - {oponente_civ1.name} with damage {daño2} (hp={oponente_civ1.hp}/{oponente_civ1.total_hp}).")
            else:
                print(f"No se seleccionó objetivo para el atacante {individuo2.name} de la civilización {civilizacion2.name}. No se realizará ataque.")
     
    #Ataque de las unidades que aun quedan vivas
    if len(civilizacion1.units) > len(civilizacion2.units):
        for i in range(len(civilizacion2.units), len(civilizacion1.units)):
            atacante = civilizacion1.units[i]
            obj = None
            for j in civilizacion2.units:
                if j.hp > 0:
                    obj = j
                    break
                if obj:
                    daño = atacante.attack(obj)
                    print(f"{civilizacion1.name} - {atacante.name} attacks {civilizacion2.name} - {obj.name} with damage {daño} (hp={obj.hp}/{obj.total_hp}).")

    elif len(civilizacion2.units) > len(civilizacion1.units):
        for i in range(len(civilizacion1.units), len(civilizacion2.units)):
            atacante = civilizacion2.units[i]
            obj = None
            for j in civilizacion1.units:
                if j.hp > 0:
                    obj = j
                    break
                if obj:
                    daño = atacante.attack(obj)
                    print(f"{civilizacion2.name} - {atacante.name} attacks {civilizacion1.name} - {obj.name} with damage {daño} (hp={obj.hp}/{obj.total_hp}).")


    #Atque Worker
    if not vivas_no_workers(civilizacion1) and not vivas_no_workers(civilizacion2):
        for worker1 in civilizacion1.units:
            if worker1.unit_type == 'Worker' and worker1.hp > 0:
                obj_civ2 = selec_objetivo(worker1, civilizacion2)
            
                if obj_civ2 and not obj_civ2.is_debilitated():
                    daño_worker1 = worker1.attack(obj_civ2)
                    obj_civ2.hp -= daño_worker1
                    print(f"{civilizacion1.name} - {worker1.name} attacks {civilizacion2.name} - {obj_civ2.name} with damage {daño_worker1} (hp={obj_civ2.hp}/{obj_civ2.total_hp}).")
                else:
                    print(f"No se seleccionó objetivo para el atacante {worker1.name} de la civilización {civilizacion1.name}. No se realizará ataque.")
                
    if not vivas_no_workers(civilizacion1) and not vivas_no_workers(civilizacion2):
        for worker2 in civilizacion2.units:
            if worker2.unit_type == 'Worker' and worker2.hp > 0:
                obj_civ1 = selec_objetivo(worker2, civilizacion1)
                
                if obj_civ1 and not obj_civ1.is_debilitated():
                    daño_worker2 = worker2.attack(obj_civ1)
                    obj_civ1.hp -= daño_worker2
                    print(f"{civilizacion2.name} - {worker2.name} attacks {civilizacion1.name} - {obj_civ1.name} with damage {daño_worker2} (hp={obj_civ1.hp}/{obj_civ1.total_hp}).")
    
                else:
                    print(f"No se seleccionó objetivo para el atacante {worker2.name} de la civilización {civilizacion2.name}. No se realizará ataque.")
        
    #Comprobar si hay alguna civilización que se queda sin unidades con vida.
    if civilizacion1.all_debilitated():
        return(f"{civilizacion1.name} está fuera de combate, el ganador es {civilizacion2.name} ")
    elif civilizacion2.all_debilitated():
        return(f"{civilizacion2.name} está fuera de combate, el ganador es {civilizacion1.name} ")
    else:
        return 'La batalla continúa.'

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