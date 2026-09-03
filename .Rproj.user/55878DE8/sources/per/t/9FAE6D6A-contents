# cargar librerias
library(here)
library(readr)

archivo <- "cantidad_de_residuos_en_la_estacion_de_transferencia_2023.csv"
ruta_csv <- here("data", archivo)

if (!file.exists(ruta_csv)) {
  stop(paste("No se encontró el archivo en:", ruta_csv))
}

df <- read_csv(ruta_csv)

# 4. Inspección inicial de 
cat("--- Archivo cargado exitosamente desde:", basename(ruta_csv), "---\n")
print(spec(df))  # Muestra el tipo de dato asignado a cada columna
head(df)

str(df)

length(unique(df$matricula_letra))

## La columna identificadora es "pesada"
