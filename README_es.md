# OCDS Kit Web
OCDS Kit Web es una aplicación web para la manipulación de archivos OCDS basada en el proyecto [OCDS Kit](https://github.com/open-contracting/ocdskit).
OCDS Kit Web provee al usuario las mismas funcionalidades de OCDS Kit a través de una interfaz web intuitiva y fácil de utilizar.

## Inicio
### Prerequisitos
1. Instalar [Python 3.6+](https://www.python.org/downloads).
2. [Clonar](https://help.github.com/en/articles/cloning-a-repository) el proyecto de Github.
3. Instalar [virtualenv](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv). **La instalación de esta herramienta es opcional, pero recomendada**.

### Instalación
1. Instalar las dependencias del proyecto:
```
pip install -r requirements.txt
```
2. Definir las siguientes variables de entorno:
* OCDS_TOUCAN_MEDIA_ROOT: ruta del directorio donde se guardan los archivos subidos. A libre elección.
* OCDS_TOUCAN_LOCALE_PATH: Debe apuntar al directorio locale/ dentro del proyecto.
* OCDS_TOUCAN_MAXNUMFILES: número máximo de archivos a subir por operación.
* OCDS_TOUCAN_MAXFILESIZE: tamaño máximo de archivos a subir en bytes.

### Levantar el proyecto
Levantar el servidor de desarrollo:
```
python manage.py runserver
```

## Funcionalidades
### Create Release Packages
Genera un [Release Package](http://standard.open-contracting.org/latest/en/getting_started/publication_patterns/#packaging-releases-and-records) a partir de varios archivos [Release](http://standard.open-contracting.org/latest/en/getting_started/releases_and_records/#releases).  
Utiliza el comando `package-releases`. [Más información](https://github.com/open-contracting/ocdskit#package-releases).
>Tipo de archivo válido: Release.

### Compile Releases
Genera un [Record Package](http://standard.open-contracting.org/latest/en/getting_started/publication_patterns/#packaging-releases-and-records) a partir de archivos Release Package.  
Utiliza el comando `compile`. **Observación**: este comando utiliza como parámetros `--package` y `--versioned`, visite la [documentación](https://github.com/open-contracting/ocdskit#compile) del comando para más información.
>Tipo de archivo válido: Release Package.

### Upgrade from 1.0 to 1.1
Actualiza packages y releases de la versión 1.0 de OCDS a la 1.1.  
Utiliza el comando `upgrade`. [Más información](https://github.com/open-contracting/ocdskit#upgrade).
>Tipo de archivo válido: cualquier tipo.

### Generate a spreadsheet version of schema
Genera un spreadsheet de cualquier versión de un OCDS schema.  
Utiliza el comando `mapping-sheet`. [Más información](https://github.com/open-contracting/ocdskit#mapping-sheet).
>Puede generar spreadsheets de Release, Release Package o Record Package.

### Convert to CSV/Excel
Convierte un archivo Release Package a una versión CSV/Excel.  
Utiliza la herramienta [flatten-tool](https://github.com/OpenDataServices/flatten-tool).
>Tipo de archivo válido: Release Package.

### Data Review Tool
Enlaza a la [Herramienta de Revisión de Datos](http://standard.open-contracting.org/review/).

### OCDS Extension Creator
Enlaza a la [Herramienta de Creación de Extensiones OCDS](https://open-contracting.github.io/extension_creator/).

## Arquitectura
### Descripción  de la arquitectura
Se utiliza Django Framework para construir los módulos Fron-end y Back-end para la aplicación.
El módulo Front-end contiene los elementos de presentación para interactuar con el usuario.
En el módulo Back-end se encuentran implementados el OCDS Kit y el flatten-tool como librerias que implementan las funcionalidades.
![alt text](img/architecture.png "Diagrama General")

### Diseño
Página principal de la aplicación:

![alt text](img/landing_page.png "Página de inicio")

Vista de funcionalidades, el diseño es el mismo en la mayoría de los casos:

![alt text](img/feature_view.png "Diseño para las funcionalidades")

### Restricciones
Las restricciones del sistema son las siguientes:

Restricción | Valor
--- | ---
Tamaño máximo de archivos | 10MB
Cantidad máxima de archivos por operación | 20
Timeout de sesión | 24 horas

## Ejemplos de uso
### 1. Crear un Release Package
1. Elegir un archivo con "Add a file" o arrastrar al cuadro. Utilizaremos archivos [Release 1.1](sample-data/1.1/releases).
![Alt text](img/ex1_1.png "Figura 1.1")
2. Añadir más archivos con el botón "Add more files" (2.1) o crear Release Package con "Start" (2.2).
![Alt text](img/ex1_2.png "Figura 1.2")
3. Una vez terminado, aparecerá un cuadro para poder descargar el Release Package generado.
![Alt text](img/ex1_3.png "Figura 1.3")

### 2. Merge Relase Packages
1. Elegir un archivo con "Add a file" o arrastrar al cuadro, igual al primer ejemplo. Utilizaremos los [Release Packages 1.1](sample-data/1.1/release-packages) de ejemplo.
2. Igual que en el ejemplo anterior, podemos agregar más archivos o iniciar la operación. También tenemos la opción de incluir versionado de Releases en nuestro Record Package a generar.
![Alt text](img/ex2_1.png "Figura 2.1")
3. Igual al anterior ejemplo, nos aparece un cuadro para descargar el Record Package generado.
![Alt text](img/ex2_2.png "Figura 2.2")

### 3. Actualizar un archivo 1.0 a 1.1
1. Elegir uno o más archivos Release/Record Package que sean versión 1.0. Para este ejemplo utilizamos [este](sample-data/1.0/release-packages/0001-tender.json) archivo de prueba.
2. Podemos añadir más archivos 1.0 o iniciar la conversión.
3. Una vez terminado, aparecerá un cuadro para poder descargar los archivos actualizados.
![Alt text](img/ex3.png "Figura 3")

### 4. Generar una versión spreadsheet de un OCDS schema
1. Elegir el tipo de schema y la versión a generar. En este ejemplo generaremos un Release Package Schema 1.1.
![Alt text](img/ex4.png "Figura 4")
2. Se generará un archivo con extensión .csv y se descargará automáticamente.

### 5. Convertir un Release Package a .csv
1. Elegir el archivo Release Package a convertir. Sólo se puede subir uno. Utilizaremos [este](sample-data/1.1/release-packages/0002-tender.json) archivo de prueba.
2. Se generarán dos archivos, un archivo .xlsx y un comprimido con archivos .csv, que contienen los datos del Release Package..
![Alt text](img/ex5.png "Figura 5")

## Herramientas utilizadas
* [Python 3.5+](https://www.python.org/) - Lenguaje de programación interpretado.
* [Django 2.1](https://www.djangoproject.com/) - Framework Web de Python.
* [JQuery 3.3](https://jquery.com/) - Biblioteca JavaScript.
* [Bootstrap 3](https://getbootstrap.com/) - Biblioteca Multiplataforma.

## Versiones
Se utiliza Git para el control de versiones.

## Licencias
Copyright (c) Open Contracting Partnership
