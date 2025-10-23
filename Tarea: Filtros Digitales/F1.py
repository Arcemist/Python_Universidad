# Primer Filtro:
# Se cambio el uso de media por mediana.

# Este filtro es bastante parecido al del ejemplo,
# pero se ve afectado menos por valores extremos.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creacion de datos randomizados
np.random.seed(5)
valores = np.random.random(100)
df = pd.DataFrame(valores, columns=["valores"])

# Filtro:
df["Mediana"] = df["valores"].rolling(window = 20).median()

# Presentacion del grafico:
plt.title("Gráfica Filtro 1")
plt.xlabel("Muestras")
plt.ylabel("Valores")
plt.plot(df["valores"])
plt.plot(df["Mediana"])
plt.show()
