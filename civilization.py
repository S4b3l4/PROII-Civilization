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

  
    def train_unit(self, unit_type:str)-> 'Unit':
            
    
    def collect_resources(self)-> None:
        """ Permite que la civilización obtenga recursos cuando se llama a la función collect_resources """
        for unidad in sefl._units:
            if unidad._name == "Worker":
                self._resources += collect(unidad)
        return self._resources
    
    def all_debilitated(self)-> bool:
        """ indica la civilización está fuera de combate (True) o todavía en batalla (False) """
        live = 0
        for units in self._units:
            if units._hp == 0:
                live += 1
        if live == len(self._units):
            return True
        
