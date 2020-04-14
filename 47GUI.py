# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:51:26 2020

@author: Kajal
"""

## Note : most of the widgets are only available in Jupyter notebook

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def func(x):
    return x

interact(func, x = True)   # Checkbox for boolean
interact(func, x = 10)     # Slider for integers

## Reminder @ is decorator
@interact(x = True, y =0.1)
#Or can fixed y 
#@interact(x = True, y = fixed(0.1))
def g(x,y):
    
    return (x,y)

interact(func, x = widgets.IntSlider( min = -100, max = 100, step = 1, vaue = 0))

interact(func, x = (-10, 10, 0.1))   # breviated format

@interact(x =  (0.0, 20, 0.5))
def h(x=5.0):
    return x

interact(func, x = ['hello', 'option2', 'option3'])
# Gives drop down menu

from IPython.display import display
def f(a,b):
    display(a+b)
    return a+b

w = interactive(f, a=10, b =20)
type(w)     # >> ipywidgets.widgets.interaction.interactive

w.children

display(w)


widgets.IntRangeSlider()

# Show all available widgets

for item in widgets.Widget.widget_types.items():
    print(item[0])