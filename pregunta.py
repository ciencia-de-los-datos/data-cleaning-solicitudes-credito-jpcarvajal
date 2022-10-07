"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
from enum import unique
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    
    df.dropna(inplace=(True))
    df.drop(['Unnamed: 0'], axis=1, inplace=(True))

    #SEXO
    df.sexo = df.sexo.str.lower()
    #print(df.sexo.value_counts())

    #EMPRENDIMIENTO
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    #print(df.tipo_de_emprendimiento.value_counts())

    #IDEA DE NEGOCIO
    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.replace("-","_")
    df.idea_negocio = df.idea_negocio.str.replace(" ","_")
    df.idea_negocio = df.idea_negocio.str.rstrip("_")
    #df=df.sort_values('idea_negocio')
    #print(df.idea_negocio.value_counts())

    #BARRIO
    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.str.replace(" ","_")
    df.barrio = df.barrio.str.replace("-","_")
    #df.barrio = df.barrio.str.rstrip("_")
    
    #df=df.sort_values('barrio')
    #print(len(df.barrio.unique()))

    #ESTRATO
    #print(df.estrato.value_counts())

    #COMUNA
    df = df.dropna(axis=0, subset=['comuna_ciudadano'])
    #print(df[(df.comuna_ciudadano.isnull())])

    #FECHA
    #!!!!!!!!!!!!!!!!!!!!!!!!Preguntar cómo se debería hacer, el ignore no funciona?
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)
    #print(df.fecha_de_beneficio.value_counts())

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Preguntar por qué con dayfirst funciona diferente a con strftime, usar sets para ver la diferencia
    """     df.fecha_de_beneficio = df.fecha_de_beneficio.dt.strftime('%Y-%m-%d')
    df=df.sort_values('fecha_de_beneficio')
    print(df.fecha_de_beneficio.unique()) """

    #MONTO DEL CREDITO
    df.monto_del_credito = df.monto_del_credito.str.replace(r"[^\d\.]", "", regex = True).astype(float)
    #print(df.monto_del_credito.value_counts())

    #LINEA DE CREDITO
    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.str.replace("-","_")
    df.línea_credito = df.línea_credito.str.replace(" ","_")
    df.línea_credito = df.línea_credito.str.rstrip("_")
    #print(df.línea_credito.value_counts())

    df.drop_duplicates(inplace=(True))
    return df

#print(clean_data())
clean_data()
