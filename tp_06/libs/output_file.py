from datetime import datetime
import json
import logging

def output_file(data, file_name="out", type_file="json"):   
    
    """
    Guarda una lista de noticias en un archivo.
    
    Parameters
    ----------
    data : list
        lista de noticias a guardar
    file_name : str, optional
        nombre del archivo a guardar, por defecto "out"
    type_file : str, optional
        tipo de archivo a guardar, puede ser "json", "txt" o "yaml", por defecto "json"
    
    Raises
    -------
    Exception
        Si ocurre un error al guardar el archivo
    """
    try:  
        logging.info(f"Guardadno en archivo")  
        now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        match type_file:
            case "json":
                type_file_use="json"
            case "txt":
                type_file_use="txt"
            case "lista":
                type_file_use="txt"
            case _:
                type_file_use="json"       
        file_name = f"output/{file_name}_{now}..{type_file_use}"
        match type_file:
            case "json":
                with open(file_name, "a", encoding="utf-8") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
            case "lista":
                with open(file_name, "a", encoding="utf-8") as file:
                    for item in data:
                        for clave, valor in item.items():
                            file.write(f"{clave}: {valor}\n")
                        file.write("-" * 40 + "\n")         
            # case "yaml":
            #     with open(file_name, "a", encoding="utf-8") as file:
            #         yaml.dump(data, file)
            #         # file.write(data.to_string(index=False))
            
            case "txt":
                with open(file_name, "a", encoding="utf-8") as file:
                    for item in data:
                        file.write(f"Titulo: {item['titulo']}, Link: {item['link']}, Fecha: {item['fecha']}, Categoria: {item['categoria']}\n")
            case _:
                with open(file_name, "a", encoding="utf-8") as file:
                    for item in data:
                        for clave, valor in item.items():
                            file.write(f"{clave}: {valor}\n")
                        file.write("-" * 40 + "\n")
                            
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")
        logging.error(f"Ocurrió un error al guardar el archivo: {e}")                        
    
        
    