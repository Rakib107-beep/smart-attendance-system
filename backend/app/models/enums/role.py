from enum import Enum


class Role(str, Enum):
    ADMIN = "ADMIN"
    TEACHER = "TEACHER"
    USER = "USER"