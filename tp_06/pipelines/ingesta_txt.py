import logging
def ingesta_txt(file_path_name="noticias_crudas.txt"):
    """
    Lee un archivo de texto y devuelve su contenido.    
    
    Si el archivo esta vacio o solo contiene espacios en blanco, se muestra un mensaje de warning y se devuelve una cadena vacia.    
    
    Si ocurre un error al leer el archivo, se muestra un mensaje de error y se devuelve una cadena vacia.    
    
    Parameters
    ----------
    file_path_name : str
        nombre del archivo a leer. Por defecto es "noticias_crudas.txt".    
    
    Returns 
    -------
    str
        contenido del archivo. Si el archivo no existe o esta vacio, se devuelve una cadena vacia.
    """
    try: 
        with open(file_path_name, "r", encoding="utf-8") as file:
            # lee archvio, si el msimo esta vacio o solo con contneido blanco hace un logging 
            contenido = file.read()           
            if not contenido.strip():
                logging.warning(f"El archivo {file_path_name} está vacío.")                
                return ""            
        return contenido             
    
    except FileNotFoundError:
        
        logging.error(f"El archivo {file_path_name} no fue encontrado.")
        return""
    except UnicodeDecodeError:
        logging.error(f"El archivo {file_path_name} no tiene un formato válido.")
        return""
    except Exception as e:
        logging.error(f"Ocurrió un error al leer el archivo {file_path_name}: {e}")
        return""
            
def parse_txt(data):
    """
    Parsea el contenido de un archivo y devuelve una lista de noticias.    
    Si el contenido del archivo no puede ser parseado, se muestra un mensaje de error y se devuelve una lista vacia.    
    Parameters
    ----------
    data : str
        contenido del archivo a parsear.    
    Returns
    -------
    list
        lista de noticias. Si el contenido del archivo no puede ser parseado, se devuelve una lista vacia.
    """
    try:
        noticias = data.split("\n")        
        return noticias
    except Exception as e:
        logging.error(f"Ocurrió un error al parsear el archivo: {e}")
        return[]
    
def parse_noticias(data):
    """
    Parsea una lista de noticias y devuelve una lista de noticias parseadas.
    Cada noticia se parsea en un diccionario con las siguientes claves:
    - titulo: str, titulo de la noticia
    - link: str, enlace a la noticia
    - fecha: str, fecha en la que se publico la noticia
    - categoria: str, categoria a la que pertenece la noticia
    Si una noticia no puede ser parseada, se ignora.
    Parameters
    ----------
    data : list
        lista de noticias a parsear
    Returns
    -------
    list
        lista de noticias parseadas
    """
    noticias_parseadas = []
    for linea in data:
        linea = linea.strip()
        if not linea:
            continue
        noticia_parseada = linea.split("|")
        titulo=noticia_parseada[0].split(":")[1].strip()        
        link=noticia_parseada[1].replace("Link:","").strip()
        fecha=noticia_parseada[2].split(":")[1].strip()
        categoria=""
        if len(noticia_parseada)>3:
            categoria=noticia_parseada[3].split(":")[1].strip()
        noticias_parseadas.append({"titulo":titulo, "link": link,"fecha":fecha,"categoria":categoria})        
    return noticias_parseadas