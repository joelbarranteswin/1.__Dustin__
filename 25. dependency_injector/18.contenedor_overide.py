import sqlite3
from unittest import mock

from dependency_injector import containers, providers


class Foo:
    ...


class Bar:
    ...


class Container(containers.DeclarativeContainer):

    database = providers.Singleton(sqlite3.connect, ":memory:")


if __name__ == "__main__":
    container = Container()

    container.database.override_providers(
        foo=mock.Mock(Foo), bar=mock.Mock(Bar))

    assert isinstance(container.foo(), mock.Mock)
    assert isinstance(container.bar(), mock.Mock)

    print(container.foo())
    print(isinstance(container.foo(), mock.Mock))
