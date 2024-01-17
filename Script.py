# %% [markdown]
# ### Conversión de Unidades 

# %% [markdown]
# este programa realiza la conversión de 10 diferentes unidades en donde el usuario ingresa el tipo de conversión a realizar y la unidad a comvertir y recibe como respuesta el valor correspondiente a la unidad deseada. 
# el programa debe ser capaz de comvertir de: 
# - kilómetros a millas y millas a kilómetros 
# - metros a pies y pies a metros 
# - centímetros a pulgadas y pulgadas a centímetros 
# - gramos a onzas y onzas a gramos 
# - grados centígrados a fahrenheit y de fahrenheit a grados centígrados 

# %% [markdown]
# ### Kilómetros a millas y millas a kilómetros 

# %%
def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

def miles_to_km(miles):
    kilometers = miles / 0.621371
    return kilometers

# Ejemplos de uso
km_value = 10
miles_result = km_to_miles(km_value)
print(f"{km_value} kilometros son {miles_result:.2f} millas")

miles_value = 5
km_result = miles_to_km(miles_value)
print(f"{miles_value} millas son {km_result:.2f}  kilometros")

# %% [markdown]
#  ### metros a pies y pies a metros 

# %%
def metros_a_pies(metros):
    pies = metros * 3.28084
    return f"{pies} pies"

# %%
metros_a_pies(10)

# %%
def pies_a_metros(pies):
    metros = pies / 3.28084
    return metros

# %%
pies = 30
pies = metros_a_pies(pies)
print(f"{pies} pies son equivalente a {metros} pies. ")

# %%
metros = 10
pies = metros_a_pies(metros)
print(f"{metros} metros son equivalente a {pies} pies. ")

# %%
def gramos_a_onzas(gramos):
    onzas = gramos * 0.035274
    return onzas

# %% [markdown]
# ### centímetros a pulgadas y pulgadas a centímetros

# %%


# %% [markdown]
#  ### gramos a onzas y onzas a gramos 

# %%
def gramos_a_onzas(gramos):
    onzas = gramos * 0.035274
    return onzas

# %%
def onzas_a_gramos(onzas):
    gramos = onzas / 0.035274
    return gramos

# %%
gramos = 100
onzas = gramos_a_onzas(gramos)
print(f"{gramos} gramos son equivalentes a {onzas} onzas. ")

# %%
onzas = 5
gramos = onzas_a_gramos(gramos)
print(f"{onzas} onzas son equivalentes a {gramos} gramos. ")

# %% [markdown]
# ### grados centígrados a fahrenheit y de fahrenheit a grados centígrados 

# %%

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Ejemplos de uso
celsius_value = 25
fahrenheit_result = celsius_to_fahrenheit(celsius_value)
print(f"{celsius_value} grados Celsius son {fahrenheit_result:.2f} grados Fahrenheit")

fahrenheit_value = 77
celsius_result = fahrenheit_to_celsius(fahrenheit_value)
print(f"{fahrenheit_value} grados Fahrenheit son {celsius_result:.2f} grados Celsius")



