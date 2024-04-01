from enum import StrEnum


class SelectboxEnum(StrEnum):
    @classmethod
    def options(cls) -> list[str]:
        return list(map(lambda member: member.value, cls))
