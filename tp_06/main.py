import logging
import argparse
from libs.logging_config import setup_logging
from pipelines.ingesta_txt import ingesta_txt, parse_txt, parse_noticias
from libs.output_file import output_file


def main():
    """
    Programa principal del pipeline.

    Utiliza argparse para leer el nombre del archivo a procesar desde la linea de comandos.
    Configura el logging para escribir en un archivo.
    Lee el archivo de texto y lo parsea en una lista de noticias.
    Parsea la lista de noticias en una lista de noticias parseadas.
    Guarda la lista de noticias parseadas en un archivo.
    Escribir en el archivo de log el inicio y fin del programa.
    """
    setup_logging()
    logging.info(f"Inicio del programa")
    parser = argparse.ArgumentParser()
    parser.add_argument("--archivo", type=str, required=True, help="Ruta del archivo a procesar")
    args = parser.parse_args()
    file_path_name=args.archivo
    type_file=file_path_name.split(".")[-1]
    match type_file:
        case "txt":
            contenido = ingesta_txt(file_path_name)
            noticias = parse_txt(contenido)
            noticias_parseadas = parse_noticias(noticias)
            output_file(noticias_parseadas, "pipeline", "lista")
            
        case "json":
            raise ValueError(f"en poceso: {type_file}")            
        case "csv":
            raise ValueError(f"en poceso: {type_file}")
            
        case _:
            raise ValueError(f"Extensión no soportada: {type_file}")
    
    logging.info(f"Fin del programa")

if __name__ == "__main__":
    main()