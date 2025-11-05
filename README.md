
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

qa-project-Urban-Routes-es/
│
├── fixtures/                             # Configuraciones y utilidades compartidas
│   ├── __init__.py                       # Permite tratar la carpeta como un paquete de Python
│   └── driver.py                         # Configura e inicializa el WebDriver para las pruebas
│
├── pages/                                # Implementación del patrón Page Object Model (POM)
│   ├── __init__.py                       # Marca el paquete de páginas
│   └── urban_routes_page.py              # Contiene los localizadores y métodos de interacción con la web
│
├── tests/                                # Carpeta de pruebas automatizadas con Pytest
│   ├── __init__.py                       # Define el paquete de pruebas
│   └── test_urban_routes.py              # Pruebas principales del flujo completo de Urban Routes
│
├── utils/                                # Funciones auxiliares o soporte adicional
│   ├── __init__.py                       # Permite importar módulos desde utils
│   └── phone_intercept.py                # Simula o intercepta el código SMS para validación
│
├── .gitignore.py                         # Archivos y carpetas que no se suben al repositorio
├── configuration.py                      # Configuración general: URLs, credenciales y parámetros globales
├── data.py                               # Datos de prueba (direcciones, teléfonos, tarifas, etc.)
├── main.py                               # Punto de entrada para ejecutar o integrar el flujo completo de pruebas
└── README.md                             # Documentación del proyecto

## Instalación de librerías
1. Asegúrate de tener **Python 3.14** instalado en tu máquina.  
2. Clona el repositorio:
```bash
git clone https://github.com/rogarf99-oss/qa-project-Urban-Routes-es.git

## Consejos
- El navegador permanecerá **abierto** después de la ejecución de las pruebas para que puedas revisarlo manualmente.
- Cada prueba contiene al menos un `assert` para verificar que la acción realizada funcionó correctamente.
- PyTest detecta automáticamente el orden de las pruebas según el nombre de las funciones `test_`.

## Autor y Sprint
- **Nombre del autor:** Roberto Garfias
- **Sprint del proyecto:** Sprint 9 - Grupo39 - QA / Automatización de pruebas


**Estado del Proyecto

El proyecto Urban Routes QA Automation se encuentra completamente actualizado y funcional.
Se implementaron 9 pruebas automatizadas utilizando Pytest y Selenium WebDriver, siguiendo las buenas prácticas de automatización y la estructura modular recomendada.

Cobertura de pruebas:

test_set_route → Verifica el establecimiento correcto de la ruta.

test_select_comfort → Comprueba la selección de la tarifa Comfort.

test_enter_phone_number → Valida el ingreso y solicitud del número telefónico.

test_enter_and_confirm_sms_code → Confirma la correcta validación del código SMS.

test_add_payment_method → Verifica la adición de un método de pago (tarjeta).

test_write_message → Comprueba que se puede escribir un mensaje para el conductor.

test_blanket → Valida la solicitud de una frazada.

test_add_icecream → Verifica que se puedan añadir helados.

test_find_driver → Asegura que el sistema pueda buscar correctamente un conductor.

Cada prueba incluye al menos un assert y se ejecuta de manera ordenada con una sola instancia de WebDriver, optimizando el flujo completo de la aplicación.





