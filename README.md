# grupo 8 modulo 6 django


## Introducción a DJANGO

Paso 1: Crear entorno virtual:
```bash
python3 -m venv nombre_entorno
```

Paso 2: Activar entorno 
**Windows** 

*(cmd)*
```bash
call nombre_entorno\Scripts\activate
```
*(git bash)*
```bash
source nombre_entorno/Scripts/activate 
```

**Mac**

*(bash o fish)*
```bash
source nombre_entorno/bin/activate.fish
```
*(zsh) *
```bash
source nombre_entorno/bin/activate
``` 

Paso 3: Instalar DJango en el entorno virtual creado 
*en windows usar **pip** y en mac usar **pip3*** 

```bash
pip3 install django
```

Paso 4: Crear el proyecto
```bash
django-admin startproject nombre_proyecto
```
Paso 5: Acceder al proyecto:
```bash
cd nombre_proyecto
```

Paso 6: Agregar app al proyecto
```bash
python3 manage.py startapp nombre_proyecto
```

Paso 7: Vincular app al proyecto con el nombre de la app 
    INSTALLED_APPS=[
    'nombre_app',
    … ]
