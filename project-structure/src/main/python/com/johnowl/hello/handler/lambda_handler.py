from src.main.python.com.johnowl.hello.service.validator_service import ValidatorService
import base64

service = ValidatorService()


def lambda_handler(event, context):
    request = event['Records'][0]['cf']['request']
    headers = request['headers']

    body = ""
    if request['method'] in ['POST', 'PUT', 'PATCH']:
        body = base64.b64decode(request['body']['data'])
    elif request['method'] not in ['GET', 'DELETE']:
        return error("invalid_http_method", "Os verbos HTTP aceitos são: GET, POST, PUT, PATCH e DELETE.")

    result = service.is_valid(headers, body)

    if result:
        return request
    else:
        return error(result.kind, result.message)


def error(kind: str, message: str):
    return {
        'status': '403',
        'statusDescription': 'Forbidden',
        'headers': {
            "content-type": [
                {
                    'key': 'Content-Type',
                    'value': 'text/html'
                }
            ],
            'content-encoding': [
                {
                    'key': 'Content-Encoding',
                    'value': 'UTF-8'
                }
            ]
        },
        'body': {
            'type': kind,
            'message': message
        }
    }
