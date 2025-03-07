"""
Autoría: Sabela Fiaño García (sabela.fgarcia@udc.es) y Sara Gende Longueira (sara.gende@udc.es)
"""
import sys
import random
import pandas
from civilization import civilization
from unit import Archer, Cavalry, Infantry, Worker

def estadisticas(civilization1, civilization2):
    """Esta función calcula el daño medio de cada unidad, de cada civilizacion y de cada unidad sobre cada civilizacion.
    
    Parameters
    ----------
    civilization1 : instancia
    Llama a la clase civilizacion con los atributos de la civilizacion 1
    civilization2 : instancia
    Llama a la clase civilizacion con los atributos de la civilizacion 2
    
    Returns
    -------
    DataFrame
    Devuelve un DataFrame con los datos del daño medio.
    """
    #Creamos dos listas, una con la información de las civilizaciones y otra con la de las unidades.
    units_info = []
    for _ in range(100):
        units_info.append([random.choice(['Archer', 'Cavalry', 'Infantry', 'Worker']),
                               random.choice(['civ1', 'civ2']),
                               random.randint(1,5),
                               random.choice(['civ1', 'civ2'])])

    #Creamos el dataframe
    data = pandas.DataFrame(units_info, columns=['unit_type', 'civilization', 'damage', 'target'])

    #Agrupamos por civilizacion y calculamos el daño medio por cada una
    group_col = "civilization"
    target_col = "damage"
    data_damage = data.groupby(group_col).agg({target_col :["mean"]})
    #Imprimimos los resultados
    print ('\n', "###################################")
    print ("   damage grouped by civilization      ")
    print ("###################################\n")
    print (data_damage)

    #Agrupamos por unidad y calculamos el daño medio de cada uña
    group_col = "unit_type"
    target_col = "damage"
    data_damage = data.groupby(group_col).agg({target_col :["mean"]})
    print ('\n', "###################################")
    print ("   damage grouped by unit_type      ")
    print ("###################################\n")
    print (data_damage)

    #We can group data by multiple columns, e.g., by job and sex
    group_col = ["unit_type","target"]
    target_col = "damage"
    data_damage = data.groupby(group_col).agg({target_col :["mean"]})
    print ('\n', "###################################")
    print (" damage grouped by (unit_type, target)  ")
    print ("###################################\n")
    print (data_damage)
        
def recoleccion(civilization1, civilization2):
    """Esta función llama a la funcion collect_resources e imprime las unidades que se crean con su hp.
   
    Parameters
    ----------
    civilization1 : instancia
    Llama a la clase civilizacion con los atributos de la civilizacion 1
    civilization2 : instancia
    Llama a la clase civilizacion con los atributos de la civilizacion 2
    
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
                if individuo.hp > 0:
                    if individuo.unit_type == clase : 
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
            elif turno % 4 == 3:
                print(civilizacion.train_unit("Worker"))
            
        else:
            print(f"{civilizacion.name} cannot create any unit right now.")    
            
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
    efecto_oponente = -1
    oponente_final = None
    if atacante.hp > 0:
        for oponente in civ_oponente.units: 
            #oponentes Worker
            if vivas_no_workers(civ_oponente) == False :                
                if oponente.hp > 0 and oponente.unit_type == "Worker":
                        return oponente 
            #oponentes no workers
            else:
                if oponente.hp > 0 and oponente.unit_type != "Worker" :
                    efecto = atacante.effectiveness(oponente)
                    if efecto > efecto_oponente:
                        efecto_oponente = efecto 
                        oponente_final = oponente
        
    return oponente_final                                               

def ha_ganado (civilizacion1, civilizacion2):
    """Esta función comprueba si alguna civilización ha ganado.
    
    Parameters
    ----------
    civilizacion1 : instancia
    Contiene los atributos de la civilizacion.
   
    Returns
    -------
    bool
    Devuelve True si alguna civilización ha ganado y False en caso contrario.
    """
    if civilizacion1.all_debilitated() or  civilizacion2.all_debilitated():
        return True
    else:
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
    n_medio_und = min(len(civilizacion1.units), len(civilizacion2.units))
    n_max_und =  max(len(civilizacion1.units), len(civilizacion2.units))
    
    #Comprobar si hay alguna civilización se queda sin unidades con vida.
    if ha_ganado(civilizacion1, civilizacion2) == False:
        #segimos el ataque con nº de unidades igualitario
        for pos_atack in range(n_medio_und):
            
            #civilicación 1
            atacante1 = civilizacion1.units[pos_atack]
            #atacante Worker en civilización 1
            if vivas_no_workers(civilizacion1) == False :  
                if atacante1.hp > 0 and atacante1.unit_type == "Worker":
                    oponente_civ2 = selec_objetivo(atacante1, civilizacion2)
                    daño1 = atacante1.attack(oponente_civ2)
                    oponente_civ2.hp -= daño1
                    print(f"{civilizacion1.name} - {atacante1.name} attacks {civilizacion2.name} - {oponente_civ2.name} with damage {daño1} (hp={oponente_civ2.hp}/{oponente_civ2.total_hp}).")
            #atacantes no workers en civilización 1
            else:
                if atacante1.hp > 0 and atacante1.unit_type != "Worker":
                    oponente_civ2 = selec_objetivo(atacante1, civilizacion2)
                    daño1 = atacante1.attack(oponente_civ2)
                    oponente_civ2.hp -= daño1
                    print(f"{civilizacion1.name} - {atacante1.name} attacks {civilizacion2.name} - {oponente_civ2.name} with damage {daño1} (hp={oponente_civ2.hp}/{oponente_civ2.total_hp}).")
                    
            #civilicación 2
            atacante2 = civilizacion2.units[pos_atack]
            #atacante Worker en civilización 2
            if vivas_no_workers(civilizacion2) == False :  
                if atacante2.hp > 0 and atacante2.unit_type == "Worker":
                    oponente_civ1 = selec_objetivo(atacante2, civilizacion1)
                    daño2 = atacante2.attack(oponente_civ1)
                    oponente_civ1.hp -= daño2
                    print(f"{civilizacion2.name} - {atacante2.name} attacks {civilizacion1.name} - {oponente_civ1.name} with damage {daño2} (hp={oponente_civ1.hp}/{oponente_civ1.total_hp}).")
            #atacantes no workers en civilización 2
            else:
                if atacante2.hp > 0 and atacante2.unit_type != "Worker":
                    oponente_civ1 = selec_objetivo(atacante2, civilizacion1)
                    daño2 = atacante2.attack(oponente_civ1)
                    oponente_civ1.hp -= daño2
                    print(f"{civilizacion2.name} - {atacante2.name} attacks {civilizacion1.name} - {oponente_civ1.name} with damage {daño2} (hp={oponente_civ1.hp}/{oponente_civ1.total_hp}).")         
           
        #Ataque de las unidades restantes de la civilización con más unidades
        if len(civilizacion1.units) != len(civilizacion2.units):
            civilizacion_mayor = max(civilizacion1, civilizacion2)
            civilizacion_menor = min(civilizacion1, civilizacion2)
            print("#End of alternating sequence: One civilization has no more attackers left")
            print(f"The remaining units of the stronger civilization {civilizacion_mayor.name} now attack in sequence.")
          
            for pos_atack in range(n_medio_und, n_max_und):
                atacante = civilizacion_mayor.units[pos_atack]
                #atacante Worker en civilizacion_mayor
                if vivas_no_workers(civilizacion_mayor) == False :  
                    if atacante.hp > 0 and atacante.unit_type == "Worker":
                        oponente = selec_objetivo(atacante, civilizacion_menor)
                        daño = atacante.attack(oponente)
                        oponente.hp -= daño
                        print(f"{civilizacion_mayor.name} - {atacante.name} attacks {civilizacion_menor.name} - {oponente.name} with damage {daño} (hp={oponente.hp}/{oponente.total_hp}).")
                #atacantes no workers en civilización 1
                else:
                    if atacante.hp > 0 and atacante.unit_type != "Worker":
                        oponente = selec_objetivo(atacante, civilizacion_menor)
                        daño = atacante.attack(oponente)
                        oponente.hp -= daño
                        print(f"{civilizacion_mayor.name} - {atacante.name} attacks {civilizacion_menor.name} - {oponente.name} with damage {daño} (hp={oponente.hp}/{oponente.total_hp}).")
    else:
        return ("El juego ha finalizado")

        

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
    #calculamos las estadísticas llamando a la función
    estadisticas(civ1, civ2)