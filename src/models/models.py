from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Set
from uuid import UUID, uuid4


class PackageStatus(Enum):
    CREATED = "CREATED"
    ACCEPTED = "ACCEPTED"
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"


class LocationType(Enum):
    WAREHOUSE = "WAREHOUSE"
    SORTING_CENTER = "SORTING_CENTER"
    TRANSPORT = "TRANSPORT"
    PICKUP_POINT = "PICKUP_POINT"
    OTHER = "OTHER"


class UserRole(Enum): # типы пользователей
    CLIENT = "CLIENT"
    EMPLOYEE = "EMPLOYEE"
    ADMINISTRATOR = "ADMINISTRATOR"


@dataclass
class Address:
    postal_code: str = ""
    country: str = ""
    city: str = ""
    street: str = ""
    house: str = ""
    apartment: str = ""


@dataclass
class Location:
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    type: LocationType = LocationType.WAREHOUSE
    address: Address = field(default_factory=Address)


@dataclass
class HistoryRecord:
    id: UUID = field(default_factory=uuid4)
    updated_at: datetime = field(default_factory=datetime.now)
    status: PackageStatus = PackageStatus.CREATED
    location: str = ""


@dataclass
class Package:
    id: UUID = field(default_factory=uuid4)
    tracking_number: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    sender: str = ""
    recipient: str = ""
    status: PackageStatus = PackageStatus.CREATED
    delivery_address: Address = field(default_factory=Address)


# пользователи для сервиса пользователей

class User(ABC):
    def __init__(
        self,
        id: UUID,
        login: str,
        password: str,
        name: str,
        email: str,
        is_active: bool = True,
        role: UserRole = UserRole.CLIENT,
    ):
        self.id: UUID = id
        self.login: str = login
        self.password: str = password
        self.name: str = name
        self.email: str = email
        self.is_active: bool = is_active
        self.role: UserRole = role

    def authenticate(self, login: str, password: str) -> bool:
        pass

    def logout(self) -> None:
        pass

    @abstractmethod
    def get_permissions(self) -> Set[str]:
        pass


class Client(User):
    def get_permissions(self) -> Set[str]:
        return set()


class Employee(User):
    def get_permissions(self) -> Set[str]:
        return set()


class Administrator(User):
    def get_permissions(self) -> Set[str]:
        return set()