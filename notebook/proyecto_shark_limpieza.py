import pandas as pd

pd.set_option('display.max_columns', None)

import numpy as np

import warnings

warnings.simplefilter('ignore')

import pylab as plt
import seaborn as sns

# Leo el archivo

data = pd.read_csv('../Data/attacks.csv', encoding='latin1')

# Modifico el nombre de las columnas a minúsculas y le quito los espacios.

data.columns = [c.lower().replace(' ', '_') for c in data.columns]
data.columns = [c.lower().replace(':', '') for c in data.columns]
data.columns = [c.lower().replace('.', '_') for c in data.columns]
data.columns = [c.lower().replace('(', '') for c in data.columns]
data.columns = [c.lower().replace(')', '') for c in data.columns]
data.columns = [c.lower().replace('/', '_') for c in data.columns]

# Me creo un subset con las filas que tiene al menos un dato.

subset = data[data.notna().any(axis=1)]

# Sustituyo todos los valores de la columna unnamed_22 y unnamed_23

subset.unnamed_22 = 'unknown'
subset.unnamed_23 = 'unknown'

# Creo un dataset en la que elimino columnas con las que quiero filtras.

filters_cols = subset.columns.drop(['case_number', 'original_order', 'unnamed_22', 'unnamed_23'])

# Me creo un dataset más limpio con el que voy a seguir trabajando

subset1 = subset[subset[filters_cols].notnull().any(axis=1)]

# Empiezo a analizar mi subset y limpiar
# Remplazo los valores nulos en la columna case_number con "unknown"

subset1.case_number.fillna("unknown", inplace=True)

# Remplazo en date "Reported" por ""

subset1.date = subset1.date.str.replace("Reported", "")

# Remplazo en year valores nulos por 0 y ambio el dtype de "object" a "int16"

subset1.year.fillna(0, inplace=True)
subset1.year = subset1.year.astype(dtype='int16')

# Remplazo ciertos valores en type

subset1.type = subset1.type.str.replace("Boating", "Boat")
subset1.type = subset1.type.str.replace("Boatomg", "Boat")
subset1.type.fillna("Questionable", inplace=True)

# Relleno en country con "unknown" los valores nulos

subset1.country.fillna("unknown", inplace=True)

# Relleno en area con "unknown" los valores nulos

subset1.area.fillna("unknown", inplace=True)

# Relleno en location con "unknown" los valores nulos

subset1.location.fillna("unknown", inplace=True)

# Relleno en activity con "unknown" los valores nulos

subset1.activity.fillna("unknown", inplace=True)

# Convierto a minusculas y sustituyo varios datos con contain en activity

subset1.activity = subset1.activity.str.lower()
subset1.activity[subset1.activity.str.contains('surf')] = 'surfing'
subset1.activity[subset1.activity.str.contains('swi')] = 'swimming'
subset1.activity[subset1.activity.str.contains('div')] = 'diving'
subset1.activity[subset1.activity.str.contains('bath')] = 'bathing'
subset1.activity[subset1.activity.str.contains('fish')] = 'fishing'
subset1.activity[subset1.activity.str.contains('boat')] = 'boating'

# Relleno en name con "unknown" los valores nulos


subset1.name.fillna("unknown", inplace=True)

# Relleno en sex_ con "unknown" los valores nulos y modifico valores

subset1.sex_.fillna("unknown", inplace=True)

subset1.sex_ = subset1.sex_.str.replace("M", "Male")
subset1.sex_ = subset1.sex_.str.replace("F", "Female")
subset1.sex_ = subset1.sex_.str.replace("N", "unknown")
subset1.sex_ = subset1.sex_.str.replace("lli", "unknown")
subset1.sex_ = subset1.sex_.str.replace(".", "unknown")
subset1.sex_ = subset1.sex_.str.replace(" ", "")

# Relleno en age con "0" los valores nulos

subset1.age.fillna("0", inplace=True)

# Uso regex para filtrar en data set los datos que contienen datos que no son numerico '\D'

subset1.age[subset1.age.str.contains(r'\D')] = "0"

# Cambiar el tipo de dtype de "object" a "integer"

subset1.age = subset1.age.astype(dtype='int8')

# Relleno en injury con "unknown" los valores nulos

subset1.injury.fillna("unknown", inplace=True)

# Relleno en fatal_y_n con "unknown" los valores nulos y remplazo valores

subset1.fatal_y_n.fillna("unknown", inplace=True)

subset1.fatal_y_n = subset1.fatal_y_n.str.replace(" ", "")
subset1.fatal_y_n = subset1.fatal_y_n.str.upper()
subset1.fatal_y_n = subset1.fatal_y_n.str.replace("M", "UNKNOWN")
subset1.fatal_y_n = subset1.fatal_y_n.str.replace("2017", "UNKNOWN")

# Relleno en time con "unknown" los valores nulos

subset1.time.fillna("unknown", inplace=True)

# Relleno en species_ con "unknown" los valores nulos

subset1.species_.fillna("unknown", inplace=True)

# Relleno en investigator_or_source con "unknown" los valores nulos

subset1.investigator_or_source.fillna("unknown", inplace=True)

# Relleno en href_formula con "unknown" los valores nulos

subset1.href_formula.fillna("unknow", inplace=True)

# Me creo una copia del data original

data_clean = data.copy()

# Filtro en el original con el índice del subset y sobreescribo con el subset

data_clean.iloc[subset1_index] = subset1

# Creo diccionario con los valores por columna

values_isna = {'case_number': "unknown", 'date': "unknown", 'year': 0, 'type': "unknown", 'country': "unknown",
               'area': "unknown", 'location': "unknown",
               'activity': "unknown", 'name': "unknown", 'sex_': "unknown", 'age': "0", 'injury': "unknown",
               'fatal_y_n': "unknown", 'time': "unknown",
               'species_': "unknown", 'investigator_or_source': "unknown", 'pdf': "unknown", 'href_formula': "unknown",
               'href': "unknown",
               'case_number_1': "unknown", 'case_number_2': "unknown", 'original_order': 0, 'unnamed_22': "unknown",
               'unnamed_23': "unknown"}

# Sustituyo los valores nulos, con los valores del diccionario

data_clean.fillna(values_isna, inplace=True)

# Sustituyo el tipo de dato en year y age con "int16"


data_clean.year = data_clean.year.astype(dtype='int16')
data_clean.age = data_clean.age.astype(dtype='int16')

# Exporto una copia del dataframe limpio

# data_clean.to_csv("../Data/attacks_clean.csv", sep= ",", index=False)

# Exporto una copia del subset para analizar

# subset1.to_csv("../Data/attacks_analys.csv", sep= ",", index=False)

