import logging
from datetime import datetime
def setup_logging(file_prefix="log"):
 
    """
    Configura el logging para escribir en un archivo

    Args:
        file_prefix (str): Prefijo del nombre del archivo de log

    Returns:
        None

    Raises:
        Exception: Si ocurre un error al configurar el logging
    """
    try:
        log_date = datetime.now().strftime("%Y_%m_%d")
        file_name = f"{file_prefix}_{log_date}.log"
        log_path = f"logs/{file_name}"
        logging.basicConfig(
            filename=log_path,
            level=logging.INFO,
            format='%(asctime)s | %(levelname)s | %(message)s',
            encoding="utf-8"
        )
    except Exception as e:
        print(f"[ERROR] No se pudo configurar logging: {e}")