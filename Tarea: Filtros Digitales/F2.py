# Segundo Filtro:
# Se cambio el uso de media por el maximo.
# Y se cambio la ventana de filtrado de 20 a 5 valores.

# Este filtro muestra el valor mas alto de las ultimas 5 muestras.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creacion de datos randomizados
np.random.seed(5)
valores = np.random.random(100)
df = pd.DataFrame(valores, columns=["valores"])

# Filtro:
df["Maximo"] = df["valores"].rolling(window = 5).max()

# Presentacion del grafico:
plt.title("Gráfica Filtro 2")
plt.xlabel("Muestras")
plt.ylabel("Valores")
plt.plot(df["valores"])
plt.plot(df["Maximo"])
plt.show()
