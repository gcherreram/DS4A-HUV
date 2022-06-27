#Libraries
import pandas as pd

"""dic_unit = pd.read_csv("data/dictionaries/Dic_salas.csv", names=["SALA_HUV", "Sala", "Piso"], header=0, 
    on_bad_lines='skip', delimiter =";", low_memory=False, encoding='latin-1')"""

#Import dataframe with all dictionary info
dic_unit = pd.read_csv("data/dictionaries/Dic_salas.csv", on_bad_lines='skip', delimiter =";", low_memory=False)

#Create dictionary to update hospital units / rooms
dic_rename_unit = (dic_unit[['Sala_HUV','Sala']]).set_index('Sala_HUV')
dic_rename_unit = dic_rename_unit.to_dict()
dic_rename_unit = dic_rename_unit.get('Sala')

#Create dictionary to clasify units by hospital floor
dic_floor_unit = (dic_unit[['Sala','Piso']]).set_index('Sala')
dic_floor_unit = dic_floor_unit.to_dict()
dic_floor_unit = dic_floor_unit.get('Piso')

list_dicts = {"dic_rename_unit": dic_rename_unit, "dic_floor_unit":dic_floor_unit}

def dictTransformUnit(variable, dictionary_ref):
    dictionary = list_dicts[dictionary_ref]
    new_var = variable.map(dictionary, na_action=None)
    return new_var