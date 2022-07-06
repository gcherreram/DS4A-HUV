#Libraries
import pandas as pd

#Import dataframes with all dictionary info
dic_medicamento = pd.read_csv("data/dictionaries/Dic_Medicamentos.csv", on_bad_lines='skip', delimiter =";", low_memory=False, encoding='latin-1')
dic_micro = pd.read_csv("data/dictionaries/Dic_microorganismos.csv", on_bad_lines='skip', delimiter =";", low_memory=False, encoding='latin-1')

# Update microorganisms
dic_rename_micro = (dic_micro[['Microorganismos_by Hospital','Microorganismos']]).set_index('Microorganismos_by Hospital')
dic_rename_micro = dic_rename_micro.to_dict()
dic_rename_micro = dic_rename_micro.get('Microorganismos')

#Create dictionary to clasify microorganisms between fungus and bacteria 
dic_bacteria_fungus = (dic_micro[['Microorganismos','Bacteria/Hongo']]).set_index('Microorganismos')
dic_bacteria_fungus = dic_bacteria_fungus.to_dict()
dic_bacteria_fungus = dic_bacteria_fungus.get('Bacteria/Hongo')

#Create dictionary to clasify microorganisms by families
dic_family_microorganism = (dic_micro[['Microorganismos','Family']]).set_index('Microorganismos')
dic_family_microorganism = dic_family_microorganism.to_dict()
dic_family_microorganism = dic_family_microorganism.get('Family')

#Create dictionary to clasify microorganisms into superior order
dic_order_microorganism = (dic_micro[['Microorganismos','Orden']]).set_index('Microorganismos')
dic_order_microorganism = dic_order_microorganism.to_dict()
dic_order_microorganism = dic_order_microorganism.get('Orden')

#Create dictionary to clasify bacteria between gram positive and gram negative, and label fungus
dic_gram_microorganism = (dic_micro[['Microorganismos','Gram/Hongo']]).set_index('Microorganismos')
dic_gram_microorganism = dic_gram_microorganism.to_dict()
dic_gram_microorganism = dic_gram_microorganism.get('Gram/Hongo')

#Create dictionary to clasify bacteria between gram positive and gram negative, and label fungus
dic_shape_microorganism = (dic_micro[['Microorganismos','Forma']]).set_index('Microorganismos')
dic_shape_microorganism = dic_shape_microorganism.to_dict()
dic_shape_microorganism = dic_shape_microorganism.get('Forma')

#Create dictionary to update medicaments
dic_rename_antibiotic = (dic_medicamento[['Medicamento-HUV','Medicamento']]).set_index('Medicamento-HUV')
dic_rename_antibiotic = dic_rename_antibiotic.to_dict()
dic_rename_antibiotic = dic_rename_antibiotic.get('Medicamento')

#Create dictionary to clasify medicaments into families
dic_family_antibiotic = (dic_medicamento[['Medicamento-HUV','Correcciones_nombre_grupos']]).set_index('Medicamento-HUV')
dic_family_antibiotic = dic_family_antibiotic.to_dict()
dic_family_antibiotic = dic_family_antibiotic.get('Correcciones_nombre_grupos')

#Create dictionary to clasify medicaments into antifungal or antibiotics
dic_type_antibiotic = (dic_medicamento[['Medicamento-HUV','ANTIBIÓTICO-ANTIMICÓTICO']]).set_index('Medicamento-HUV')
dic_type_antibiotic = dic_type_antibiotic.to_dict()
dic_type_antibiotic = dic_type_antibiotic.get('ANTIBIÓTICO-ANTIMICÓTICO')

list_dicts = {"dic_rename_micro":dic_rename_micro,
        "dic_bacteria_fungus":dic_bacteria_fungus,
        "dic_family_microorganism":dic_family_microorganism,
        "dic_order_microorganism":dic_order_microorganism,
        "dic_gram_microorganism":dic_gram_microorganism,
        "dic_shape_microorganism":dic_gram_microorganism,
        "dic_rename_antibiotic":dic_rename_antibiotic,
        "dic_family_antibiotic":dic_family_antibiotic,
        "dic_type_antibiotic":dic_family_antibiotic
        }

def dictTransform(variable, dictionary_ref):
    dictionary = list_dicts[dictionary_ref]
    new_var = variable.map(dictionary, na_action=None)
    return new_var



