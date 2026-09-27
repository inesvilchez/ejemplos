import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)

plt.title("Funcion seno")
plt.xlabel("x")
plt.ylabel("sin(x)")

plt.savefig("grafico_seno.png")

print("Grafico")
import pandas as pd

ventas_enero = pd.DataFrame({
    "producto": ["A", "B"],
    "unidades": [10, 5]
})

ventas_febrero = pd.DataFrame({
    "producto": ["A", "C"],
    "unidades": [7, 3]
})

ventas_totales = pd.concat(
    [ventas_enero, ventas_febrero],
    ignore_index=True
)

print(ventas_totales)
