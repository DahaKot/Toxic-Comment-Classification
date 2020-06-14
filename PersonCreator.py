from __future__ import print_function
import ipywidgets as widgets
import pandas as pd
from ipywidgets import interact, interactive, fixed, interact_manual

file = open("category_names.txt", "r")

category_names = file.read().split()
category_names = pd.DataFrame(columns = category_names).columns

checkboxes = []
checkboxes_names = {}
alphabet = ["a", "b", "c", "d", "e", "f"]

race_idx = [0, 3, 11, 12, 17, 23]
religion_idx = [1, 4, 5, 8, 14, 18]
sexual_orientation_idx = [2, 7, 9, 19]
gender_idx = [6, 13, 16, 22]
disability_idx = [10, 15, 20, 21]

general_category_names = ["race", "religion", "sexual_orientation", "gender", "disability"]

j = 0
for indicies in zip((race_idx, religion_idx, sexual_orientation_idx, gender_idx, disability_idx)):
    k = 0
    checkboxes.append([])
    checkboxes_names[general_category_names[j]] = {}
    
    for i in range(len(indicies[0])):
        elem = widgets.Checkbox(
            value = False,
            description = category_names[indicies[0][i]],
            disabled = False,
            indent = False
        )

        checkboxes[j].append(elem)
        checkboxes_names[general_category_names[j]][alphabet[k]] = elem
        k += 1
        
    j += 1

def f6(a, b, c, d, e, f):
    print((a, b, c, d, e, f))
    
def f4(a, b, c, d):
    print((a, b, c, d))

def display_creator():
    for i in range(len(checkboxes)):
        ui = widgets.HBox(checkboxes[i])

        f = f4
        if len(checkboxes[i]) == 6:
            f = f6

        out = widgets.interactive_output(f, checkboxes_names[general_category_names[i]])

        display(ui, out)
        
import torch

def create():
    person = torch.zeros(24)
    j = 0
    for indicies in zip((race_idx, religion_idx, sexual_orientation_idx, gender_idx, disability_idx)):
        for i in range(len(indicies[0])): 
            person[indicies[0][i]] = int(checkboxes[j][i].value)

        j += 1 
    return person