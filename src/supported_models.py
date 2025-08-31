from enum import StrEnum


class SupportedModels(StrEnum):
    """Enum class for supported models within AI Class"""

    GPT4_O = ("gpt-4o",)
    GPT4_MINI = ("gpt-4o-mini",)
    GPT4_TURBO = ("gpt-4-turbo",)
    GPT4 = ("gpt-4",)
    GPT3_TURBO = ("gpt-3.5-turbo",)
