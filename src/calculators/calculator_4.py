from flask import request as FlaskRequest
from typing import Dict


class Calculator4:

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        
    
        soma = sum(input_data)  # Calcula a soma de todos os números da lista
        
        media = soma / len(input_data)  # Calcula a média

        response = self.__format_response(media)  # Formata a resposta com o resultado

        return response
    
    def __validate_body(self, body: Dict) -> list:
        if "numbers" not in body:
            raise Exception("body mal formatado!")
        
        input_data = body["numbers"]
        # Garante que todos os valores sejam numéricos
        return [float(x) for x in input_data]
    
    def __format_response(self, media: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "result": media,
            }
        }