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
    

    #SEXO
    sexo_df = pd.DataFrame({'sexo':list(df.sexo)})
    sexo_df.sexo = sexo_df.sexo.str.lower()
    sexo_df = sexo_df.drop_duplicates()
    df.sexo = df.sexo.str.lower()
    #print(df.sexo.value_counts())

    #EMPRENDIMIENTO
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! falta
    #print('emprendimiento '+str(len(df[df.tipo_de_emprendimiento.isna()])))
    #print(df.tipo_de_emprendimiento.value_counts())

    #IDEA DE NEGOCIO
    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.replace("-","_")
    df.idea_negocio = df.idea_negocio.str.replace(" ","_")
    df.idea_negocio = df.idea_negocio.str.rstrip("_")
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! falta
    #print('barrio '+str(len(df[df.barrio.isna()])))
    #df=df.sort_values('idea_negocio')
    #print(df.idea_negocio.value_counts())

    #BARRIO
    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.str.replace(" ","_")
    df.barrio = df.barrio.str.replace("-","_")
    df.barrio = df.barrio.str.rstrip("_")
    #df=df.sort_values('barrio')
    #print(len(df.barrio.unique()))

    #ESTRATO
    #print(df.estrato.value_counts())

    #COMUNA
    #print('comuna '+str(len(df[(df.comuna_ciudadano.isnull())])))
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
    df.monto_del_credito = df.monto_del_credito.str.replace(r"[^\d\.]", "", regex = True)
    #print(df.monto_del_credito.value_counts())

    #LINEA DE CREDITO
    print(df.línea_credito.value_counts())

    return df

#print(clean_data())
clean_data()

