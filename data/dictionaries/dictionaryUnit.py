#Libraries
import pandas as pd

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

#Create dictionary to assign codes to hospital units
dic_code_unit = (dic_unit[['Sala','Codigo']]).set_index('Sala')
dic_code_unit = dic_code_unit.to_dict()
dic_code_unit = dic_code_unit.get('Codigo')

list_dicts = {"dic_rename_unit": dic_rename_unit, "dic_floor_unit":dic_floor_unit, "dic_code_unit":dic_code_unit}

def dictTransformUnit(variable, dictionary_ref):
    dictionary = list_dicts[dictionary_ref]
    new_var = variable.map(dictionary, na_action=None)
    return new_var