from typing import Any, List, Optional

from ..models.models import (
    HistoryRecord,
    Location,
    Package,
    PackageStatus,
    User,
    UserRole,
)


class SearchService:
    def __init__(self):
        self.available_packages: List[Package] = []

    def find_by_number(self, tracking_number: str) -> Optional[Package]:
        pass


class PackageService:
    def __init__(self):
        self.available_packages: List[Package] = []

    def register_package(self, data: Any) -> Optional[Package]:
        pass

    def update_package_data(self, tracking_number: str, data: Any) -> None:
        pass

    def delete_package(self, tracking_number: str) -> None:
        pass

    def get(self, tracking_number: str) -> Optional[Package]:
        pass


class TrackingService:
    def __init__(self):
        self.available_packages: List[Package] = []

    def update_state(
        self, package: Package, status: PackageStatus, location: Location
    ) -> None:
        pass

    def get_history(self, package: Package) -> List[HistoryRecord]:
        return []


class UserService:
    def __init__(self):
        self.managed_users: List[User] = []

    def create_user(self, data: Any, role: UserRole) -> Optional[User]:
        pass

    def update_user(self, user: User, data: Any) -> None:
        pass

    def block_user(self, user: User) -> None:
        pass

    def unblock_user(self, user: User) -> None:
        pass