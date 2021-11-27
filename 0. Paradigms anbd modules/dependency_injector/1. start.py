from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    api_client = providers.Singleton(
        ApiClient,
        api_key=config.api_key,
        timeout=config.timeout.as_int(),
    )

    service = providers.Factory(
        Service,
        api_client=api_client,
    )


@inject
def main(service: Service = Provide[Container.service]):
    ...


if __name__ == '__main__':
    container = Container()
    container.config.api_key.from_env('API_KEY')
    container.config.timeout.from_env('TIMEOUT')
    container.wire(modules=[sys.modules[__name__]])

    main()  # <-- dependency is injected automatically

    with container.api_client.override(mock.Mock()):
        main()  # <-- overridden dependency is injected automatically