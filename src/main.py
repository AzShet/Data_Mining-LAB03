#!/usr/bin/env python
# coding: utf-8

# # ALMACENAMIENTO DE DATOS
# ARQUITECTURA DE UN DATA WAREHOUSE. CARGA Y MANTENIMIENTO. CUBOS DE DATOS

# 1. Imporatamos la data
import pandas as pd
import numpy as np # numpy will be used in preprocess_data, ensure it's imported
from timeit import timeit # timeit is used later
import os # os is used later
# pyperclip is removed as it's notebook specific utility for clipboard

from data_utils import load_and_combine_data, save_data_to_excel, save_data_to_csv, preprocess_data

# Load data using the utility function
combined_data = load_and_combine_data(repo_id=19)

# Save data to Excel using the utility function
# Note: The original notebook saved this in the root.
# Consider if it should be saved in 'data/' directory. For now, keeping original behavior.
save_data_to_excel(combined_data, "car_evaluation_data.xlsx")

# metadata and variable information can be accessed via the initially loaded object if needed
# car_evaluation = fetch_ucirepo(id=19) # This line is implicitly handled by load_and_combine_data
# print(car_evaluation.metadata)
# print(car_evaluation.variables)

# print(combined_data) # This was for debugging, can be kept or removed


# 4. Extraer nombres de los atributos

# In[7]:

# list(car_evaluation) # car_evaluation object is not directly available here anymore
# If feature names are needed, they can be accessed from combined_data or by modifying load_and_combine_data

# In[8]:


list(combined_data)


# In[9]:


import pandas as pd


# In[10]:


list(combined_data.columns)


# In[11]:


combined_data.columns.tolist()


# In[12]:


list(combined_data.columns.values)


# 5. Para medir el rendimiento de los métodos anteriores en términos de tiempo podemos usar la función ‘timeit’ de la librería ‘timeit’.

# In[13]:

# from timeit import timeit # Already imported at the top

# In[14]:


t1 = timeit(lambda: list(combined_data))
print(t1)


# In[15]:


t2 = timeit(lambda: list(combined_data.columns))
print(t2)


# In[16]:


t3 = timeit(lambda: combined_data.columns.tolist())
print(t3)


# In[17]:


t4 = timeit(lambda: list(combined_data.columns.values))
print(t4)


# In[18]:


print(t1,t2,t3,t4)


# 6.	Usando el método ‘dtype’ para cada atributo, podemos ver su naturaleza. Si quisiéramos ver esto para todos los atributos, usaremos el método ‘dtypes’.

# In[19]:


combined_data['buying'].dtype


# In[20]:


combined_data['persons'].dtype


# In[21]:


combined_data.dtypes


# 7.	Observamos la cantidad de categorías de un atributo mediante el método ‘unique( )’.

# In[22]:


combined_data["doors"].unique


# 8.	Si en el paso anterior, la naturaleza de los atributos no coincide en cómo se está definiendo en el repositorio web, podemos cambiar esto por medio del método ‘astype( )’ aplicado sobre el atributo junto con su tipo.

# In[23]:
# Preprocessing steps are now handled by preprocess_data function
combined_data = preprocess_data(combined_data)

# In[24]:

# combined_data.astype # This line just showed the dtypes, can be replaced by print(combined_data.dtypes) if needed

# 9.	Para cambiar el nombre a las categorías debemos importar la librería ‘numpy’ que trabaja con arreglos y luego utilizar el método ‘where( )’ indicando al atributo de la data, el nuevo nombre para cada categoría.

# In[25]:

# import numpy as np # Already imported at the top

# In[26]:

# The following lines are now part of preprocess_data:
# combined_data["lug_boot"]=np.where(combined_data["lug_boot"]=="small", "pequeño", combined_data["lug_boot"])
# combined_data["lug_boot"]=np.where(combined_data["lug_boot"]=="med", "mediano", combined_data["lug_boot"])
# combined_data["lug_boot"]=np.where(combined_data["lug_boot"]=="big", "grande", combined_data["lug_boot"])
# combined_data["lug_boot"].unique # This was to show unique values, can be replaced by print(combined_data["trunk"].unique())


# 10.	Con el método ‘.value_count( )’ podemos contabilizar las frecuencias de cada categoría.

# In[27]:


combined_data["doors"].value_counts(dropna=False)


# 11.	También podemos juntar dos o más categorías mediante el método ‘where’ escribiendo la misma categoría para las que son diferentes.

# In[28]:
# These lines are now part of preprocess_data:
# combined_data["doors"] = np.where(combined_data["doors"]=="2", "3 a menos", combined_data["doors"])
# combined_data["doors"] = np.where(combined_data["doors"]=="3", "3 a menos", combined_data["doors"])

# In[29]:

# combined_data["doors"] = np.where(combined_data["doors"]=="4", "4 a más", combined_data["doors"])
# combined_data["doors"] = np.where(combined_data["doors"]=="5more", "4 a más", combined_data["doors"])

# In[30]:

# combined_data["doors"].unique() # This was to show unique values, can be replaced by print(combined_data["doors"].unique())


# 12.	Otra forma de cambiar los nombres de los encabezados es mediante el método ‘rename’ escribiendo en forma de diccionario, el nombre de la variable a cambiar (‘lug_boot’) y luego el nuevo nombre (‘trunk’). Además, debemos asignar el valor ‘axis=1’ y si queremos cambiar nombres a las filas usamos ‘axis=0’.

# In[31]:
# This is now part of preprocess_data:
# combined_data.rename({'lug_boot':'trunk'}, axis=1, inplace=True)
# combined_data # Displaying dataframe, can be replaced with print(combined_data) if needed


# 13.	Para determinar la cantidad de registros y atributos utilizamos el método ‘shape( )’; asimismo, con los métodos ‘head( )’ y ‘tail( )’, podemos ver los 5 primeros y últimos registros, respectivamente.

# In[32]:


# n de registros y atributos
combined_data.shape


# In[33]:


combined_data.head()


# In[34]:


combined_data.tail()


# 14.	Con el método ‘iloc’ podemos extraer una parte de nuestra data a manera de filas y columnas.

# In[35]:


combined_data.iloc[0:3, 1:4]


# 15.	Para extraer registros en particular, podemos hacer uso de los corchetes ([ ]) especificando dentro de estos los registros que necesitamos.

# In[36]:


combined_data.loc[[0,10],:]


# 16.	Con relación a lo anterior, también se pueden utilizar los corchetes para extraer los datos de un atributo o más de uno, colocando para ello sus nombres.

# In[37]:


combined_data.loc[0:20,['doors', 'persons']]


# 17.	También se pueden utilizar los corchetes para extraer los datos de una categoría en particular de un atributo.

# In[38]:


combined_data[combined_data.buying=='vhigh']


# 18.	Utilizando operadores lógicos, se pueden combinar condiciones y aplicar lo anterior.

# In[39]:


combined_data[(combined_data.safety=='med') | (combined_data.safety=='high')]


# 19.	Por último, si deseamos exportar nuestro documento a un csv adicionándole la ruta donde queremos guardar nuestro documento.

# In[40]:

# import os # Already imported
# import pyperclip # Removed

# copiamos el directorio actual

# In[41]:

# directorio_actual = os.getcwd() # This can be kept if needed for some local path construction
# print(directorio_actual)

# In[42]:

# The pyperclip functionality is removed as it's notebook specific
# directorio_esc = directorio_actual.replace("\\", "\\\\")
# pyperclip.copy(directorio_esc)
# print(f"El directorio escapado '{directorio_esc}' se ha copiado al portapapeles.")


# aplicamos la ruta

# In[43]:

# ruta='C:\\TECSUP\\5-tecsup\\Mineria de Datos\\Semana (3)\\LAB\\combined_data.csv' # Example of a fixed local path

# In[44]:

### combined_data.to_csv(ruta) # This was commented out
# invalido porque arroja los datos en mal formato


# HACEMOS UNA CORRECIÓN DE FORMATOS CON ucimlrepo

# In[45]:

# from ucimlrepo import fetch_ucirepo # Not needed here anymore

# In[46]:

# fetch dataset
# car_evaluation = fetch_ucirepo(id=19) # Not needed here anymore


# In[50]:

# Save data to CSV using the utility function
# Note: The original notebook saved this in the root.
# It was previously moved to data/DATA_FORMATEADA.csv.
# To align with previous subtask, it should be data/DATA_FORMATEADA.csv
save_data_to_csv(combined_data, "data/DATA_FORMATEADA.csv", encoding="ISO-8859-1")
# The print statement in the original was slightly different, now standardized by the function.


# 20.	A continuación, se muestran los métodos más importantes que existen para importar y exportar datos en Python.

# The HTML table is removed as it's for display in notebook, not for a script.
# from IPython.display import HTML
#
# tabla_html = """
# ...
# """
#
# HTML(tabla_html)
