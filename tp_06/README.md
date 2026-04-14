# TP 06 - Pipeline de ingesta de noticias

Pipeline que lee un archivo de texto con noticias, las parsea y guarda el resultado en `output/`.

## Estructura

```
tp_06/
├── main.py               # Punto de entrada
├── pipelines/
│   └── ingesta_txt.py    # Lectura y parseo de archivos .txt
├── libs/
│   ├── logging_config.py # Configuración de logs
│   └── output_file.py    # Escritura del archivo de salida
├── data/                 # Archivos de entrada
├── output/               # Archivos generados
└── logs/                 # Archivos de log
```

## Uso

```bash
python main.py --archivo data/noticias_crudas.txt
```

El argumento `--archivo` es obligatorio e indica la ruta del archivo a procesar.

## Formato de entrada

Cada línea del `.txt` debe tener el siguiente formato separado por `|`:

```
Titulo: <titulo> | Link: <url> | Fecha: <fecha> | Categoria: <categoria>
```

## Formato de salida

Se genera un archivo `.txt` en `output/` con el nombre `pipeline_<timestamp>.txt`.
Cada noticia se escribe con sus campos clave-valor separados por una línea de guiones.

## Extensiones soportadas

| Extensión | Estado      |
|-----------|-------------|
| `.txt`    | Implementado |
| `.csv`    | En proceso  |
| `.json`   | En proceso  |
