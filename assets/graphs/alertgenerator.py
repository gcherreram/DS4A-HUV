#Libraries
import numpy as np

#Create function to verify alert conditions provided by the hospital
def create_alerts(dfResLab5):
    dfResLab5["Alerta"] = np.where(
            (dfResLab5['MICROORGANISMO']=='Escherichia coli')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, 0)

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Klebsiella pneumoniae')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Klebsiella oxytoca')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Klebsiella aerogenes')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Klebsiella ozaenae')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Pseudomonas aeruginosa')  
        & ((dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Pseudomonas spp.')  
        & ((dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Acinetobacter lwoffii/haemolyticus')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & ((dfResLab5['MICROORGANISMO']=='Acinetobacter baumannii') | (dfResLab5['MICROORGANISMO']=='Acinetobacter baumannii/calcoaceticus complejo'))
        & ((dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Acinetobacter spp.') 
        & ( (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & ((dfResLab5['MICROORGANISMO']=='Enterobacter cloacae')| (dfResLab5['MICROORGANISMO']=='Enterobacter asburiae') | (dfResLab5['MICROORGANISMO']=='Enterobacter hormaechei') | (dfResLab5['MICROORGANISMO']=='Enterobacter cancerogenus') )
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefoxitina' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Proteus mirabilis') 
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Proteus vulgaris') 
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Proteus penneri') 
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Proteus spp.') 
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Morganella morganii') 
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & ((dfResLab5['MICROORGANISMO']=='Citrobacter freundii') | (dfResLab5['MICROORGANISMO']=='Citrobacter koseri') | (dfResLab5['MICROORGANISMO']=='Citrobacter youngae') 
            | (dfResLab5['MICROORGANISMO']=='Citrobacter werkmanii') | (dfResLab5['MICROORGANISMO']=='Citrobacter amalonaticus')
            | (dfResLab5['MICROORGANISMO']=='Citrobacter farmeri') | (dfResLab5['MICROORGANISMO']=='Citrobacter braakii'))
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Serratia marcescens') 
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Serratia marcescens ssp marcescens') 
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & ((dfResLab5['MICROORGANISMO']=='Aeromonas hydrophila') | (dfResLab5['MICROORGANISMO']=='Aeromonas caviae')
            | (dfResLab5['MICROORGANISMO']=='Aeromonas veronii bv veronii') | (dfResLab5['MICROORGANISMO']=='Aeromonas veronii bv sobria'))
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & ((dfResLab5['MICROORGANISMO']=='Providencia rettgeri') | (dfResLab5['MICROORGANISMO']=='Providencia stuartii') | (dfResLab5['MICROORGANISMO']=='Providencia alcalifaciens')) 
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' )
            |(dfResLab5['ANTIBIOTICO']== 'Cefepima' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0)
        & (dfResLab5['MICROORGANISMO']=='Salmonella spp.') 
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))   , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0) 
        & ((dfResLab5['MICROORGANISMO']=='Shigella') | (dfResLab5['MICROORGANISMO']=='Shigella flexneri') 
            | (dfResLab5['MICROORGANISMO']=='Shigella boydii') | (dfResLab5['MICROORGANISMO']=='Shigella sonnei') 
            | (dfResLab5['MICROORGANISMO']=='Shigella dysenteriae') ) 
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Escherichia coli')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ampicilina' ) | (dfResLab5['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Cefazolina' )
            | (dfResLab5['ANTIBIOTICO']== 'Levofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Moxifloxacino' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefalotina' ) | (dfResLab5['ANTIBIOTICO']== 'Cefuroxima' ) | (dfResLab5['ANTIBIOTICO']== 'Cefoxitina' )
            | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ) | (dfResLab5['ANTIBIOTICO']== 'Nitrofurantoína' ) | (dfResLab5['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Klebsiella pneumoniae')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ampicilina' ) | (dfResLab5['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Cefazolina' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefalotina' ) | (dfResLab5['ANTIBIOTICO']== 'Cefuroxima' ) | (dfResLab5['ANTIBIOTICO']== 'Cefoxitina' )
            | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ) | (dfResLab5['ANTIBIOTICO']== 'Nitrofurantoína' ) | (dfResLab5['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=="Klebsiella oxytoca")  
        & ((dfResLab5['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Cefazolina' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefalotina' ) | (dfResLab5['ANTIBIOTICO']== 'Cefuroxima' ) | (dfResLab5['ANTIBIOTICO']== 'Cefoxitina' )
            | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ) | (dfResLab5['ANTIBIOTICO']== 'Nitrofurantoína' ) | (dfResLab5['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) | (dfResLab5['ANTIBIOTICO']== 'Ampicilina' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
            (dfResLab5['MICROORGANISMO']=="Klebsiella ozaenae")  
        & ((dfResLab5['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Cefazolina' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefalotina' ) | (dfResLab5['ANTIBIOTICO']== 'Cefuroxima' ) | (dfResLab5['ANTIBIOTICO']== 'Cefoxitina' )
            | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ) | (dfResLab5['ANTIBIOTICO']== 'Nitrofurantoína' ) | (dfResLab5['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=="Klebsiella aerogenes")  
        & ((dfResLab5['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Cefazolina' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefalotina' ) | (dfResLab5['ANTIBIOTICO']== 'Cefuroxima' ) | (dfResLab5['ANTIBIOTICO']== 'Cefoxitina' )
            | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ) | (dfResLab5['ANTIBIOTICO']== 'Nitrofurantoína' ) | (dfResLab5['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=="Pseudomonas aeruginosa")  
        & ((dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftazidima') | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Aztreonam' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=="Pseudomonas spp.")  
        & ((dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftazidima') | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Aztreonam' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        ((dfResLab5['MICROORGANISMO']=='Acinetobacter baumannii') | (dfResLab5['MICROORGANISMO']=='Acinetobacter baumannii/calcoaceticus complejo')) 
        & ((dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftazidima') | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ) | (dfResLab5['ANTIBIOTICO']== 'Rifampicina' ) | (dfResLab5['ANTIBIOTICO']== 'Levofloxacino' )
            | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' )| (dfResLab5['ANTIBIOTICO']== 'Colistina' ) | (dfResLab5['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Acinetobacter lwoffii/haemolyticus') 
        & ((dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftazidima') | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ) | (dfResLab5['ANTIBIOTICO']== 'Rifampicina' ) | (dfResLab5['ANTIBIOTICO']== 'Levofloxacino' )
            | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' )| (dfResLab5['ANTIBIOTICO']== 'Colistina' ) | (dfResLab5['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Acinetobacter spp.') 
        & ((dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftazidima') | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ) | (dfResLab5['ANTIBIOTICO']== 'Rifampicina' ) | (dfResLab5['ANTIBIOTICO']== 'Levofloxacino' )
            | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' )| (dfResLab5['ANTIBIOTICO']== 'Colistina' ) | (dfResLab5['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Proteus mirabilis')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ampicilina' ) | (dfResLab5['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Cefazolina' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefalotina' ) | (dfResLab5['ANTIBIOTICO']== 'Cefuroxima' ) | (dfResLab5['ANTIBIOTICO']== 'Cefoxitina' )
            | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ) | (dfResLab5['ANTIBIOTICO']== 'Nitrofurantoína' ) | (dfResLab5['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=="Proteus vulgaris")  
        & ((dfResLab5['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=="Proteus penneri")  
        & ((dfResLab5['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Proteus spp.')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ampicilina' ) | (dfResLab5['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Cefazolina' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefalotina' ) | (dfResLab5['ANTIBIOTICO']== 'Cefuroxima' ) | (dfResLab5['ANTIBIOTICO']== 'Cefoxitina' )
            | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            |  (dfResLab5['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=="Morganella morganii")  
        & ((dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona')  
            | (dfResLab5['ANTIBIOTICO']== 'Aztreonam' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        ((dfResLab5['MICROORGANISMO']=='Citrobacter freundii') | (dfResLab5['MICROORGANISMO']=='Citrobacter koseri') | (dfResLab5['MICROORGANISMO']=='Citrobacter youngae') 
        | (dfResLab5['MICROORGANISMO']=='Citrobacter werkmanii') | (dfResLab5['MICROORGANISMO']=='Citrobacter amalonaticus')
        | (dfResLab5['MICROORGANISMO']=='Citrobacter farmeri') | (dfResLab5['MICROORGANISMO']=='Citrobacter braakii')) 
        & ((dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona')  
            | (dfResLab5['ANTIBIOTICO']== 'Aztreonam' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=="Serratia marcescens")  
        & ((dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona')  
            | (dfResLab5['ANTIBIOTICO']== 'Aztreonam' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=="Serratia marcescens ssp marcescens")  
        & ((dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona')  
            | (dfResLab5['ANTIBIOTICO']== 'Aztreonam' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        ((dfResLab5['MICROORGANISMO']=='Aeromonas hydrophila') | (dfResLab5['MICROORGANISMO']=='Aeromonas caviae')
            | (dfResLab5['MICROORGANISMO']=='Aeromonas veronii bv veronii') | (dfResLab5['MICROORGANISMO']=='Aeromonas veronii bv sobria') ) 
        & ((dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona')  
            | (dfResLab5['ANTIBIOTICO']== 'Aztreonam' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        ((dfResLab5['MICROORGANISMO']=='Providencia rettgeri') | (dfResLab5['MICROORGANISMO']=='Providencia stuartii') | (dfResLab5['MICROORGANISMO']=='Providencia alcalifaciens')) 
        & ((dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona')  
            | (dfResLab5['ANTIBIOTICO']== 'Aztreonam' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=="Salmonella spp.")  
        & ((dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' )
            | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona') | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' )  
            | (dfResLab5['ANTIBIOTICO']== 'Aztreonam' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        ((dfResLab5['MICROORGANISMO']=='Shigella') | (dfResLab5['MICROORGANISMO']=='Shigella flexneri') 
            | (dfResLab5['MICROORGANISMO']=='Shigella boydii') | (dfResLab5['MICROORGANISMO']=='Shigella sonnei') 
            | (dfResLab5['MICROORGANISMO']=='Shigella dysenteriae') ) 
        & ((dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' )
            | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona') | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' )  
            | (dfResLab5['ANTIBIOTICO']== 'Aztreonam' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Escherichia coli')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & (dfResLab5['RESISTENCIA']=='S')  & (dfResLab5['ESBL (+ es blee )']=='+') , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Klebsiella pneumoniae')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & (dfResLab5['RESISTENCIA']=='S')  & (dfResLab5['ESBL (+ es blee )']=='+') , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Klebsiella oxytoca')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & (dfResLab5['RESISTENCIA']=='S')  & (dfResLab5['ESBL (+ es blee )']=='+') , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Klebsiella aerogenes')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & (dfResLab5['RESISTENCIA']=='S')  & (dfResLab5['ESBL (+ es blee )']=='+') , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Klebsiella ozaenae')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & (dfResLab5['RESISTENCIA']=='S')  & (dfResLab5['ESBL (+ es blee )']=='+') , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Proteus mirabilis')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & (dfResLab5['RESISTENCIA']=='S')  & (dfResLab5['ESBL (+ es blee )']=='+') , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Proteus vulgaris')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & (dfResLab5['RESISTENCIA']=='S')  & (dfResLab5['ESBL (+ es blee )']=='+') , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Proteus penneri')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & (dfResLab5['RESISTENCIA']=='S')  & (dfResLab5['ESBL (+ es blee )']=='+') , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Proteus spp.')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & (dfResLab5['RESISTENCIA']=='S')  & (dfResLab5['ESBL (+ es blee )']=='+') , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Stenotrophomonas maltophilia')  
        & (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) 
        & ((dfResLab5['RESISTENCIA']=='S') | (dfResLab5['RESISTENCIA']=='R'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Neisseria meningitidis')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ) | (dfResLab5['ANTIBIOTICO']== 'Ampicilina' ) | (dfResLab5['ANTIBIOTICO']== 'Penicilina G' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Neisseria gonorrhoeae')  
        & ((dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ) | (dfResLab5['ANTIBIOTICO']== 'Azitromicina' ) | (dfResLab5['ANTIBIOTICO']== 'Penicilina G' )
            | (dfResLab5['ANTIBIOTICO']== 'Tetraciclina' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        ((dfResLab5['MICROORGANISMO']== "Bacilo Gram-negativo oxidasa-negativo") | (dfResLab5['MICROORGANISMO']== "Bacilo Gram-negativo oxidasa-positivo")
            |(dfResLab5['MICROORGANISMO']== "Bacilo Gram-negativo no identificado no fermentador") | (dfResLab5['MICROORGANISMO']== "Bacilo Gram-negativo"))  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        ((dfResLab5['MICROORGANISMO']== "Bacilo Gram-negativo oxidasa-negativo") | (dfResLab5['MICROORGANISMO']== "Bacilo Gram-negativo oxidasa-positivo")
            |(dfResLab5['MICROORGANISMO']== "Bacilo Gram-negativo no identificado no fermentador") | (dfResLab5['MICROORGANISMO']== "Bacilo Gram-negativo"))  
        & ((dfResLab5['ANTIBIOTICO']== 'Ertapenem' ) | (dfResLab5['ANTIBIOTICO']== 'Meropenem' ) | (dfResLab5['ANTIBIOTICO']== 'Imipenem' ) | (dfResLab5['ANTIBIOTICO']== 'Doripenem' ))
        & (dfResLab5['RESISTENCIA']=='S')  & (dfResLab5['ESBL (+ es blee )']=='+') , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        ((dfResLab5['MICROORGANISMO']== "Bacilo Gram-negativo oxidasa-negativo") | (dfResLab5['MICROORGANISMO']== "Bacilo Gram-negativo oxidasa-positivo")
            |(dfResLab5['MICROORGANISMO']== "Bacilo Gram-negativo no identificado no fermentador") | (dfResLab5['MICROORGANISMO']== "Bacilo Gram-negativo"))  
        & ((dfResLab5['ANTIBIOTICO']== 'Ampicilina' ) | (dfResLab5['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (dfResLab5['ANTIBIOTICO']== 'Ciprofloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Cefazolina' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefalotina' ) | (dfResLab5['ANTIBIOTICO']== 'Cefuroxima' ) | (dfResLab5['ANTIBIOTICO']== 'Cefoxitina' )
            | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' ) | (dfResLab5['ANTIBIOTICO']== 'Cefepima' )
            | (dfResLab5['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (dfResLab5['ANTIBIOTICO']== 'Amikacina' ) | (dfResLab5['ANTIBIOTICO']== 'Gentamicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Tigeciclina' ) | (dfResLab5['ANTIBIOTICO']== 'Nitrofurantoína' ) | (dfResLab5['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (dfResLab5['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Staphylococcus aureus')  
        & ((dfResLab5['ANTIBIOTICO']== 'Vancomicina' ) | (dfResLab5['ANTIBIOTICO']== 'Daptomicina' ) | (dfResLab5['ANTIBIOTICO']== 'Linezolida' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO']=='Staphylococcus aureus')  
        & ((dfResLab5['ANTIBIOTICO']== 'Vancomicina' ) | (dfResLab5['ANTIBIOTICO']== 'Oxacilina' ) )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='S'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(
        (dfResLab5['MICROORGANISMO']=='Staphylococcus epidermidis')  
        & (dfResLab5['ANTIBIOTICO']== 'Oxacilina' ) 
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='S'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        dfResLab5['MICROORGANISMO'].str.contains('Staphylococcus') 
        & (dfResLab5['ANTIBIOTICO']== 'Oxacilina' ) 
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='S'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        dfResLab5['MICROORGANISMO'].str.contains('Enterococcus')  
        & ((dfResLab5['ANTIBIOTICO']== 'Vancomicina' ) | (dfResLab5['ANTIBIOTICO']== 'Ampicilina'))  
        & (dfResLab5['RESISTENCIA']=='R')  , 1, dfResLab5["Alerta"])
            
    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO'].str.contains('Enterococcus'))  
        & (dfResLab5['ANTIBIOTICO']== 'Ampicilina')  
        & (dfResLab5['RESISTENCIA']=='S')  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        dfResLab5['MICROORGANISMO'].str.contains('Streptococcus') 
        & ((dfResLab5['ANTIBIOTICO']== 'Vancomicina' ) | (dfResLab5['ANTIBIOTICO']== 'Levofloxacino' )
            | (dfResLab5['ANTIBIOTICO']== 'Ceftriaxona' ) | (dfResLab5['ANTIBIOTICO']== 'Cefotaximo' )
            | (dfResLab5['ANTIBIOTICO']== 'Cefepima' ) | (dfResLab5['ANTIBIOTICO']== 'Eritromicina' )
            | (dfResLab5['ANTIBIOTICO']== 'Moxifloxacino' ) | (dfResLab5['ANTIBIOTICO']== 'Penicilina G' )
            | (dfResLab5['ANTIBIOTICO']== 'Ampicilina' ) | (dfResLab5['ANTIBIOTICO']== 'Amoxicilina' ))
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO'].str.contains('Candida'))    
        & (dfResLab5['RESISTENCIA']=='S')  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO'].str.contains('Candida'))   
        & ((dfResLab5['ANTIBIOTICO']== 'Anfotericina B' ) | (dfResLab5['ANTIBIOTICO']== 'Caspofungina' )
            | (dfResLab5['ANTIBIOTICO']== 'Anidulafungina' ) | (dfResLab5['ANTIBIOTICO']== 'Micafungina' )
            | (dfResLab5['ANTIBIOTICO']== 'Fluconazol' ) | (dfResLab5['ANTIBIOTICO']== 'Itraconazol' )
            | (dfResLab5['ANTIBIOTICO']== 'Voriconazol' ) | (dfResLab5['ANTIBIOTICO']== 'Posaconazol' )
        )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO'].str.contains('Cryptococcus'))   
        & ((dfResLab5['ANTIBIOTICO']== 'Anfotericina B' ) | (dfResLab5['ANTIBIOTICO']== 'Flucitosina' )
            | (dfResLab5['ANTIBIOTICO']== 'Fluconazol' ) | (dfResLab5['ANTIBIOTICO']== 'Itraconazol' )
            | (dfResLab5['ANTIBIOTICO']== 'Voriconazol' ) | (dfResLab5['ANTIBIOTICO']== 'Posaconazol' )
        )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO'].str.contains('Cryptococcus')) &   
        (dfResLab5['RESISTENCIA']=='S')  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO'].str.contains('Aspergillus'))   
        & ((dfResLab5['ANTIBIOTICO']== 'Anfotericina B' ) | (dfResLab5['ANTIBIOTICO']== 'Caspofungina' )
            | (dfResLab5['ANTIBIOTICO']== 'Anidulafungina' ) | (dfResLab5['ANTIBIOTICO']== 'Micafungina' )
        )
        & ((dfResLab5['RESISTENCIA']=='R') | (dfResLab5['RESISTENCIA']=='I'))  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        (dfResLab5['MICROORGANISMO'].str.contains('Aspergillus'))
        &    
        (dfResLab5['RESISTENCIA']=='S')  , 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(  (dfResLab5["Alerta"] == 0) &
        dfResLab5['MICROORGANISMO'].str.contains('Fusariums'), 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(  (dfResLab5["Alerta"] == 0) &
        dfResLab5['MICROORGANISMO'].str.contains('Bacillus'), 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(  (dfResLab5["Alerta"] == 0) &
        dfResLab5['MICROORGANISMO'].str.contains('Rhizo'), 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where(  (dfResLab5["Alerta"] == 0) &
        dfResLab5['MICROORGANISMO'].str.contains('Burkholderia'), 1, dfResLab5["Alerta"])

    dfResLab5["Alerta"] = np.where( (dfResLab5["Alerta"] == 0) &
        dfResLab5['MICROORGANISMO'].str.contains('Clostridioides'), 1, dfResLab5["Alerta"])
    
    return dfResLab5
