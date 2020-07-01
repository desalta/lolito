# Lolito

![](https://i.ibb.co/6sny9gm/lolito.png)

Lolito es un programa gratuito que tiene el fin de proveer herramientas adicionales para jugar a League of Legend.
Cuenta con las siguientes aplicaciones:

* Runero
* Batallas (proximamente)

## Runero
Esta caracteristica tiene dos funcionalidades principales

  - Proveer una herramienta para almacenar paginas de runas infinitas
  - Proveer un mecanismo para que se puedan aplicar las runas automaticamente en el juego

Acciones:
  - **Aplicar**: una vez selecionada una página de runa, saldrá una ventana emergente. Al clickear en "OK", nos dará 2 segundos para posicionar el mouse sobre el ícono de seleccion de runas. Pasado este tiempo, comenzará a seleccionar las runas configuradas en el juego.
  - **Borrar**: una vez seleccionada una página de runa, borrar elminará la página de la base de datos.
  - **Guardar**: si el nombre de la pagina de runa ya existe, actualizará la página. Si la página no existe, creará una nueva

Consideraciones:
  - El programa no valida que tener dos rutas de runas iguales. Por ejemplo, el programa permite tener Precisión en la primera y segunda ruta de runa, sin embargo esto provocará que al aplicar la pagina de ruta, no se seleccionará correctamente

### Instalación

El programa esta desarrollado en python y algunas librerías adicionales.

**Python**
 - En la carpeta del programa se encuentra el archivo ***instalador-python.exe***, que hay que instalar. 
 `Importante! A la hora de instalar hay que tildar la opción que dice "Include in PATH"`
 - En caso de tener python instalado esta opción no es necesaria. Y también se puede descargar e instalar python desde su página oficial.

**Dependencias**
- Para instalar las dependencias restantes, hay que ejecutar el archivo ***install.bat*** que se encuentra en la carpeta del programa.

### Ejecución

Para ejecutar el programa hay ejecutar el archivo ***exe.bat***.
Además existe un acceso directo llamado ***Lolito***, el cual se puede copiar al escritorio para tenerlo cerca.

