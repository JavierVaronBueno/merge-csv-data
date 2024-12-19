# Procesador de Datos CSV con Logging Robusto y Manejo de Errores

Un script basado en Python para procesar y combinar archivos CSV. Diseñado para integradores de datos y desarrolladores, este script incluye un sistema de logging robusto, manejo de errores y gestión flexible de archivos para simplificar las tareas de preprocesamiento de datos.

---

## Características

### 1. **Sistema de Logging Robusto**
- Genera archivos de registro detallados con marcas de tiempo para cada ejecución del script.
- Los logs incluyen información sobre archivos procesados, columnas faltantes y errores.
- Facilita la depuración y auditoría del flujo de procesamiento de datos.

### 2. **Gestión de Archivos**
- Utiliza **expresiones regulares (regex)** para identificar y procesar archivos CSV según patrones definidos por el usuario.
- Maneja inconsistencias en los nombres de los archivos, como números añadidos (por ejemplo, `archivo(1).csv`).

### 3. **Procesamiento de Datos**
- Estandariza los nombres de columnas utilizando un mapeo predefinido (`COLUMN_MAPPING`).
- Detecta y analiza automáticamente columnas de fechas.
- Elimina filas duplicadas basándose en la columna `Date`.
- Genera un archivo CSV combinado y limpio para cada patrón procesado.

### 4. **Manejo de Errores**
- Captura y registra errores específicos de cada archivo para garantizar que los demás archivos continúen procesándose.
- Advierte sobre columnas requeridas faltantes y omite archivos inválidos de manera segura.

---

## Requisitos del Sistema
- **Python**: 3.7 o superior
- Librerías de Python necesarias:
  - `pandas`
  - `logging`
  - `datetime`
  - `re`

---

## Configuración del Entorno Virtual

### Paso 1: Crear un Entorno Virtual
```bash
# Windows
python -m venv venv

# Linux/Mac
python3 -m venv venv
```

### Paso 2: Activar el Entorno Virtual
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Paso 3: Instalar las Dependencias
1. Crea un archivo llamado `requirements.txt` con el siguiente contenido:
    ```text
    pandas>=2.0.0
    python-dateutil>=2.8.2
    pytz>=2023.3
    ```
2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

---

## Ejecución del Script

### Paso 1: Estructura del Proyecto
Organiza tu proyecto de la siguiente manera:
```
project_root/
├── venv/                   # Entorno virtual
├── requirements.txt        # Dependencias
├── csv_merger.py           # Script principal
└── data/                   # Directorio con los archivos CSV
    └── tus_archivos_csv/
```

### Paso 2: Ejecutar el Script
```bash
python csv_merger.py
```
- Asegúrate de activar el entorno virtual antes de ejecutar el script.
- Actualiza las variables `directory` y `patterns` en el script para apuntar a tu directorio de datos y patrones de archivos deseados.

---

## Estructura del Proyecto
```
project_root/
├── venv/                   # Entorno virtual
├── requirements.txt        # Dependencias
├── csv_merger.py           # Script principal
├── logs/                   # Archivos de log
├── data/                   # Directorio con los archivos CSV
└── output/                 # Directorio para los archivos procesados
```

---

## Ejemplo de Uso

### Configuración de Variables
En `csv_merger.py`, configura:
- `directory_data` con la ruta donde están tus archivos CSV.
- `directory_output` con la ruta donde se guardaran tus archivos CSV.
- `patterns` como una lista de patrones base de nombres de archivo. Ejemplo:
    ```python
    directory_data = r"c:\Users\TuUsuario\data"
    directory_output = r"c:\Users\TuUsuario\output"
    patterns = ["USD_THB Historical Data", "EUR_USD Historical Data"]
    ```

### Ejecutar el Script
1. Activa el entorno virtual:
    ```bash
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # Linux/Mac
    ```
2. Ejecuta el script:
    ```bash
    python csv_merger.py
    ```

### Resultados
- Se generará un archivo CSV combinado llamado `<pattern>_TOTAL.csv` en el directorio especificado.
- Los logs detallados se almacenan en la carpeta `logs/`.

---

## Cómo Contribuir
Si deseas contribuir al proyecto:
1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad:
    ```bash
    git checkout -b nombre-de-la-funcionalidad
    ```
3. Realiza tus cambios y envía un pull request.

---

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## Contacto
Si tienes preguntas, sugerencias o necesitas ayuda:
- **Correo Electrónico**: soporte_desarrolladores@example.com
- **Issues en GitHub**: [GitHub Issues](https://github.com/tu-repositorio/issues)
