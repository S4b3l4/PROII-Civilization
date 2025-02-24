# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:18:49 2025

@author: usuario
"""
from abc import ABC, abstractmethod
import math

class Unit(ABC):
    'definimos las características básicas de la clase abstracta Unit.'
    def __init__(self, name:str, strength:int, defense:int, hp:int, total_hp:int, unit_type:str):
      self._name = name
      self._strength = strength
      self._defense = defense
      self._hp = hp
      self._total_hp = total_hp
      self._unit_type = None #se define en la subclase
  
    def __str__(self):
        return f'nombre: {self._name}, unit:{self._unit_type}, ATT: {self._strength}, DEF: {self._defense}, HP: {self._hp/self._total_hp}'
      # no sabemos como funciona
      
    @abstractmethod
    def effectiveness(self, opponent:'Unit')-> int:
        'se completa en el archivo de batalla'
        pass 
    
    def attack(self, opponent:'Unit')-> int:
        'daño básico de 1 unidad, se modifica dependiendo de la clase'
        return 1
    
    def is_debilitated(self)-> bool:
        'indica la unidad está fuera de combate (True) o todavía en batalla (False)'
        return self._hp == 0
   
   # ============================================================================
   #   Estas tres funciones son comunes a todos los personajes
   # ============================================================================
    
   
class Archer(Unit):
    
    def __init__(self, name:str, strength:int, defense:int, hp:int, total_hp:int, arrows:int):
        'define las características de la clase arquero'
        self._arrows = arrows
        'definimos el nº de flechas a la hora de la batalla para más flexibilidad del juego'
        super().__init__(name, strength, defense, hp, total_hp, unit_type = 'Archer') #super llama a la superclase.
        
    def attack(self, opponent:'Unit') -> int:
        'definimos el número de daño a cada oponente siendo 1 si no hay flechas'
        if opponent._hp > 0:
            factor =1
            if opponent._unit_type == 'Cavalry':
                factor = 1.5
            elif opponent._unit_type == 'Infantry':
                factor = 0.5

            n = math.floor((max(1, (factor*self._strength) - opponent._defense)))
        if self._arrows > 0:
            self._arrows = self._arrows - 1
            if opponent._hp - n <= 0:
                n = opponent._hp
        else:
            n = 1
            if opponent._hp - n <= 0:
                n = opponent._hp
        return n
    
    def effectiveness(self, opponent:'Unit') -> int:
        'definos la efectividad del ataque sobre cada oponente'
        effect = 0
        if opponent._unit_type == 'Cavalry':
            effect = 1
        elif opponent._unit_type == 'Infantry':
            effect = -1
        return  effect 
        
    
class Cavalry(Unit):
    
    def __init__(self, name:str, strength:int, defense:int, hp:int, total_hp:int, charge:int):
        'define las características de la clase caballería'
        self._charge = charge
        super().__init__(name, strength, defense, hp, total_hp, unit_type = 'Cavalry') 
        
    def attack(self, opponent:'Unit') -> int:
        'definimos el número de daño a cada oponente y lo restamos a la vida del oponente'
        if opponent._hp > 0:
            factor = 1
            if opponent._unit_type == 'Infantry':
                factor = 1.5
            elif opponent._unit_type == 'Archer':
                factor = 0.5
                
            n = math.floor((max(1, (self._charge + factor*self._strength) - opponent._defense)))
        if opponent._hp - n <= 0:
            n = opponent._hp
        return n
        
    def effectiveness(self, opponent:'Unit') -> int:
        'definos la efectividad del ataque sobre cada oponente'
        effect = 0
        if opponent._unit_type == 'Archer':
            effect = -1
        elif opponent._unit_type == 'Infantry':
            effect = 1
        return effect 
        
    
class Infantry(Unit):
    
    def __init__(self, name:str, strength:int, defense:int, hp:int, total_hp:int, fury:int):
        'define las características de la clase infantería'
        self._fury = fury
        super().__init__(name, strength, defense, hp, total_hp, unit_type = 'Infantry') 
        
    def attack(self, opponent:'Unit') -> int:
        'definimos el número de daño a cada oponente siendo 1 si no hay flechas'
        if opponent._hp > 0:
            factor = 1
            if opponent._unit_type == 'Archer':
                factor = 1.5
            elif opponent._unit_type == 'Cavalry':
                factor = 0.5
                
            n = math.floor((max(1, (self._fury + factor*self._strength) - opponent._defense)))
        if opponent._hp - n <= 0:
            n = opponent._hp
        return n
        
    def effectiveness(self, opponent:'Unit') -> int:
        'definos la efectividad del ataque sobre cada oponente'
        effect = 0
        if opponent._unit_type == 'Archer':
            effect = 1
        elif opponent._unit_type == 'Cavalry':
            effect = -1
        return  effect 
            
class Worker(Unit):
    
    def __init__(self, name:str, strength:int, defense:int, hp:int, total_hp:int):
        'define las características de la clase trabajador'
        super().__init__(name, strength, defense, hp, total_hp, unit_type = 'Worker') 
    def collect(self)-> int:
        return 10
    def effectiveness(self, opponent:'Unit') -> int:
        return -1