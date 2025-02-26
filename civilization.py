# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:13:07 2025

@author: usuario
"""

from abc import ABC
from unit import *

class civilization():
    """ definimos las características básicas de la clase abstracta Unit. """
    def __init__(self, name:str, resources:int, units:list):
      self._name = name
      self._resources = resources
      self._units = units #se define en la subclaseç
      self._units_count = {"Archer" : 0, "Worker" : 0, "Cavalry" : 0, "Infantry":0 }
    
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
    @units.setter
    def units(self, value):
        if isinstance(value, list):
            self._units = value
        else:
            return 'Debe ser una lista.'

    def train_unit(self, new_unit_type:str)-> 'Unit':
            if new_unit_type == "Worker" and self._resources >= 30:
                self._unit_count ["Worker"]+= 1
                name = f"Worker_{self._unit_count["Worker"]}"
                new_unit = Worker(name, 1, 0, 5, 5)
                self._units.append(new_unit)
                
            elif self.resources >= 60:
                if new_unit_type == "Archer":
                    self._unit_count ["Archer"]+= 1
                    name = f"Archer_{self._unit_count["Archer"]}"
                    new_unit = Archer(name, 7, 2, 15, 15, 3) 
                    self._units.append(new_unit)
                   
                elif new_unit_type == "Cavalry":
                    self._unit_count ["Cavalry"]+= 1
                    name = f"Cavalry_{self._unit_count["Cavalry"]}"
                    new_unit = Cavalry(name, 5, 2, 25, 25, 5) 
                    self._units.append(new_unit)
                   
                elif new_unit_type == "Infantry":
                    self._unit_count ["Worker"]+= 1
                    name = f"Infantry_{self._unit_count["Infantry"]}"
                    new_unit = Infantry(name, 3, 2, 25, 25, 3) 
                    self._units.append(new_unit)
            else:
                return None
            return new_unit
        
    def collect_resources(self)-> None:
        """ Permite que la civilización obtenga recursos cuando se llama a la función collect_resources """
        for unidad in self._units:
            if unidad._unit_type == "Worker":
                self._resources += unidad.collect()
        return self._resources
    
    def all_debilitated(self)-> bool:
        """ indica la civilización está fuera de combate (True) o todavía en batalla (False) """
        live = 0
        for units in self._units:
            if units._hp == 0:
                live += 1
        if live == len(self._units):
            return True
        else:
            return False
