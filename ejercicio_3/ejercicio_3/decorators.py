'''
Decoradores para agregar ruido a funciones.
'''

import functools
from typing import Dict
from numpy.random import choice, random


def anadir_ruido(noise_probability : float, noise_distribution : Dict[str, float]):
    '''
    Agrega ruido a la salida de una funcion. Con probabilidad
    `noise_probability` la funcion retornara un valor de
    `noise_distribution` en vez del valor original.

    Parametros
    ----------
    noise_probability : float
        Probabilidad de que la funcion retorne un valor de
        `noise_distribution` en vez del valor original.
    noise_distribution : Dict[str, float]
        Distribucion de probabilidad de los valores de ruido.
        Las llaves son los valores de ruido y los valores son
        las probabilidades de cada valor. La suma de las probabilidades debe ser 1.
    
    Returns
    -------
    decorator : function
        Decorador que agrega ruido a la salida de una funcion.

    '''
    def inner_decorator(func):
        possible_noise_values = list(noise_distribution.keys())
        noise_value_probabilities = list(noise_distribution.values())
        @functools.wraps(func)
        def wrapper(*args):
            true_value = func(*args)
            if random() <= noise_probability: #ie con prob `noise_probability`
                vals, probs = exclude_true_value(possible_noise_values,
                                                 noise_value_probabilities, true_value)
                return choice(vals, p=probs)
            return true_value
        return wrapper
    return inner_decorator


def exclude_true_value(possible_noise_values, noise_value_probabilities, true_value):
    '''
    Excluye el valor verdadero de la lista de valores posibles de ruido y
    normaliza las probabilidades de los valores restantes.
    
    Parametros
    ----------
    possible_noise_values : Iterable
        Valores posibles de ruido.
    noise_value_probabilities : Iterable
        Probabilidades de los valores de ruido.
    true_value : str
        Valor verdadero.

    Returns
    -------
    vals : Iterable
        Valores de ruido posibles, excluyendo el valor verdadero.
    probs : Iterable
        Probabilidades normalizadas de los valores de ruido posibles.

    '''
    try:
        i = possible_noise_values.index(true_value)
        possible_noise_values = possible_noise_values[:i] + possible_noise_values[i+1:]
        noise_value_probabilities = noise_value_probabilities[:i] + noise_value_probabilities[i+1:]
        z = sum(noise_value_probabilities)
        noise_value_probabilities = [x/z for x in noise_value_probabilities]
    except ValueError:
        pass
    return possible_noise_values, noise_value_probabilities

if __name__ == "__main__":
    @anadir_ruido(0.5, {'ups!':0.7, 'UPS!':0.3})
    def funcion_de_ejemplo(x):
        '''
        Funcion que devuelve el doble del valor de x

        Parametros
        ----------
        x : int
            Valor de entrada.

        Returns
        -------
        int
            Doble del valor de x.
        '''
        return 2*x
    for y in range(10):
        print(funcion_de_ejemplo(y))
