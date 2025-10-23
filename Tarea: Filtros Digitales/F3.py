# Tercer Filtro:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creacion de datos randomizados
np.random.seed(5)
valores = np.random.random(100)
df = pd.DataFrame(valores, columns=["valores"])

# Filtro:
df["Minimo"] = df["valores"].rolling(window = 5).min()

# Presentacion del grafico:
plt.title("Gráfica Filtro 3")
plt.xlabel("Muestras")
plt.ylabel("Valores")
plt.plot(df["valores"])
plt.plot(df["Minimo"])
plt.show()
