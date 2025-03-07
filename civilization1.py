"""
Autoría: Sabela Fiaño García (sabela.fgarcia@udc.es) y Sara Gende Longueira (sara.gende@udc.es)
"""
from unit import Archer, Cavalry, Infantry, Worker

class civilization():
    """Definimos las características básicas de la clase civilization.
    
    Attributes
    ----------
    name : str
    Nombre de la civilización
    resouces : int
    Numero de unidades de recursos de la civilización
    units : list
    Lista con todas la unidades de la civilización.
    units_count : dict
    Diccionario que almacena el numero de unidades de cada clase
    
    Methods
    -------
    train_unit(self, new_unit_type:str):
    Función para crear las unidades dependiendo de los recursos disponibles.
    def collect_resources(self):
    Función para recolectar recursos cada vez que se invoque.
    def all_debilitated(self):
    Función que indica si una civilización tiene todas sus unidades sin vida o si aún queda alguna.
    """
    
    def __init__(self, name:str, resources:int):
        """Asigna atributos al objeto civilization
        
        Parameters
        ----------
        name : str
        Indica el nombre de la civilización.
        resources : int
        Indica los recursos que tiene la civilización.
        
        Returns
        -------
        None.
        """
        self._name = name
        self._resources = resources
        self._units = [] #se define en la subclase
        self._unit_count = {"Archer" : 0, "Worker" : 0, "Cavalry" : 0, "Infantry":0 }
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError('El nombre no puede ser una cadena de texto vacía.')

    @property
    def resources(self):
        return self._resources
    @resources.setter
    def resources(self, value):
        if isinstance(value, int) and value >= 0:
            self._resources = value
        else:
            raise ValueError('Debe ser un número entero y positivo.')
        
    @property
    def units(self):
        return self._units
    @units.setter
    def units(self, value):
        if isinstance(value, list):
            self._units = value
        else:
            raise ValueError('Debe ser una lista.')
        
    @property
    def units_count(self):
        return self._unit_count
    @units_count.setter
    def units_count(self, value):
        if isinstance(value, dict):
            self._unit_count = value
        else:
            raise ValueError('Debe ser un diccionario.')

    def train_unit(self, new_unit_type:str):
        """Función para crear las unidades dependiendo de los recursos disponibles.
        
        Parameters
        ----------
        new_unit_type : str
        La unidad que se quiere crear. Para cada una se comprobará que haya los recursos suficientes.
        
        Returns
        --------
        None
        Unit
        Devuelve la nueva unidad creada tras haberla añadida a la lista de unidades.
        """
        if new_unit_type == "Worker" and self._resources >= 30:
            self._unit_count ["Worker"]+= 1
            name = f'Worker_{self._unit_count["Worker"]}'
            new_unit = Worker(name, 1, 0, 5, 5)
            self._resources -= 30
            self._units.append(new_unit)
            
        elif self.resources >= 60:
            if new_unit_type == "Archer":
                self._unit_count ["Archer"]+= 1
                name = f'Archer_{self._unit_count["Archer"]}'
                new_unit = Archer(name, 7, 2, 15, 15, 3)
                self._resources -= 60
                self._units.append(new_unit)
               
            elif new_unit_type == "Cavalry":
                self._unit_count ["Cavalry"]+= 1
                name = f'Cavalry_{self._unit_count["Cavalry"]}'
                new_unit = Cavalry(name, 5, 2, 25, 25, 5) 
                self._resources -= 60
                self._units.append(new_unit)
               
            elif new_unit_type == "Infantry":
                self._unit_count ["Infantry"]+= 1
                name = f'Infantry_{self._unit_count["Infantry"]}'
                new_unit = Infantry(name, 3, 2, 25, 25, 3) 
                self._resources -= 60
                self._units.append(new_unit)
        else:
            return None
        return new_unit
        
    def collect_resources(self)-> None:
        """ Permite que la civilización obtenga recursos cuando se llama a la función collect_resources.
        
        Parameters
        ----------
        No tiene parámetros propios, solo hace referencia a la clase.
        
        Returns
        --------
        str
        Devuelve la cantidad de recursos que recolecta el worker al llamar a la función collect().
        """
        for unidad in self._units:
            if unidad.unit_type == "Worker":
                self._resources += unidad.collect()
        return self._resources
    
    def all_debilitated(self)-> bool:
        """ indica si la civilización está fuera de combate (True) o todavía en batalla (False)
        
        Parameters
        ----------
        No tiene parámetros propios, solo hace referencia a la clase.
        
        Returns
        --------
        bool
        Devuelve True si todas las unidades están sin vida, en caso contrario devuelve False.
        """
        live = 0
        for units in self._units:
            if units._hp == 0:
                live += 1
        if live == len(self._units):
            return True
        else:
            return False
