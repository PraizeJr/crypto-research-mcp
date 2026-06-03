from src.tools import (
    get_top_protocols_by_tvl,
    get_protocol_info,
    get_top_chains
)

def test_get_top_protocols_by_tvl():
    result = get_top_protocols_by_tvl(limit=5)

    assert result is not None
    assert isinstance(result, list)
    assert len(result) > 0
    assert "tvl" in result[0]


def test_get_protocol_info():
    result = get_protocol_info("aave")

    assert result is not None
    assert isinstance(result, dict)
    assert "name" in result or "symbol" in result


def test_get_top_chains():
    result = get_top_chains(limit=5)

    assert result is not None
    assert isinstance(result, list)
    assert len(result) > 0
