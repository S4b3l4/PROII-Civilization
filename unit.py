"""
Autoría: Sabela Fiaño García (sabela.fgarcia@udc.es) y Sara Gende Longueira (sara.gende@udc.es)
"""
from abc import ABC, abstractmethod
import math

class Unit(ABC):
    """ definimos las características básicas de la clase abstracta Unit que serán comunes a todas las subunidades.
    Attributes
    ----------
    name : str
    Nombre de la unidad.
    strength : int
    Unidades de fuerza basica de la uniad, las unidades de ataque se calculan con la strength y la defense.
    defense : int
    Unidades de defensa, se resta al total del daño antes de devolver el número de unidades de daño causadas.
    hp : int
    Puntos de salud varia a lo largo del juego pero nunca aumenta, siempre inferior o igual a total_hp.
    total_hp : int
    Puntos totales de vida, no varia a lo largo de la partida.
    -------
    effectiveness(self, opponent:'Unit') :
    Define la relación entre las subclases en base a su interacción en batalla -1 devil, 0 neutro y 1 efectivo.
    attack(self, opponent:'Unit') :
    Daño básico de 1 unidad, se modifica dependiendo de la clase.
    is_debilitated(self) :
    Indica si la unidad está fuera de combate, con unidades de hp igual a 0 (True) o todavía en batalla (False)
    """
    
    def __init__(self, name:str, strength:int, defense:int, hp:int, total_hp:int):
        """Asigna atributos al objeto.
        Parameters
        ----------
        name : str
        Nombre de la unidad.
        strength : int
        Unidades de fuerza basica de la uniad, las unidades de ataque se calculan con la strength y la defense.
        defense : int
        Unidades de defensa, se resta al total del daño antes de devolver el número de unidades de daño causadas.
        hp : int
        Puntos de salud varia a lo largo del juego pero nunca aumenta, siempre inferior o igual a total_hp.
        total_hp : int
        Puntos totales de vida, no varia a lo largo de la partida.
        Returns
        -------
        None.
        """
        self._name = name
        self._strength = strength
        self._defense = defense
        self._hp = hp
        self._total_hp = total_hp
  
    def __str__(self):
        """Definimos la cadena que se muestra por pantalla cuando se llama a print con el objeto como argumento.
        Parameters
        ----------
        self : Unit
        Objeto sobre el que queremos saber información.  
        Returns
        --------
        str
        Resultado {name} ({unit_type}) Stats: ATT: {strength}, DEF: {defense}, HP: {hp/total_hp}
        """
        return f'nombre: {self._name}, unit:{self._unit_type}, ATT: {self._strength}, DEF: {self._defense}, HP: {self._hp}/{self._total_hp}'
      
    @abstractmethod
    def effectiveness(self, opponent:'Unit')-> int:
        """Define la relación entre las subclases en base a su interacción en batalla.
        Parameters
        ----------
        self : Unit
        Objeto que queremos saber si tiene algun efecto sobre el oponente.
        opponent : Unit
        Objeto oponente del cual necesitamos saber su unit_tipe.
        Returns
        -------
        int
        Devuelve -1 si es débil ante el oponente ,0 si es neutro contra el oponente o 1 si es efectivo ante el oponente.
        """
        pass 
    
    def attack(self, opponent:'Unit')-> int:
        """Daño básico de 1 unidad, se modifica dependiendo de la clase.
        Parameters
        ----------
        self : Unit
        Objeto que queremos que ataque.
        opponent : Unit
        Objeto oponente del cual necesitamos saber su defensa.
        Returns
        -------
        int
        Devuelve las unidades de ataque.
        """
        return 1
    
    def is_debilitated(self)-> bool:
        """Indica si la unidad está fuera de combate, con unidades de hp igual a 0 (True) o todavía en batalla (False).
        Parameters
        ----------
        self : Unit
        Objeto que queremos saber si está debilitado.
        Returns
        -------
        bool
        True si está debilitado, False si sigue en pie para la batalla.
        """
        return self._hp <= 0

    
    """
    Estas tres funciones son comunes a todos los personajes.
    Con las etiquetas @property y @setter permitimos el acceso a los atributos de cada clase.
    """

    
    @property
    def name(self): #definimos como "leer" el nombre
        return self._name
    @name.setter
    def name(self, name): # definimos como insertar nombre con precondiciones = str y len>0
           if isinstance(name, str) and len(name) > 0:
               self._name = name
           else:
               raise ValueError('El nombre no puede ser una cadena de texto vacía.')

    @property
    def strength(self):
        return self._strength
    @strength.setter
    def strength(self, value):
        if isinstance(value, int):
            self._strength = max(0, value)
        else:
            raise ValueError('Debe ser un número entero y positivo.')
       
    @property
    def defense(self):
        return self._defense
    @defense.setter
    def defense(self, value):
        if isinstance(value, int):
            self._defense = max(0, value)
        else:
            raise ValueError("Defense debe ser un número entero.")
        
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, value):
        if isinstance(value, int):
            self._hp = max(0, value)
        else:
            raise ValueError("HP debe ser un número entero.")
        
    @property
    def total_hp(self):
        return self._total_hp
    @total_hp.setter
    def total_hp(self, value):
        if isinstance(value, int):
            self._total_hp = max(0, value)
        else:
            raise ValueError("Total_hp debe ser un número entero.")
        
    @property
    def unit_type(self):
        return self._unit_type
    @unit_type.setter
    def unit_type(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._unit_type = value
        else:
            raise ValueError("El tipo de unidad debe ser una cadena de texto no vacía.")


class Archer(Unit):
    """ definimos las características básicas de la clase Archer.
    Attributes
    ----------
    Unit
    Al llamar a la superclase ya contiene todos sus atributos
    -------
    effectiveness(self, opponent:'Unit') :
    Define la relación entre las subclases en base a su interacción en batalla -1 devil, 0 neutro y 1 efectivo.
    attack(self, opponent:'Unit') :
    Daño básico de 1 unidad, se modifica dependiendo de la clase.
    is_debilitated(self) :
    Indica si la unidad está fuera de combate, con unidades de hp igual a 0 (True) o todavía en batalla (False)
    """
    
    def __init__(self, name:str, strength:int, defense:int, hp:int, total_hp:int, arrows:int):
        """ Asigna atributos al objeto Archer
        Parameters
        ----------
        self : Unit
        Objeto que referencia a Archer
        name : str
        Nombre de la unidad.
        strength : int
        Unidades de fuerza basica de la uniad, las unidades de ataque se calculan con la strength y la defense.
        defense : int
        Unidades de defensa, se resta al total del daño antes de devolver el número de unidades de daño causadas.
        hp : int
        Puntos de salud varia a lo largo del juego pero nunca aumenta, siempre inferior o igual a total_hp.
        total_hp : int
        Puntos totales de vida, no varia a lo largo de la partida.
        arrows: int
        Total de flechas que tiene.
        Returns
        -------
        None
        """
        self._arrows = arrows
        self._unit_type = 'Archer'
        'definimos el nº de flechas a la hora de la batalla para más flexibilidad del juego'
        super().__init__(name, strength, defense, hp, total_hp) #super llama a la superclase.
        
    def attack(self, opponent:'Unit') -> int:
         """Daño que se realiza al oponente, se modifica dependiendo de la clase.
         Parameters
         ----------
         self : Unit
         Objeto que queremos que ataque.
         opponent : Unit
         Objeto oponente del cual necesitamos saber su defensa.
         Returns
         -------
         int
         Devuelve las unidades de ataque.
         """
         if opponent._hp > 0:
            factor = 1
            if opponent._unit_type == 'Cavalry':
                factor = 1.5
            elif opponent._unit_type == 'Infantry':
                factor = 0.5
           
            n = math.floor(max(1, (factor*self._strength) - opponent._defense))
            """ si hay flechas el ataque se realiza de forma normal"""
            if self._arrows > 0:
                self._arrows -= 1
                if opponent._hp - n <= 0:
                    n = opponent._hp
            else:
                """si no hay flechas el ataque solo será una 1 de daño"""
                n = 1
                if opponent._hp - n <= 0:
                    n = opponent._hp
            opponent._hp = max(0, opponent._hp - n)
            return n
         else:
             """si el oponente no tiene vida no podrá ser atacado"""
             return 'Oponente no disponible'
    
    def effectiveness(self, opponent:'Unit') -> int:
        """Indica la efectividad del ataque dependiendo de la unidad.
        Parameters
        ----------
        self : Unit
        Objeto que queremos saber si está debilitado.
        Returns
        -------
        int
        1 si el oponente es Cavalry, -1 si es Infantry y 0 en el resto de casos.
        """
        effect = 0
        if opponent._unit_type == 'Cavalry':
            effect = 1
        elif opponent._unit_type == 'Infantry':
            effect = -1
        return  effect 
    
    @property
    def arrows(self):
        return self._arrows

    @arrows.setter
    def arrows(self, value):
        if isinstance(value, int) and value >= 0:
            self._arrows = value
        else:
            raise ValueError('El número de flechas debe ser un número entero.')
 
class Cavalry(Unit):
    """ definimos las características básicas de la clase Cavalry.
    Attributes
    ----------
    Unit
    Al llamar a la superclase ya contiene todos sus atributos
    -------
    effectiveness(self, opponent:'Unit') :
    Define la relación entre las subclases en base a su interacción en batalla -1 devil, 0 neutro y 1 efectivo.
    attack(self, opponent:'Unit') :
    Daño básico de 1 unidad, se modifica dependiendo de la clase.
    is_debilitated(self) :
    Indica si la unidad está fuera de combate, con unidades de hp igual a 0 (True) o todavía en batalla (False)
    """
    
    def __init__(self, name:str, strength:int, defense:int, hp:int, total_hp:int, charge:int):
        """ Asigna atributos al objeto Cavalry 
        Parameters
        ----------
        self : Unit
        Objeto que referencia a Cavalry
        name : str
        Nombre de la unidad.
        strength : int
        Unidades de fuerza basica de la uniad, las unidades de ataque se calculan con la strength y la defense.
        defense : int
        Unidades de defensa, se resta al total del daño antes de devolver el número de unidades de daño causadas.
        hp : int
        Puntos de salud varia a lo largo del juego pero nunca aumenta, siempre inferior o igual a total_hp.
        total_hp : int
        Puntos totales de vida, no varia a lo largo de la partida.
        charge: int
        Total de carga que tiene.
        Returns
        -------
        None
        """
        self._charge = charge
        self._unit_type = 'Cavalry'
        super().__init__(name, strength, defense, hp, total_hp) 
        
    def attack(self, opponent:'Unit') -> int:
        """Daño que se realiza al oponente, se modifica dependiendo de la clase.
        Parameters
        ----------
        self : Unit
        Objeto que queremos que ataque.
        opponent : Unit
        Objeto oponente del cual necesitamos saber su defensa.
        Returns
        -------
        int
        Devuelve las unidades de ataque.
        """
        if opponent._hp > 0:
            factor = 1
            if opponent._unit_type == 'Infantry':
                factor = 1.5
            elif opponent._unit_type == 'Archer':
                factor = 0.5
         
            n = math.floor((max(1, (self._charge + factor*self._strength) - opponent._defense)))
            if opponent._hp - n <= 0:
                """comprobamos que la vida restante del oponente no sea inferior a 0"""
                n = opponent._hp
            opponent._hp = max(0, opponent._hp - n)
            return n
        else:
            return 'Oponente no disponible'
        
    def effectiveness(self, opponent:'Unit') -> int:
        """Indica la efectividad del ataque dependiendo de la unidad.
        Parameters
        ----------
        self : Unit
        Objeto que queremos saber si está debilitado.
        Returns
        -------
        int
        1 si el oponente es Infantry, -1 si es Archer y 0 en el resto de casos.
        """
        effect = 0
        if opponent._unit_type == 'Archer':
            effect = -1
        elif opponent._unit_type == 'Infantry':
            effect = 1
        return effect 

    @property
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self, value):
        if isinstance(value, int) and value >= 0:
            self._charge = value
        else:
            raise ValueError('La carga tiene que ser positiva y entera.')
 
class Infantry(Unit):
    """ definimos las características básicas de la clase Infantry.
    Attributes
    ----------
    Unit
    Al llamar a la superclase ya contiene todos sus atributos
    -------
    effectiveness(self, opponent:'Unit') :
    Define la relación entre las subclases en base a su interacción en batalla -1 devil, 0 neutro y 1 efectivo.
    attack(self, opponent:'Unit') :
    Daño básico de 1 unidad, se modifica dependiendo de la clase.
    is_debilitated(self) :
    Indica si la unidad está fuera de combate, con unidades de hp igual a 0 (True) o todavía en batalla (False)
    """
    
    def __init__(self, name:str, strength:int, defense:int, hp:int, total_hp:int, fury:int):
        """ Asigna atributos al objeto Infantry 
        Parameters
        ----------
        self : Unit
        Objeto que referencia a Infantry
        name : str
        Nombre de la unidad.
        strength : int
        Unidades de fuerza basica de la uniad, las unidades de ataque se calculan con la strength y la defense.
        defense : int
        Unidades de defensa, se resta al total del daño antes de devolver el número de unidades de daño causadas.
        hp : int
        Puntos de salud varia a lo largo del juego pero nunca aumenta, siempre inferior o igual a total_hp.
        total_hp : int
        Puntos totales de vida, no varia a lo largo de la partida.
        fury: int
        Total de furia que tiene.
        Returns
        -------
        None
        """
        self._fury = fury
        self._unit_type = 'Infantry'
        super().__init__(name, strength, defense, hp, total_hp) 
        
    def attack(self, opponent:'Unit') -> int:
        """Daño que se realiza al oponente, se modifica dependiendo de la clase.
        Parameters
        ----------
        self : Unit
        Objeto que queremos que ataque.
        opponent : Unit
        Objeto oponente del cual necesitamos saber su defensa.
        Returns
        -------
        int
        Devuelve las unidades de ataque.
        """
        if opponent._hp > 0:
            factor = 1
            if opponent._unit_type == 'Archer':
                factor = 1.5
            elif opponent._unit_type == 'Cavalry':
                factor = 0.5
                
            n = math.floor((max(1, (self._fury + factor*self._strength) - opponent._defense)))
            if opponent._hp - n <= 0:
                n = opponent._hp
            opponent._hp = max(0, opponent._hp - n)
            return n
        else:
            return 'Oponente no disponible'
        
    def effectiveness(self, opponent:'Unit') -> int:
        """Indica la efectividad del ataque dependiendo de la unidad.        
        Parameters
        ----------
        self : Unit
        Objeto que queremos saber si está debilitado.
        Returns
        -------
        int
        1 si el oponente es Archer, -1 si es Cavalry y 0 en el resto de casos.
        """
        effect = 0
        if opponent._unit_type == 'Archer':
            effect = 1
        elif opponent._unit_type == 'Cavalry':
            effect = -1
        return  effect 

    @property
    def fury(self):
        return self._fury

    @fury.setter
    def fury(self, value):
        if isinstance(value, int) and value >= 0:
            self._fury = value
        else:
            raise ValueError('La furia tiene que ser positiva y entera.')
            
class Worker(Unit):
    """ definimos las características básicas de la clase Worker.
    Attributes
    ----------
    Unit
    Al llamar a la superclase ya contiene todos sus atributos
    -------
    effectiveness(self, opponent:'Unit') :
    Define la relación entre las subclases en base a su interacción en batalla -1 devil, 0 neutro y 1 efectivo.
    attack(self, opponent:'Unit') :
    Daño básico de 1 unidad, se modifica dependiendo de la clase.
    is_debilitated(self) :
    Indica si la unidad está fuera de combate, con unidades de hp igual a 0 (True) o todavía en batalla (False)
    """
    
    def __init__(self, name:str, strength:int, defense:int, hp:int, total_hp:int): 
        """ Asigna atributos al objeto Worker 
        Parameters
        ----------
        self : Unit
        Objeto que referencia a Worker
        name : str
        Nombre de la unidad.
        strength : int
        Unidades de fuerza basica de la uniad, las unidades de ataque se calculan con la strength y la defense.
        defense : int
        Unidades de defensa, se resta al total del daño antes de devolver el número de unidades de daño causadas.
        hp : int
        Puntos de salud varia a lo largo del juego pero nunca aumenta, siempre inferior o igual a total_hp.
        total_hp : int
        Puntos totales de vida, no varia a lo largo de la partida.
        Returns
        -------
        None
        """
        self._unit_type = 'Worker'
        super().__init__(name, strength, defense, hp, total_hp) 
        
    def attack(self, opponent:'Unit') -> int:
        """Daño que se realiza al oponente, siempre es 1.
        Parameters
        ----------
        self : Unit
        Objeto que queremos que ataque.
        opponent : Unit
        Objeto oponente del cual necesitamos saber su defensa.
        Returns
        -------
        int
        Devuelve las unidades de ataque.
        """
        if opponent._hp > 0:
            n = 1
            if opponent._hp - n <= 0:
                n = opponent._hp
            opponent._hp = max(0, opponent._hp - n)
            return n
        else:
            return 'Oponente no disponible'
        n = 1
        return n
        
    def collect(self)-> int:
        """permite a los Worker recolectar 10 de recursos
        Parameters
        ----------
        self : Unit
        Objeto que hace referencia a Worker
        Returns
        -------
        int
        Devuelve las unidades que recolecta que son 10.
        """
        return 10
        
    def effectiveness(self, opponent:'Unit') -> int:
        """Indica la efectividad del ataque dependiendo de la unidad.
        Parameters
        ----------
        self : Unit
        Objeto que queremos saber si está debilitado.
        Returns
        -------
        int
        Siempre devuelve -1.
        """
        return -1
