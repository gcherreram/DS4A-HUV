#Libraries
import numpy as np

#Create function to verify alert conditions provided by the hospital
def create_alerts(df):
    df["Alerta"] = np.where(
            (df['MICROORGANISMO']=='Escherichia coli')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, 0)

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Klebsiella pneumoniae')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Klebsiella oxytoca')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Klebsiella aerogenes')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' )
            | (df['ANTIBIOTICO']== 'Cefepima' ) | (df['ANTIBIOTICO']== 'Ceftriaxona' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Klebsiella ozaenae')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' )
            | (df['ANTIBIOTICO']== 'Cefepima' ) | (df['ANTIBIOTICO']== 'Ceftriaxona' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Pseudomonas aeruginosa')  
        & ((df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Pseudomonas spp.')  
        & ((df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Acinetobacter lwoffii/haemolyticus')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & ((df['MICROORGANISMO']=='Acinetobacter baumannii') | (df['MICROORGANISMO']=='Acinetobacter baumannii/calcoaceticus complejo'))
        & ((df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Acinetobacter spp.') 
        & ( (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & ((df['MICROORGANISMO']=='Enterobacter cloacae')| (df['MICROORGANISMO']=='Enterobacter asburiae') | (df['MICROORGANISMO']=='Enterobacter hormaechei') | (df['MICROORGANISMO']=='Enterobacter cancerogenus') )
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' )
            | (df['ANTIBIOTICO']== 'Cefepima' ) | (df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefoxitina' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Proteus mirabilis') 
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Proteus vulgaris') 
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Proteus penneri') 
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Proteus spp.') 
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Morganella morganii') 
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & ((df['MICROORGANISMO']=='Citrobacter freundii') | (df['MICROORGANISMO']=='Citrobacter koseri') | (df['MICROORGANISMO']=='Citrobacter youngae') 
            | (df['MICROORGANISMO']=='Citrobacter werkmanii') | (df['MICROORGANISMO']=='Citrobacter amalonaticus')
            | (df['MICROORGANISMO']=='Citrobacter farmeri') | (df['MICROORGANISMO']=='Citrobacter braakii'))
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' )
            | (df['ANTIBIOTICO']== 'Cefepima' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Serratia marcescens') 
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Serratia marcescens ssp marcescens') 
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & ((df['MICROORGANISMO']=='Aeromonas hydrophila') | (df['MICROORGANISMO']=='Aeromonas caviae')
            | (df['MICROORGANISMO']=='Aeromonas veronii bv veronii') | (df['MICROORGANISMO']=='Aeromonas veronii bv sobria'))
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' )
            | (df['ANTIBIOTICO']== 'Cefepima' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & ((df['MICROORGANISMO']=='Providencia rettgeri') | (df['MICROORGANISMO']=='Providencia stuartii') | (df['MICROORGANISMO']=='Providencia alcalifaciens')) 
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' )
            |(df['ANTIBIOTICO']== 'Cefepima' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0)
        & (df['MICROORGANISMO']=='Salmonella spp.') 
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))   , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0) 
        & ((df['MICROORGANISMO']=='Shigella') | (df['MICROORGANISMO']=='Shigella flexneri') 
            | (df['MICROORGANISMO']=='Shigella boydii') | (df['MICROORGANISMO']=='Shigella sonnei') 
            | (df['MICROORGANISMO']=='Shigella dysenteriae') ) 
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Escherichia coli')  
        & ((df['ANTIBIOTICO']== 'Ampicilina' ) | (df['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Cefazolina' )
            | (df['ANTIBIOTICO']== 'Levofloxacino' ) | (df['ANTIBIOTICO']== 'Moxifloxacino' )
            | (df['ANTIBIOTICO']== 'Cefalotina' ) | (df['ANTIBIOTICO']== 'Cefuroxima' ) | (df['ANTIBIOTICO']== 'Cefoxitina' )
            | (df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ) | (df['ANTIBIOTICO']== 'Cefepima' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Tigeciclina' ) | (df['ANTIBIOTICO']== 'Nitrofurantoína' ) | (df['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Klebsiella pneumoniae')  
        & ((df['ANTIBIOTICO']== 'Ampicilina' ) | (df['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Cefazolina' )
            | (df['ANTIBIOTICO']== 'Cefalotina' ) | (df['ANTIBIOTICO']== 'Cefuroxima' ) | (df['ANTIBIOTICO']== 'Cefoxitina' )
            | (df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ) | (df['ANTIBIOTICO']== 'Cefepima' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Tigeciclina' ) | (df['ANTIBIOTICO']== 'Nitrofurantoína' ) | (df['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=="Klebsiella oxytoca")  
        & ((df['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Cefazolina' )
            | (df['ANTIBIOTICO']== 'Cefalotina' ) | (df['ANTIBIOTICO']== 'Cefuroxima' ) | (df['ANTIBIOTICO']== 'Cefoxitina' )
            | (df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ) | (df['ANTIBIOTICO']== 'Cefepima' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Tigeciclina' ) | (df['ANTIBIOTICO']== 'Nitrofurantoína' ) | (df['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) | (df['ANTIBIOTICO']== 'Ampicilina' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
            (df['MICROORGANISMO']=="Klebsiella ozaenae")  
        & ((df['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Cefazolina' )
            | (df['ANTIBIOTICO']== 'Cefalotina' ) | (df['ANTIBIOTICO']== 'Cefuroxima' ) | (df['ANTIBIOTICO']== 'Cefoxitina' )
            | (df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ) | (df['ANTIBIOTICO']== 'Cefepima' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Tigeciclina' ) | (df['ANTIBIOTICO']== 'Nitrofurantoína' ) | (df['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=="Klebsiella aerogenes")  
        & ((df['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Cefazolina' )
            | (df['ANTIBIOTICO']== 'Cefalotina' ) | (df['ANTIBIOTICO']== 'Cefuroxima' ) | (df['ANTIBIOTICO']== 'Cefoxitina' )
            | (df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ) | (df['ANTIBIOTICO']== 'Cefepima' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Tigeciclina' ) | (df['ANTIBIOTICO']== 'Nitrofurantoína' ) | (df['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=="Pseudomonas aeruginosa")  
        & ((df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Ceftazidima') | (df['ANTIBIOTICO']== 'Cefepima' ) 
            | (df['ANTIBIOTICO']== 'Aztreonam' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=="Pseudomonas spp.")  
        & ((df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Ceftazidima') | (df['ANTIBIOTICO']== 'Cefepima' ) 
            | (df['ANTIBIOTICO']== 'Aztreonam' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        ((df['MICROORGANISMO']=='Acinetobacter baumannii') | (df['MICROORGANISMO']=='Acinetobacter baumannii/calcoaceticus complejo')) 
        & ((df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Ceftazidima') | (df['ANTIBIOTICO']== 'Cefepima' ) 
            | (df['ANTIBIOTICO']== 'Tigeciclina' ) | (df['ANTIBIOTICO']== 'Rifampicina' ) | (df['ANTIBIOTICO']== 'Levofloxacino' )
            | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' )| (df['ANTIBIOTICO']== 'Colistina' ) | (df['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Acinetobacter lwoffii/haemolyticus') 
        & ((df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Ceftazidima') | (df['ANTIBIOTICO']== 'Cefepima' ) 
            | (df['ANTIBIOTICO']== 'Tigeciclina' ) | (df['ANTIBIOTICO']== 'Rifampicina' ) | (df['ANTIBIOTICO']== 'Levofloxacino' )
            | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' )| (df['ANTIBIOTICO']== 'Colistina' ) | (df['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Acinetobacter spp.') 
        & ((df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Ceftazidima') | (df['ANTIBIOTICO']== 'Cefepima' ) 
            | (df['ANTIBIOTICO']== 'Tigeciclina' ) | (df['ANTIBIOTICO']== 'Rifampicina' ) | (df['ANTIBIOTICO']== 'Levofloxacino' )
            | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' )| (df['ANTIBIOTICO']== 'Colistina' ) | (df['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Proteus mirabilis')  
        & ((df['ANTIBIOTICO']== 'Ampicilina' ) | (df['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Cefazolina' )
            | (df['ANTIBIOTICO']== 'Cefalotina' ) | (df['ANTIBIOTICO']== 'Cefuroxima' ) | (df['ANTIBIOTICO']== 'Cefoxitina' )
            | (df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ) | (df['ANTIBIOTICO']== 'Cefepima' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Tigeciclina' ) | (df['ANTIBIOTICO']== 'Nitrofurantoína' ) | (df['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=="Proteus vulgaris")  
        & ((df['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (df['ANTIBIOTICO']== 'Ciprofloxacino' ) 
            | (df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ) | (df['ANTIBIOTICO']== 'Cefepima' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=="Proteus penneri")  
        & ((df['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (df['ANTIBIOTICO']== 'Ciprofloxacino' ) 
            | (df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ) | (df['ANTIBIOTICO']== 'Cefepima' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Proteus spp.')  
        & ((df['ANTIBIOTICO']== 'Ampicilina' ) | (df['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Cefazolina' )
            | (df['ANTIBIOTICO']== 'Cefalotina' ) | (df['ANTIBIOTICO']== 'Cefuroxima' ) | (df['ANTIBIOTICO']== 'Cefoxitina' )
            | (df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ) | (df['ANTIBIOTICO']== 'Cefepima' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            |  (df['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=="Morganella morganii")  
        & ((df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Ceftriaxona')  
            | (df['ANTIBIOTICO']== 'Aztreonam' ) | (df['ANTIBIOTICO']== 'Cefepima' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        ((df['MICROORGANISMO']=='Citrobacter freundii') | (df['MICROORGANISMO']=='Citrobacter koseri') | (df['MICROORGANISMO']=='Citrobacter youngae') 
        | (df['MICROORGANISMO']=='Citrobacter werkmanii') | (df['MICROORGANISMO']=='Citrobacter amalonaticus')
        | (df['MICROORGANISMO']=='Citrobacter farmeri') | (df['MICROORGANISMO']=='Citrobacter braakii')) 
        & ((df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Ceftriaxona')  
            | (df['ANTIBIOTICO']== 'Aztreonam' ) | (df['ANTIBIOTICO']== 'Cefepima' ) | (df['ANTIBIOTICO']== 'Tigeciclina' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=="Serratia marcescens")  
        & ((df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Ceftriaxona')  
            | (df['ANTIBIOTICO']== 'Aztreonam' ) | (df['ANTIBIOTICO']== 'Cefepima' ) | (df['ANTIBIOTICO']== 'Tigeciclina' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=="Serratia marcescens ssp marcescens")  
        & ((df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Ceftriaxona')  
            | (df['ANTIBIOTICO']== 'Aztreonam' ) | (df['ANTIBIOTICO']== 'Cefepima' ) | (df['ANTIBIOTICO']== 'Tigeciclina' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        ((df['MICROORGANISMO']=='Aeromonas hydrophila') | (df['MICROORGANISMO']=='Aeromonas caviae')
            | (df['MICROORGANISMO']=='Aeromonas veronii bv veronii') | (df['MICROORGANISMO']=='Aeromonas veronii bv sobria') ) 
        & ((df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Ceftriaxona')  
            | (df['ANTIBIOTICO']== 'Aztreonam' ) | (df['ANTIBIOTICO']== 'Cefepima' ) | (df['ANTIBIOTICO']== 'Tigeciclina' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        ((df['MICROORGANISMO']=='Providencia rettgeri') | (df['MICROORGANISMO']=='Providencia stuartii') | (df['MICROORGANISMO']=='Providencia alcalifaciens')) 
        & ((df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Ceftriaxona')  
            | (df['ANTIBIOTICO']== 'Aztreonam' ) | (df['ANTIBIOTICO']== 'Cefepima' ) | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=="Salmonella spp.")  
        & ((df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' )
            | (df['ANTIBIOTICO']== 'Ceftriaxona') | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' )  
            | (df['ANTIBIOTICO']== 'Aztreonam' ) | (df['ANTIBIOTICO']== 'Cefepima' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        ((df['MICROORGANISMO']=='Shigella') | (df['MICROORGANISMO']=='Shigella flexneri') 
            | (df['MICROORGANISMO']=='Shigella boydii') | (df['MICROORGANISMO']=='Shigella sonnei') 
            | (df['MICROORGANISMO']=='Shigella dysenteriae') ) 
        & ((df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' )
            | (df['ANTIBIOTICO']== 'Ceftriaxona') | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' )  
            | (df['ANTIBIOTICO']== 'Aztreonam' ) | (df['ANTIBIOTICO']== 'Cefepima' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Escherichia coli')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & (df['RESISTENCIA']=='S')  & (df['ESBL (+ es blee )']=='+') , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Klebsiella pneumoniae')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & (df['RESISTENCIA']=='S')  & (df['ESBL (+ es blee )']=='+') , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Klebsiella oxytoca')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & (df['RESISTENCIA']=='S')  & (df['ESBL (+ es blee )']=='+') , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Klebsiella aerogenes')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & (df['RESISTENCIA']=='S')  & (df['ESBL (+ es blee )']=='+') , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Klebsiella ozaenae')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & (df['RESISTENCIA']=='S')  & (df['ESBL (+ es blee )']=='+') , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Proteus mirabilis')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & (df['RESISTENCIA']=='S')  & (df['ESBL (+ es blee )']=='+') , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Proteus vulgaris')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & (df['RESISTENCIA']=='S')  & (df['ESBL (+ es blee )']=='+') , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Proteus penneri')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & (df['RESISTENCIA']=='S')  & (df['ESBL (+ es blee )']=='+') , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Proteus spp.')  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & (df['RESISTENCIA']=='S')  & (df['ESBL (+ es blee )']=='+') , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Stenotrophomonas maltophilia')  
        & (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) 
        & ((df['RESISTENCIA']=='S') | (df['RESISTENCIA']=='R'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Neisseria meningitidis')  
        & ((df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ) | (df['ANTIBIOTICO']== 'Ampicilina' ) | (df['ANTIBIOTICO']== 'Penicilina G' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Neisseria gonorrhoeae')  
        & ((df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ) | (df['ANTIBIOTICO']== 'Azitromicina' ) | (df['ANTIBIOTICO']== 'Penicilina G' )
            | (df['ANTIBIOTICO']== 'Tetraciclina' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        ((df['MICROORGANISMO']== "Bacilo Gram-negativo oxidasa-negativo") | (df['MICROORGANISMO']== "Bacilo Gram-negativo oxidasa-positivo")
            |(df['MICROORGANISMO']== "Bacilo Gram-negativo no identificado no fermentador") | (df['MICROORGANISMO']== "Bacilo Gram-negativo"))  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        ((df['MICROORGANISMO']== "Bacilo Gram-negativo oxidasa-negativo") | (df['MICROORGANISMO']== "Bacilo Gram-negativo oxidasa-positivo")
            |(df['MICROORGANISMO']== "Bacilo Gram-negativo no identificado no fermentador") | (df['MICROORGANISMO']== "Bacilo Gram-negativo"))  
        & ((df['ANTIBIOTICO']== 'Ertapenem' ) | (df['ANTIBIOTICO']== 'Meropenem' ) | (df['ANTIBIOTICO']== 'Imipenem' ) | (df['ANTIBIOTICO']== 'Doripenem' ))
        & (df['RESISTENCIA']=='S')  & (df['ESBL (+ es blee )']=='+') , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        ((df['MICROORGANISMO']== "Bacilo Gram-negativo oxidasa-negativo") | (df['MICROORGANISMO']== "Bacilo Gram-negativo oxidasa-positivo")
            |(df['MICROORGANISMO']== "Bacilo Gram-negativo no identificado no fermentador") | (df['MICROORGANISMO']== "Bacilo Gram-negativo"))  
        & ((df['ANTIBIOTICO']== 'Ampicilina' ) | (df['ANTIBIOTICO']== 'Ampicilina-Sulbactam' ) | (df['ANTIBIOTICO']== 'Ciprofloxacino' ) | (df['ANTIBIOTICO']== 'Cefazolina' )
            | (df['ANTIBIOTICO']== 'Cefalotina' ) | (df['ANTIBIOTICO']== 'Cefuroxima' ) | (df['ANTIBIOTICO']== 'Cefoxitina' )
            | (df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefotaximo' ) | (df['ANTIBIOTICO']== 'Cefepima' )
            | (df['ANTIBIOTICO']== 'Piperacilina-Tazobactam' ) | (df['ANTIBIOTICO']== 'Amikacina' ) | (df['ANTIBIOTICO']== 'Gentamicina' )
            | (df['ANTIBIOTICO']== 'Tigeciclina' ) | (df['ANTIBIOTICO']== 'Nitrofurantoína' ) | (df['ANTIBIOTICO']== 'Fosfomicina c/G6P' ) 
            | (df['ANTIBIOTICO']== 'Trimetoprim-Sulfametoxazol' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Staphylococcus aureus')  
        & ((df['ANTIBIOTICO']== 'Vancomicina' ) | (df['ANTIBIOTICO']== 'Daptomicina' ) | (df['ANTIBIOTICO']== 'Linezolida' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO']=='Staphylococcus aureus')  
        & ((df['ANTIBIOTICO']== 'Vancomicina' ) | (df['ANTIBIOTICO']== 'Oxacilina' ) )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='S'))  , 1, df["Alerta"])

    df["Alerta"] = np.where(
        (df['MICROORGANISMO']=='Staphylococcus epidermidis')  
        & (df['ANTIBIOTICO']== 'Oxacilina' ) 
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='S'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        df['MICROORGANISMO'].str.contains('Staphylococcus') 
        & (df['ANTIBIOTICO']== 'Oxacilina' ) 
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='S'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        df['MICROORGANISMO'].str.contains('Enterococcus')  
        & ((df['ANTIBIOTICO']== 'Vancomicina' ) | (df['ANTIBIOTICO']== 'Ampicilina'))  
        & (df['RESISTENCIA']=='R')  , 1, df["Alerta"])
            
    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO'].str.contains('Enterococcus'))  
        & (df['ANTIBIOTICO']== 'Ampicilina')  
        & (df['RESISTENCIA']=='S')  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        df['MICROORGANISMO'].str.contains('Streptococcus') 
        & ((df['ANTIBIOTICO']== 'Vancomicina' ) | (df['ANTIBIOTICO']== 'Levofloxacino' )
            | (df['ANTIBIOTICO']== 'Ceftriaxona' ) | (df['ANTIBIOTICO']== 'Cefotaximo' )
            | (df['ANTIBIOTICO']== 'Cefepima' ) | (df['ANTIBIOTICO']== 'Eritromicina' )
            | (df['ANTIBIOTICO']== 'Moxifloxacino' ) | (df['ANTIBIOTICO']== 'Penicilina G' )
            | (df['ANTIBIOTICO']== 'Ampicilina' ) | (df['ANTIBIOTICO']== 'Amoxicilina' ))
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO'].str.contains('Candida'))    
        & (df['RESISTENCIA']=='S')  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO'].str.contains('Candida'))   
        & ((df['ANTIBIOTICO']== 'Anfotericina B' ) | (df['ANTIBIOTICO']== 'Caspofungina' )
            | (df['ANTIBIOTICO']== 'Anidulafungina' ) | (df['ANTIBIOTICO']== 'Micafungina' )
            | (df['ANTIBIOTICO']== 'Fluconazol' ) | (df['ANTIBIOTICO']== 'Itraconazol' )
            | (df['ANTIBIOTICO']== 'Voriconazol' ) | (df['ANTIBIOTICO']== 'Posaconazol' )
        )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO'].str.contains('Cryptococcus'))   
        & ((df['ANTIBIOTICO']== 'Anfotericina B' ) | (df['ANTIBIOTICO']== 'Flucitosina' )
            | (df['ANTIBIOTICO']== 'Fluconazol' ) | (df['ANTIBIOTICO']== 'Itraconazol' )
            | (df['ANTIBIOTICO']== 'Voriconazol' ) | (df['ANTIBIOTICO']== 'Posaconazol' )
        )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO'].str.contains('Cryptococcus')) &   
        (df['RESISTENCIA']=='S')  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO'].str.contains('Aspergillus'))   
        & ((df['ANTIBIOTICO']== 'Anfotericina B' ) | (df['ANTIBIOTICO']== 'Caspofungina' )
            | (df['ANTIBIOTICO']== 'Anidulafungina' ) | (df['ANTIBIOTICO']== 'Micafungina' )
        )
        & ((df['RESISTENCIA']=='R') | (df['RESISTENCIA']=='I'))  , 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        (df['MICROORGANISMO'].str.contains('Aspergillus'))
        &    
        (df['RESISTENCIA']=='S')  , 1, df["Alerta"])

    df["Alerta"] = np.where(  (df["Alerta"] == 0) &
        df['MICROORGANISMO'].str.contains('Fusariums'), 1, df["Alerta"])

    df["Alerta"] = np.where(  (df["Alerta"] == 0) &
        df['MICROORGANISMO'].str.contains('Bacillus'), 1, df["Alerta"])

    df["Alerta"] = np.where(  (df["Alerta"] == 0) &
        df['MICROORGANISMO'].str.contains('Rhizo'), 1, df["Alerta"])

    df["Alerta"] = np.where(  (df["Alerta"] == 0) &
        df['MICROORGANISMO'].str.contains('Burkholderia'), 1, df["Alerta"])

    df["Alerta"] = np.where( (df["Alerta"] == 0) &
        df['MICROORGANISMO'].str.contains('Clostridioides'), 1, df["Alerta"])
    
    return df["Alerta"]
