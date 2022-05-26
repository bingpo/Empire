import sys
from unittest.mock import MagicMock, Mock

from empire.test.conftest import SERVER_CONFIG_LOC


def test_bypass_loader(monkeypatch):
    sys.argv = ["", "server", "--config", SERVER_CONFIG_LOC]
    session_mock = MagicMock()
    monkeypatch.setattr(
        "empire.server.v2.core.bypass_service.SessionLocal", session_mock
    )

    session_mock.begin.return_value.__enter__.return_value.query.return_value.first.return_value.install_path = (
        "empire/server"
    )

    session_mock.begin.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = (
        None
    )

    from empire.server.v2.core.bypass_service import BypassService

    main_menu = Mock()
    main_menu.installPath = "empire/server"

    bypass_service = BypassService(main_menu)

    assert session_mock.begin.return_value.__enter__.return_value.add.call_count > 4


def test_listener_template_loader(monkeypatch):
    sys.argv = ["", "server", "--config", SERVER_CONFIG_LOC]
    session_mock = MagicMock()
    monkeypatch.setattr(
        "empire.server.v2.core.listener_template_service.SessionLocal", session_mock
    )

    session_mock.begin.return_value.__enter__.return_value.query.return_value.first.return_value.install_path = (
        "empire/server"
    )

    from empire.server.v2.core.listener_template_service import ListenerTemplateService

    main_menu = Mock()
    main_menu.installPath = "empire/server"

    listener_template_service = ListenerTemplateService(main_menu)

    assert len(listener_template_service.get_listener_templates()) > 7


def test_stager_template_loader(monkeypatch):
    sys.argv = ["", "server", "--config", SERVER_CONFIG_LOC]
    session_mock = MagicMock()
    monkeypatch.setattr(
        "empire.server.v2.core.stager_template_service.SessionLocal", session_mock
    )

    session_mock.begin.return_value.__enter__.return_value.query.return_value.first.return_value.install_path = (
        "empire/server"
    )

    from empire.server.v2.core.stager_template_service import StagerTemplateService

    main_menu = Mock()
    main_menu.installPath = "empire/server"

    stager_template_service = StagerTemplateService(main_menu)

    assert len(stager_template_service.get_stager_templates()) > 10


def test_profile_loader(monkeypatch):
    sys.argv = ["", "server", "--config", SERVER_CONFIG_LOC]
    session_mock = MagicMock()
    monkeypatch.setattr(
        "empire.server.v2.core.profile_service.SessionLocal", session_mock
    )

    session_mock.begin.return_value.__enter__.return_value.query.return_value.first.return_value.install_path = (
        "empire/server"
    )

    session_mock.begin.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = (
        None
    )

    from empire.server.v2.core.profile_service import ProfileService

    main_menu = Mock()
    main_menu.installPath = "empire/server"

    profile_service = ProfileService(main_menu)

    assert session_mock.begin.return_value.__enter__.return_value.add.call_count > 20
