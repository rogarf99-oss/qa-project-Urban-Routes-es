# utils/phone_intercept.py
import json
import time
from selenium.common import WebDriverException

def retrieve_phone_code(driver) -> str:
    """
    Recupera el código de confirmación desde los logs de performance de Chrome.
    Úsalo *después* de haber solicitado el código en la aplicación.
    """
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log("performance") if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
                if code:
                    return code
        except WebDriverException:

            time.sleep(1)
            continue

        time.sleep(1)

    raise Exception(
        "No se encontró el código de confirmación del teléfono.\n"
        "Utiliza 'retrieve_phone_code(driver)' solo después de haber solicitado el código en tu aplicación."
    )
