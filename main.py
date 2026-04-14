import logging
import argparse
from libs.logging_config import setup_logging
from pipelines.ingesta_txt import ingesta_txt, parse_txt, parse_noticias
from libs.output_file import output_file


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--archivo", type=str, required=True, help="Ruta del archivo a procesar")
    args = parser.parse_args()

    setup_logging()
    logging.info(f"Inicio del programa")
    contenido = ingesta_txt(file_path_name=args.archivo)
    noticias = parse_txt(contenido)
    noticias_parseadas = parse_noticias(noticias)
    output_file(noticias_parseadas, "pipeline", "lista")
    logging.info(f"Fin del programa")

if __name__ == "__main__":
    main()