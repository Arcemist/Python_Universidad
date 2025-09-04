import matplotlib.pyplot as plt
import pandas
import seaborn
import numpy

# El dataset en 'Gender' codifica '0' como Hombre y '1' como Mujer

#stress_dt = pandas.read_csv("./dataset/Stress_Dataset.csv")
stress_lv_dt = pandas.read_csv("./dataset/StressLevelDataset.csv")

plt.figure(1).subplots_adjust(
    wspace=0.5,
    hspace=0.6
)
plt.subplot(2, 3, 1)
heatmap, xedges, yedges = numpy.histogram2d(
    stress_lv_dt["sleep_quality"],
    stress_lv_dt["blood_pressure"],
    bins=6
)
plt.imshow(
    heatmap.T,
    origin="lower",
    cmap="viridis",
    aspect="auto"
)
plt.colorbar(label="Cantidad")
plt.title("Presion Sanguinea\n segun\n Calidad de Sueño")
plt.xlabel("Calidad de Sueño")
plt.ylabel("Presion Sanguinea")



plt.subplot(2 ,3 ,2)
heatmap, xedges, yedges = numpy.histogram2d(
    stress_lv_dt["sleep_quality"],
    stress_lv_dt["anxiety_level"],
    bins=6
)
plt.imshow(
    heatmap.T,
    origin="lower",
    cmap="viridis",
    aspect="auto"
)
plt.colorbar(label="Cantidad")
plt.title("Ansiedad\n segun\n Calidad de Sueño")
plt.xlabel("Calidad de Sueño")
plt.ylabel("Ansiedad")



plt.subplot(2 ,3 ,3)
heatmap, xedges, yedges = numpy.histogram2d(
    stress_lv_dt["anxiety_level"],
    stress_lv_dt["self_esteem"],
    bins=10
)
plt.imshow(
    heatmap.T,
    origin="lower",
    cmap="viridis",
    aspect="auto"
)
plt.colorbar(label="Cantidad")
plt.title("Autoestima\n segun\n Ansiedad")
plt.xlabel("Ansiedad")
plt.ylabel("Autoestima")



plt.subplot(2 ,3 ,4)
heatmap, xedges, yedges = numpy.histogram2d(
    stress_lv_dt["living_conditions"],
    stress_lv_dt["breathing_problem"],
    bins=6
)
plt.imshow(
    heatmap.T,
    origin="lower",
    cmap="viridis",
    aspect="auto"
)
plt.colorbar(label="Cantidad")
plt.title("Problemas Respiratorios\n segun\n Condicion de Vivienda")
plt.xlabel("Condicion de Vivienda")
plt.ylabel("Problemas Respiratorios")



plt.subplot(2 ,3 ,5)
heatmap, xedges, yedges = numpy.histogram2d(
    stress_lv_dt["blood_pressure"],
    stress_lv_dt["headache"],
    bins=6
)
plt.imshow(
    heatmap.T,
    origin="lower",
    cmap="viridis",
    aspect="auto"
)
plt.colorbar(label="Cantidad")
plt.title("Dolores de Cabeza\n segun\n Presion Sanguinea")
plt.xlabel("Presion Sanguinea")
plt.ylabel("Dolores de Cabeza")



plt.subplot(2 ,3 ,6)
heatmap, xedges, yedges = numpy.histogram2d(
    stress_lv_dt["noise_level"],
    stress_lv_dt["sleep_quality"],
    bins=6
)
plt.imshow(
    heatmap.T,
    origin="lower",
    cmap="viridis",
    aspect="auto"
)
plt.colorbar(label="Cantidad")
plt.title("Calidad de Sueño\n segun\n Niveles de ruido")
plt.xlabel("Niveles de Ruido")
plt.ylabel("Calidad de Sueño")

plt.show()
