from enum import StrEnum


class SelectboxEnum(StrEnum):
    """An enum representing options in a streamlit selectbox"""

    @classmethod
    def options(cls) -> list[str]:
        return list(map(lambda member: member.value, cls))
