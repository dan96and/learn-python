# learn-python

# Crear un proyecto en Reflex

Crear un entorno virtual: py -3 -m venv .venv
Activar el entorno virtual: .venv\\Scripts\\activate
Desactivar el entorno virtual: deactivate

Instalamos reflex en el directorio: pip install reflex
Iniciamos reflex: init reflex

Iniciar el proyecto: reflex run

Si aparece un warning que pone: Que no puede añadir las dependencias con Bun, y que lo va a hacer con npm.
Para solucionar este warning, tendremos que instalar Bun con npm con el siguiente comando: 
npm install -g bun
Una vez que lo instalamos tenemos que ir a la ruta donde tenemos el bun.exe instalado: C:\Users\xxxx\AppData\Roaming\npm\node_modules\bun\bun.exe
Copiaremos este archivo y lo pegaremos en:
C:\Users\dandr\AppData\Local\reflex\bun\bin

Si no conseguimos que el IDE (Visual Studio Code) reconozca los imports de Reflex:
- Abre la paleta de comandos (Ctrl+Shift+P)
- Escribe "Python: Select Interpreter" y selecciona la opción.
- Elige el intérprete que apunta a venv\Scripts\python.exe en Windows.