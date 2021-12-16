import sqlite3

from dependency_injector import containers, providers


class UserService:
    def __init__(self, db: sqlite3.Connection):
        self.db = db


class AuthService:
    def __init__(self, db: sqlite3.Connection, user_service: UserService):
        self.db = db
        self.user_service = user_service


class Container(containers.DeclarativeContainer):

    # se crea una unica instancia de la base de datos
    database = providers.Singleton(sqlite3.connect, ":memory:")

    user_service = providers.Factory(
        UserService,
        db=database,
    )

    auth_service = providers.Factory(
        AuthService,
        db=database,
        user_service=user_service,
    )


if __name__ == "__main__":
    container = Container()

    user_service = container.user_service()
    auth_service = container.auth_service()

    assert user_service.db is auth_service.db is container.database()
    assert isinstance(auth_service.user_service, UserService)

    print(user_service.db)
    print(auth_service.db)
    print(container.database())
    print(auth_service.user_service)
    print(UserService)
