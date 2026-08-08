"""Infraestrutura de comunicação do PetPass AI com a API da OpenAI."""

import json
import os
from collections.abc import Mapping

from openai import OpenAI


OPENAI_API_KEY_ENV = "OPENAI_API_KEY"
OPENAI_MODEL_ENV = "OPENAI_MODEL"


class OpenAIConfigurationError(RuntimeError):
    """Indica que a configuração obrigatória da OpenAI está ausente."""


def validate_openai_configuration() -> tuple[str, str]:
    """Retorna chave e modelo ou informa que a configuração é inválida."""
    api_key = os.getenv(OPENAI_API_KEY_ENV, "").strip()
    if not api_key:
        raise OpenAIConfigurationError(
            "A IA não está configurada: "
            f"a variável de ambiente {OPENAI_API_KEY_ENV} está ausente."
        )

    model = os.getenv(OPENAI_MODEL_ENV, "").strip()
    if not model:
        raise OpenAIConfigurationError(
            "A IA não está configurada: "
            f"a variável de ambiente {OPENAI_MODEL_ENV} está ausente."
        )
    return api_key, model


class OpenAIService:
    """Responsável exclusivamente pela comunicação com a API da OpenAI."""

    def __init__(self) -> None:
        api_key, self._model = validate_openai_configuration()
        self._client = OpenAI(api_key=api_key)

    def generate_emergency_summary(
        self,
        data: Mapping[str, Mapping[str, str]],
    ) -> str:
        """Solicita um resumo fiel dos dados não vazios da ficha de emergência."""
        provided_data = {
            section: {
                field: value.strip()
                for field, value in fields.items()
                if value.strip()
            }
            for section, fields in data.items()
        }
        provided_data = {
            section: fields
            for section, fields in provided_data.items()
            if fields
        }

        response = self._client.responses.create(
            model=self._model,
            instructions=(
                "Produza um resumo claro e organizado da ficha de emergência. "
                "Use exclusivamente os dados fornecidos. Ignore campos ausentes. "
                "Não crie diagnósticos, tratamentos, prescrições, recomendações "
                "médicas ou informações não fornecidas."
            ),
            input=json.dumps(provided_data, ensure_ascii=False),
        )
        return response.output_text
