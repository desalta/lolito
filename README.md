# Lolito

![Lolito](https://i.imgur.com/HO8rtFM.png)

Lolito es un programa portable y gratuito que tiene el fin de proveer herramientas adicionales para jugar a League of Legend.
Cuenta con las siguientes aplicaciones:

* Runero
* Infochamp (proximamente)
* Batallas (proximamente)

## Runero
Esta función tiene dos funcionalidades principales

  - Proveer una herramienta para almacenar paginas de runas (infinitas)
  - Proveer un mecanismo para que se puedan aplicar las runas automaticamente en el juego

Acciones:
  - **Aplicar**: una vez selecionada una página de runa, saldrá una ventana emergente. Al clickear en "OK", nos dará 2 segundos para posicionar el mouse sobre el ícono de seleccion de runas. Pasado este tiempo, comenzará a seleccionar las runas configuradas en el juego.
  - **Borrar**: una vez seleccionada una página de runa, borrar elminará la página de la base de datos.
  - **Guardar**: si el nombre de la pagina de runa ya existe, actualizará la página. Si la página no existe, creará una nueva

Consideraciones:
  - El programa no valida que tener dos rutas de runas iguales. Por ejemplo, el programa permite tener Precisión en la primera y segunda ruta de runa, sin embargo esto provocará que al aplicar la pagina de ruta, no se seleccionará correctamente

### Instalación

El programa esta desarrollado en python y requiere algunas librerías adicionales. A continuación la instalación de las mismas.

**Python**
 - En la carpeta del programa se encuentra el archivo ***instalador-python.exe***, que hay que instalar. 
 `Importante! A la hora de instalar hay que tildar la opción que dice "Add Python 3.8 to PATH"`
 - En caso de tener python instalado esta opción no es necesaria. Y también se puede descargar e instalar python desde su página oficial.
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](https://i.imgur.com/842AtYt.png)

**Dependencias**
- Para instalar las dependencias restantes, hay que ejecutar el archivo ***install.bat*** que se encuentra en la carpeta del programa.

**Link en el Escritorio**
- Para genera un link de acceso directo en el escritorio ejecutar ***link.bat***. Tener en cuenta si que se cambia la ubicación de la carpeta, tendrían que volver a generar un nuevo link.

### Ejecución

Simplemente, iniciar desde el link ***Lolito*** que aparece en el escritorio.
También se puede iniciar el programa desde el archivo ***run.bat***.

