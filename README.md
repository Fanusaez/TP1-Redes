# File Transfer Application

Este proyecto es el Trabajo Práctico N°1 de la materia **Introducción a los Sistemas Distribuidos (75.43)** en la Facultad de Ingeniería, Universidad de Buenos Aires. Su objetivo principal es la implementación de una aplicación cliente-servidor para la transferencia de archivos utilizando conceptos avanzados de comunicación en red.

## Integrantes

| Nombre                      | Legajo  |
|-----------------------------|---------|
| GALIÁN, Tomás Ezequiel      | 104354  |
| SAEZ, Edgardo Francisco     | 104896  |
| PUJATO, Iñaki               | 109131  |
| LARDIEZ, Mateo              | 107992  |
| ZACARIAS, Victor            | 107080  |

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Ejecucion Cliente](#ejecucion-cliente)
- [Ejecucion Servidor](#ejecucion-servidor)

---

## Descripción

El propósito de esta aplicación es implementar un protocolo de **Transferencia Confiable de Datos (RDT)** utilizando **UDP** como protocolo de transporte. Se desarrollaron dos versiones del protocolo:

1. **Stop & Wait**
2. **TCP con SACK (Selective ACKnowledgments)**

Además, la aplicación permite forzar condiciones de error para validar la confiabilidad en la transferencia.

## Características

- **Transferencia de archivos binarios** de hasta 5 MB.
- **Operaciones soportadas**:
  - `UPLOAD`: Envío de archivos del cliente al servidor.
  - `DOWNLOAD`: Descarga de archivos del servidor al cliente.
- Garantiza la entrega de paquetes con una pérdida de hasta **10%** en los enlaces.
- Manejo concurrente de múltiples clientes.
- Desarrollo en **Python** siguiendo las especificaciones de PEP8.

## Requisitos

1. **Python 3.x** instalado.
2. Librería estándar de sockets de Python.
3. Herramienta **Mininet** para simular condiciones de red.

### Instalación de Dependencias

```bash
pip install flake8
```

## Ejecucion Cliente

**NOTA: el flag -s no se encuentra implementado, usar por defecto el flag -n con alguno de los nombres de archivos contenidos dentro de del directorio archivos_de_prueba. Lo mismo aplica para el caso de especificar del destino de la descarga (operación download), no hay que especificar la ruta de descarga.**


### Upload
```bash
python upload [-h] [-v|-q] [-H ADDR ] [-p PORT] [-s FILEPATH] [-n FILENAME] [-a ALGORITHM]
```

Opciones:

| Opción         | Descripción                                  |
|----------------|----------------------------------------------|
| `-h`, `--help` | Muestra el mensaje de ayuda y sale.          |
| `-v`, `--verbose` | Incrementa la verbosidad de la salida.    |
| `-q`, `--quiet` | Disminuye la verbosidad de la salida.       |
| `-H`, `--host` | Dirección IP del servidor.                   |
| `-P`, `--port` | Puerto del servidor.                        |
| `-s`, `--src` | Ruta del archivo fuente que se desea subir.  |
| `-n`, `--name` | Nombre del archivo.                         |
| `-a`, `--algorithm` | Algoritmo elegido (sw or sack)         |



#### Ejemplo de uso
```bash
python3 upload.py -H 192.168.1.100 -p 8080 -s /ruta/al/archivo.txt -n archivo.txt -a sack
```

### Download
```bash
python download [-v|-q] [-H ADDR] [-p PORT] [-d FILEPATH ] [-n FILENAME ] [-a ALGORITHM]
```

Opciones:

| Opción            | Descripción                                      |
|-------------------|--------------------------------------------------|
| `-h`, `--help`    | Muestra el mensaje de ayuda y sale.              |
| `-v`, `--verbose` | Incrementa la verbosidad de la salida.           |
| `-q`, `--quiet`   | Disminuye la verbosidad de la salida.            |
| `-H`, `--host`    | Dirección IP del servidor.                       |
| `-p`, `--port`    | Puerto del servidor.                            |
| `-d`, `--dst`     | Ruta de destino del archivo descargado.          |
| `-n`, `--name`    | Nombre del archivo.                             |
| `-a`, `--algorithm` | Algoritmo elegido (sw or sack)               |


#### Ejemplo de uso
```bash
python3 download.py -H 192.168.1.100 -p 8080 -s /ruta/al/archivo.txt -n archivo.txt -a sack
```

--- 

## Ejecucion Servidor

```bash
python start-server [-h] [-v|-q] [-H ADDR] [-p PORT] [-s DIRPATH] [-a ALGORITHM]
```
Opciones:

| Opción              | Descripción                                   |
|---------------------|-----------------------------------------------|
| `-h`, `--help`      | Muestra el mensaje de ayuda y sale.           |
| `-v`, `--verbose`   | Incrementa la verbosidad de la salida.        |
| `-q`, `--quiet`     | Disminuye la verbosidad de la salida.         |
| `-H`, `--host`      | Dirección IP del servidor.                    |
| `-p`, `--port`      | Puerto del servidor.                          |
| `-s`, `--storage`   | Directorio donde se almacenarán los archivos. |
| `-a`, `--algorithm` | Algoritmo elegido (sw or sack).               |

#### Ejemplo de uso
```bash
python3 start_server.py -H 192.168.1.100 -p 8080 -s /ruta/de/stotage/ -a sack
```
