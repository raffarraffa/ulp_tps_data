import logging
import argparse
from libs.logging_config import setup_logging
from pipelines.ingesta_txt import ingesta_txt, parse_txt, parse_noticias
from libs.output_file import output_file


def main():

    """
    Punto de entrada del programa.
    
    Se encarga de leer los argumentos de la linea de comandos y ejecutar la pipeline de proceso de un archivo de texto.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    
    setup_logging()
    logging.info(f"Inicio del programa")
    parser = argparse.ArgumentParser()
    parser.add_argument("--archivo", type=str, required=True, help="Ruta del archivo a procesar")
    parser.add_argument("--salida", type=str, required=False, default="json", help="Tipo salida")
    args = parser.parse_args()
    file_path_name = args.archivo
    file_salida = args.salida
    type_file=file_path_name.split(".")[-1]
    match type_file:
        case "txt":
            contenido = ingesta_txt(file_path_name)
            noticias = parse_txt(contenido)
            noticias_parseadas = parse_noticias(noticias)
            output_file(data=noticias_parseadas,file_name="pipeline",type_file=file_salida)
            
        case "json":
            raise ValueError(f"en poceso: {type_file}")            
        case "csv":
            raise ValueError(f"en poceso: {type_file}")
            
        case _:
            raise ValueError(f"Extensión no soportada: {type_file}")
    
    logging.info(f"Fin del programa")

if __name__ == "__main__":
    main()