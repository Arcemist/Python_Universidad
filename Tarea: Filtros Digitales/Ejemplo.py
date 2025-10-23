# Ejemplo proveido por el profesor:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.random.seed(5)
#y = np.array([10,123,5,23,132,5421,4,321,41,123,4,1231,4,12314,123])
y = np.random.random(100)
#x = np.arange(100)
print(y)
df = pd.DataFrame(y, columns=["valores"])
ventanilla = 20
df["Promedio"] = df["valores"].rolling(window=ventanilla).mean()
plt.title("Gráfica")
plt.xlabel("Muestras")
plt.ylabel("Valores")
plt.plot(y)
plt.plot(df["Promedio"])
#plt.scatter(y,x, color="black", alpha=0.5)
plt.show()
