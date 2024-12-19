import os
import pandas as pd
import logging
from datetime import datetime
import re


# Configuración del logging
def setup_logging():
    """Configura el sistema de logging con formato timestamp y nivel de detalle."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    logging.basicConfig(
        filename=f'csv_merger_{timestamp}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


# Mapeo de columnas según especificaciones
COLUMN_MAPPING = {
    'Fecha': 'Date',
    'Date': 'Date',
    'Último': 'Close',
    'Ultimo': 'Close',
    'Price': 'Close',
    'Cierre': 'Close',
    'Apertura': 'Open',
    'Open': 'Open',
    'Máximo': 'High',
    'High': 'High',
    'Mínimo': 'Low',
    'Low': 'Low',
    'Vol.': 'Volume',
    '% var.': 'Change%',
    'Change %': 'Change%'
}


def find_csv_files(directory, pattern):
    """
    Encuentra archivos CSV que coincidan con el patrón especificado.
    
    Args:
        directory (str): Ruta del directorio a buscar
        pattern (str): Patrón base para buscar archivos
    
    Returns:
        list: Lista de rutas de archivos CSV encontrados
    """
    csv_files = []
    pattern_regex = re.compile(f"{re.escape(pattern)}(?:\s*\(\d+\))?.csv$")
    
    for file in os.listdir(directory):
        if pattern_regex.match(file):
            csv_files.append(os.path.join(directory, file))
            logging.info(f"Archivo encontrado: {file}")
    
    return csv_files


def read_and_standardize_csv(file_path):
    """
    Lee y estandariza un archivo CSV según el mapeo de columnas definido.
    
    Args:
        file_path (str): Ruta del archivo CSV a procesar
    
    Returns:
        pandas.DataFrame: DataFrame con columnas estandarizadas
    """
    try:
        # Leer CSV con manejo de fechas
        df = pd.read_csv(file_path, parse_dates=['Date'])
        
        # Registrar columnas originales para debugging
        original_columns = df.columns.tolist()
        logging.info(f"Columnas originales en {os.path.basename(file_path)}: {original_columns}")
        
        # Renombrar columnas según el mapeo
        renamed_columns = {}
        for col in df.columns:
            if col in COLUMN_MAPPING:
                renamed_columns[col] = COLUMN_MAPPING[col]
        
        df = df.rename(columns=renamed_columns)
        
        # Verificar columnas requeridas
        required_columns = {'Date', 'Close'}
        missing_columns = required_columns - set(df.columns)
        
        if missing_columns:
            logging.warning(f"Columnas faltantes en {os.path.basename(file_path)}: {missing_columns}")
            raise ValueError(f"Faltan columnas requeridas: {missing_columns}")
        
        return df
    
    except Exception as e:
        logging.error(f"Error procesando {os.path.basename(file_path)}: {str(e)}")
        raise


def merge_csv_files(directory, pattern):
    """
    Función principal para combinar archivos CSV.
    
    Args:
        directory (str): Directorio donde se encuentran los archivos
        pattern (str): Patrón base para identificar los archivos
    """
    setup_logging()
    logging.info(f"Iniciando proceso de combinación de archivos CSV en {directory}")
    
    try:
        # Encontrar archivos CSV
        csv_files = find_csv_files(directory, pattern)
        if not csv_files:
            raise FileNotFoundError(f"No se encontraron archivos CSV con el patrón '{pattern}'")
        
        # Lista para almacenar los DataFrames procesados
        dfs = []
        
        # Procesar cada archivo
        for file_path in csv_files:
            try:
                df = read_and_standardize_csv(file_path)
                dfs.append(df)
                logging.info(f"Archivo procesado exitosamente: {os.path.basename(file_path)}")
            except Exception as e:
                logging.error(f"Error en archivo {os.path.basename(file_path)}: {str(e)}")
                continue
        
        if not dfs:
            raise ValueError("No se pudo procesar ningún archivo correctamente")
        
        # Combinar todos los DataFrames
        combined_df = pd.concat(dfs, ignore_index=True)
        
        # Eliminar duplicados basados en la fecha
        combined_df = combined_df.drop_duplicates(subset=['Date'], keep='first')
        
        # Ordenar por fecha
        combined_df = combined_df.sort_values('Date', ascending=False)
 
        # Generar nombre del archivo de salida
        output_filename = f"{pattern}_TOTAL.csv"
        output_path = os.path.join(directory, output_filename)
    
        # Guardar resultado
        combined_df.to_csv(output_path, index=False)
        logging.info(f"Archivo combinado guardado exitosamente: {output_filename}")
    
        # Registrar estadísticas finales
        logging.info(f"Estadísticas finales:")
        logging.info(f"- Archivos procesados: {len(csv_files)}")
        logging.info(f"- Total de registros: {len(combined_df)}")
        logging.info(f"- Columnas en archivo final: {combined_df.columns.tolist()}")
       
    except Exception as e:
        logging.error(f"Error en el proceso de combinación: {str(e)}")
        raise


if __name__ == "__main__":
    # Ejemplo de uso
    directory = r"c:\Users\Nabucodonosor\Downloads"
    pattern = "USD_THB Historical Data"
    
    try:
        merge_csv_files(directory, pattern)
        print("Proceso completado exitosamente. Revisa el archivo de log para más detalles.")
    except Exception as e:
        print(f"Error en el proceso: {str(e)}")
        print("Revisa el archivo de log para más detalles.")