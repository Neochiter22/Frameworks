from storage import load_json, save_json


def test_save_and_load_json(tmp_path):
    filename = tmp_path / "data.json"
    data = [{"id": 1, "name": "test"}]
    save_json(str(filename), data)
    assert load_json(str(filename), []) == data


def test_missing_json_returns_default(tmp_path):
    filename = tmp_path / "missing.json"
    assert load_json(str(filename), []) == []
