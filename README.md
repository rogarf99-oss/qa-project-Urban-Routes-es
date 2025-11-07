# Urban Routes QA Automation

## Descripción del proyecto
Este proyecto automatiza el flujo completo de solicitud de un servicio de taxi en la plataforma Urban Routes. Las pruebas cubren:

- Selección de dirección de origen y destino.
- Selección de la tarifa Comfort.
- Ingreso de teléfono y verificación mediante código SMS.
- Adición de métodos de pago.
- Envío de comentarios para el conductor.
- Selección de servicios adicionales como manta, pañuelos y helados.
- Confirmación del recorrido y espera del conductor en la pantalla de "Buscar automóvil".

El objetivo es garantizar que el flujo principal de la aplicación funcione correctamente y detectar cualquier fallo en el proceso de reserva de un taxi.

## Tecnologías y técnicas utilizadas
- **Python 3.14**: Lenguaje principal del proyecto.
- **Selenium 4**: Automatización de la interfaz web.
- **pytest**: Framework para organizar y ejecutar los casos de prueba.
- **WebDriverWait y Expected Conditions**: Para manejar elementos dinámicos y sincronización.
- **ActionChains**: Para simular acciones complejas de usuario.
- **JavaScript injection**: Para forzar clics en elementos que pueden no ser detectados correctamente por Selenium.
- **Interceptación de SMS**: Uso de un script utilitario (`phone_intercept.py`) para recuperar códigos enviados al número de prueba.
- **Manejo de overlays y elementos bloqueantes**: Se espera a que desaparezcan antes de interactuar con botones.
- **Estructura modular**: Carpeta `pages` para Page Objects, `tests` para los casos de prueba, `fixtures` para configuraciones compartidas y `utils` para utilidades.

## Estructura del proyecto
qa-project-Urban-Routes-es/
│
├── fixtures/                             # Configuraciones y utilidades compartidas
│   ├── __init__.py                       # Permite tratar la carpeta como un paquete de Python
│   └── driver.py                         # Configura e inicializa el WebDriver
│
├── pages/                                # Implementación del patrón Page Object Model (POM)
│   ├── __init__.py                       # Marca el paquete de páginas
│   └── urban_routes_page.py              # Localizadores y métodos de interacción
│       - Métodos incluidos:
│           - open()                      # Abrir la página
│           - set_route()                 # Selección de ruta y botón "Pedir taxi"
│           - select_comfort()            # Selección de tarifa Comfort
│           - enter_phone()               # Ingreso y confirmación del número de teléfono
│           - add_card()                  # Agregar tarjeta de crédito
│           - write_comment()             # Escribir un comentario para el conductor
│           - select_blanket()            # Selección de manta y pañuelos
│           - add_icecreams()             # Pedir helados
│           - wait_for_driver()           # Pedir taxi y esperar pantalla de "Buscar automóvil" + mantener 10s
│
├── tests/                                # Pruebas automatizadas con pytest
│   ├── __init__.py                       # Define el paquete de pruebas
│   └── test_urban_routes.py              # Pruebas del flujo completo
│       - test_01_set_route()              # Confirmar ruta
│       - test_02_select_comfort()         # Seleccionar Comfort
│       - test_03_enter_phone()            # Ingreso de teléfono
│       - test_04_add_card()               # Agregar tarjeta
│       - test_05_write_comment()          # Enviar comentario
│       - test_06_select_blanket()         # Pedir manta y pañuelos
│       - test_07_add_icecreams()          # Pedir helados
│       - test_08_wait_for_driver()        # Esperar pantalla de "Buscar automóvil"
│
├── utils/                                # Funciones auxiliares
│   ├── __init__.py
│   └── phone_intercept.py                # Intercepta el código SMS de confirmación
│
├── .gitignore.py                         # Archivos y carpetas que no se suben al repositorio
├── configuration.py                      # Configuración general y URL base
├── data.py                               # Datos de prueba (direcciones, teléfono, tarjeta, mensaje)
├── main.py                               # Punto de entrada para ejecutar las pruebas
└── README.md                             # Documentación del proyecto

## Instalación y ejecución
1. Asegúrate de tener **Python 3.14** instalado en tu máquina.  
2. Clona el repositorio:
```bash
git clone https://github.com/rogarf99-oss/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es

##Ejecuta todas las pruebas
pytest -v

Consejos
-El navegador permanece abierto durante toda la sesión para revisión manual.
-Cada prueba tiene al menos un assert para validar correctamente cada paso.
-Se manejan overlays y elementos bloqueantes para evitar errores de clic.
-La pantalla de "Buscar automóvil" se mantiene visible 10 segundos para inspección manual.
-Pytest detecta automáticamente el orden de ejecución según el nombre de las funciones test_.

Autor y Sprint
-Nombre del autor: Roberto Garfias
-Sprint del proyecto: Sprint 9 - Grupo39 - QA / Automatización de pruebas




