# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:13:07 2025

@author: usuario
"""

from abc import ABC

class civilization(ABC):
    """ definimos las características básicas de la clase abstracta Unit. """
    def __init__(self, name:str, resources:int, units:list):
      self._name = name
      self._resources = resources
      self._units = units #se define en la subclase
      
    def train_unit(self, unit_type:str)-> 'Unit':
        """ se completa en el archivo de batalla"""
        pass 
    
    def collect(self)-> None:
        """ daño básico de 1 unidad, se modifica dependiendo de la clase """
        return 1
    
    def all_debilitated(self)-> bool:
        """ indica la unidad está fuera de combate (True) o todavía en batalla (False) """
    
    """
    Estas tres funciones son comunes a todos los personajes
    """
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            return 'El nombre no puede ser una cadena de texto vacía.'

    @property
    def resources(self):
        return self._resources
    @resources.setter
    def resources(self, value):
        if isinstance(value, int) and value >= 0:
            self._resources = value
        else:
            return 'Debe ser un número entero y positivo.'
        
    @property
    def units(self):
        return self._units
