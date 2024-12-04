# Tarea 4 - HW_4

Repositorio para atención de la tarea *HW4* del curso de *COMPUTACIÓN CUÁNTICA Y CRIPTOGRAFÍA - 202420_MSIN4213_1* de la Universidad de los Andes.

**Por:** Hector Julian Mejia Arango

## Para ejecutar / verificar la tarea

### 1. Descargar repositorio

Todos los archivos deben estar **en una misma carpeta**.

### 2. Crear un *entorno virtual* de Python

Puede usar el *módulo de Python* [`venv` (*virtualenv*)][def].
Se recomienda desplegar la *carpeta* del *entorno virtual* dentro de la generada en el *Punto 2* para los archivos.

### 3. Activar el *entorno virtual (Python 3.4+)*

Suponiendo que el nombre dado a la carpeta del *entorno virtual* fue *"venv"*:

- En *Windows*
  - En cmd: `venv\Scripts\activate.bat`
  - En PowerShell: `venv\Scripts\Activate.ps1`
- En *Linux / MacOS*: `source venv/bin/activate`

### 4. Instale los *paquetes Python* requeridos

Use el comando `pip` y el *archivo* `requirements.txt`:
`pip install -r requirements.txt`

**NOTA:** Este código hace uso de la versión de *QisKit* `0.46.2`.

### 5. Ejecución / verificación

Con el *entorno virtual* **habilitado** y tras la *instalación* de las librerías necesarias, sobre la *terminal* tenida, ejecute: `python qc4_test.py`

Esto imprimirá el resultado de cada uno de los *test* generados para verificar la *correcta codificación* de las *funciones* solicitadas en el archivo `qc4.py`

[def]: https://python.land/virtual-environments/virtualenv
