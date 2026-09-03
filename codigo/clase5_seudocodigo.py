import pandas as pd

# 1. Crear el vector con datos
temperaturas = [18, 22, 15, 25, 30]

# Confirmar si está el vector
print(temperaturas)

# 2. Crear el vector para los datos filtrados
temperaturas_filtradas = []

# Hacer que vaya viendo cada elemento (temp) del vector temperaturas para que encuentre los mayores a 20 y los ponga en
# el vector temperaturas_filtradas
for temp in temperaturas:
    if temp > 20:
        temperaturas_filtradas.append(temp)

# 3. Mostrar los datos filtrados
print(temperaturas_filtradas)