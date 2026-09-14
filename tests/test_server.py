from connectsecure_mcp.server import ConnectSecureClient, OPERATIONS


def test_every_specification_operation_is_exposed():
    assert len(OPERATIONS) == 359
    assert len({operation.name for operation in OPERATIONS}) == 359


def test_client_uses_bearer_auth_and_escapes_path_values(monkeypatch):
    captured = {}

    class Response:
        status = 200
        def read(self): return b'{"status": true}'
        def __enter__(self): return self
        def __exit__(self, *args): return False

    def fake_urlopen(request, timeout):
        captured["url"] = request.full_url
        captured["authorization"] = request.get_header("Authorization")
        captured["user_id"] = request.get_header("X-user-id")
        return Response()

    monkeypatch.setattr("connectsecure_mcp.server.urlopen", fake_urlopen)
    response = ConnectSecureClient("https://example.test", "token", "user-1").request(
        OPERATIONS[3], {"id": "a/b"}, {"limit": 10}, {}, None
    )
    assert response == {"status": 200, "data": {"status": True}}
    assert captured == {"url": "https://example.test/r/company/companies/a%2Fb?limit=10", "authorization": "Bearer token", "user_id": "user-1"}
