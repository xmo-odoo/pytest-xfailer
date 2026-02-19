import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    confpath = config.rootpath / "xfail.conf"
    try:
        with confpath.open("r") as cf:
            xfailed = {
                stripped
                for line in cf
                if (stripped := line.strip())
                if not stripped.startswith(('#', ';'))
            }
    except FileNotFoundError:
        return

    if not xfailed:
        return

    mark_xfail = pytest.mark.xfail()
    for item in items:
        if item.nodeid in xfailed:
            item.add_marker(mark_xfail)
