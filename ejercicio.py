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
