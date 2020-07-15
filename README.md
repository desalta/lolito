# Lolito

![Lolito](https://i.imgur.com/HO8rtFM.png)

Lolito es un programa portable y gratuito que tiene el fin de proveer herramientas adicionales para jugar a League of Legend.
Descargar el archivo comprimido desde el siguiente [Link](https://github.com/desalta/lolito/archive/master.zip)

Cuenta con las siguientes aplicaciones:

* Runero
* Wikilol
* Batallas (próximamente)

Para mas informacion, esta desarrollado en python y flask. Con algunas librerías adicionales.

## Runero
Esta función tiene dos funcionalidades principales

  - Proveer una herramienta para almacenar paginas de runas (infinitas)
  - Proveer un mecanismo para que se puedan aplicar las runas automáticamente en el juego

[![Watch the video](https://i.imgur.com/6jRJNK2.jpg)](https://vimeo.com/435069489)

Acciones:
  - **Aplicar**: una vez seleccionada una página de runa, saldrá una ventana emergente. Al clickear en "Aceptar", nos dará 2 segundos para posicionar el mouse sobre el ícono de selección de runas. Pasado este tiempo, comenzará a seleccionar las runas configuradas en el juego.
  - **Borrar**: una vez seleccionada una página de runa, borrar eliminará la página de la base de datos.
  - **Guardar**: si el nombre de la pagina de runa ya existe, actualizará la página. Si la página no existe, creará una nueva

Consideraciones:
  - El programa no valida que tener dos rutas de runas iguales. Por ejemplo, el programa permite tener Precisión en la primera y segunda ruta de runa, sin embargo esto provocará que al aplicar la pagina de ruta, no se seleccionará correctamente

### Instalación

Para realizar la instalación es muy simple. La carpeta del programa posee 3 archivos
 1. instalador-python.exe
 2. instalador-librerias.bat
 3. link-escritorio.bat


**Instalador Python**
 - El programa utiliza python 3.8, por lo cual debe estar instalado en la maquina, si ya lo tiene puede saltar este paso. Caso contrario, lo puede descargar desde la pagina oficial, o utilizar el instalador provisto llamado instalador-python.exe
 
    `Importante! A la hora de instalar hay que tildar la opción que dice "Add Python 3.8 to PATH"`
 [click para mostrar mas detalles](https://i.imgur.com/842AtYt.png)

**Instalador Librerías**
- Ademas de python se necesitan instalar algunas librerías, para ello simplemente ejecutar **instalador-liberias.bat**, que las descargara e instalara automáticamente.

**Link en el Escritorio**
- En este punto el programa ya se puede usar. Para genera un link de acceso directo en el escritorio ejecutar ***link-escritorio.bat***. Tener en cuenta si que se cambia la ubicación de la carpeta, tendrían que volver a generar un nuevo link.

### Ejecución

Simplemente, iniciar desde el link ***Lolito*** que aparece en el escritorio.

También se puede iniciar el programa desde el archivo ***lolitoapp/system/run.bat***.


