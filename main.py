# from app import ingesta_txt, logging_config, parse_txt, parse_noticias
import logging
from libs.logging_config import setup_logging
from pipelines.ingesta_txt import ingesta_txt,  parse_txt, parse_noticias
from libs.output_file import output_file


def main():  
    setup_logging()
    logging.info(f"Inicio del programa")
    contenido = ingesta_txt(file_path_name="data/noticias_crudas.txt")
    noticias = parse_txt(contenido)
    noticias_parseadas = parse_noticias(noticias)
    output_file(noticias_parseadas,"pipeline","lista")
    logging.info(f"Fin del programa")           
if __name__ == "__main__":
    main()

