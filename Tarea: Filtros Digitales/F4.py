# Cuarto Filtro:
# Se cambio el uso de Media por el filtro de kurt
# este se usa para detectar la variacion de un set
# de numeros entre si mismo.
# Y se cambio la ventana de muestrado a 10 para
# que sea mas sensible el filtro.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creacion de datos randomizados
np.random.seed(5)
valores = np.random.random(100)
df = pd.DataFrame(valores, columns=["valores"])

# Filtro:
df["Kurt"] = df["valores"].rolling(window = 10).kurt()

# Presentacion del grafico:
plt.title("Gráfica Filtro 4")
plt.xlabel("Muestras")
plt.ylabel("Valores")
plt.plot(df["valores"])
plt.plot(df["Kurt"])
plt.show()
