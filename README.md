
# Urban Routes QA Automation

## Descripción del proyecto
Este proyecto automatiza el flujo completo de solicitud de un servicio de taxi en la plataforma Urban Routes. Las pruebas cubren la selección de dirección de origen y destino, la selección de la tarifa Comfort, el ingreso de teléfono y verificación mediante código SMS, así como la adición de métodos de pago, comentarios, selección de servicios adicionales y confirmación del recorrido.

El objetivo es garantizar que el flujo principal de la aplicación funcione correctamente y detectar cualquier fallo en el proceso de reserva de un taxi.

## Tecnologías y técnicas utilizadas
- **Python 3.14**: Lenguaje principal del proyecto.
- **Selenium 4**: Para automatización de la interfaz web.
- **pytest**: Framework de pruebas utilizado para organizar y ejecutar los test cases.
- **WebDriverWait y Expected Conditions**: Para manejar la sincronización y esperar elementos dinámicos en la página.
- **ActionChains**: Para simular acciones complejas de usuario.
- **JavaScript injection**: Para forzar clics en elementos que a veces no son detectados correctamente por Selenium.
- **Interceptación de SMS**: Uso de un script utilitario para recuperar códigos enviados al número de teléfono de prueba.
- **Estructura modular**: Carpeta `pages` para Page Objects, `tests` para los casos de prueba, y `fixtures` para configuraciones compartidas.

## Estructura del proyecto
qa-project-Urban-Routes-es/
│
├─ pages/
│ └─ urban_routes_page.py # Clases y métodos de Page Object
│
├─ tests/
│ └─ test_urban_routes.py # Casos de prueba automatizados
│
├─ fixtures/
│ └─ driver.py # Configuración de WebDriver
│
├─ utils/
│ └─ phone_intercept.py # Función para recuperar código SMS
│
├─ configuration.py # Variables de configuración (URL base, etc.)
├─ data.py # Datos de prueba (direcciones, teléfono, tarjeta)
├─ requirements.txt # Dependencias del proyecto
└─ README.md # Este archivo

## Instalación de librerías
1. Asegúrate de tener **Python 3.14** instalado en tu máquina.  
2. Clona el repositorio:
```bash

## Consejos
- El navegador permanecerá **abierto** después de la ejecución de las pruebas para que puedas revisarlo manualmente.
- Cada prueba contiene al menos un `assert` para verificar que la acción realizada funcionó correctamente.
- PyTest detecta automáticamente el orden de las pruebas según el nombre de las funciones `test_`.

## Autor y Sprint
- **Nombre del autor:** Roberto Garfias
- **Sprint del proyecto:** Sprint 9 - Grupo39 - QA / Automatización de pruebas





