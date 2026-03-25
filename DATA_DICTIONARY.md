# Diccionario de Datos

## Impacto de la Inteligencia Artificial en el Mercado Laboral de América Latina (2020-2025)

### automatizacion_sectores.csv
| Campo | Tipo | Descripción |
|-------|------|-------------|
| pais | string | País de América Latina |
| sector | string | Sector económico |
| año | integer | Año de referencia |
| indice_automatizacion | float | Índice 0-1 de riesgo de automatización |
| empleos_en_riesgo_pct | float | % de empleos en riesgo |

### desplazamiento_laboral.csv
| Campo | Tipo | Descripción |
|-------|------|-------------|
| pais | string | País |
| año | integer | Año proyectado |
| empleos_desplazados | integer | Número de empleos desplazados |
| escenario | string | Optimista/Base/Pesimista |

### nuevas_ocupaciones.csv
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ocupacion | string | Nombre de la nueva ocupación |
| demanda_crecimiento_pct | float | % de crecimiento proyectado |
| habilidades_requeridas | string | Lista de habilidades |

### politicas_laborales.csv
| Campo | Tipo | Descripción |
|-------|------|-------------|
| pais | string | País |
| politica | string | Descripción de la política |
| tipo | string | Regulación/Incentivo/Formación |
| año_implementacion | integer | Año de implementación |