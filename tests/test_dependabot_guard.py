import httpx


def test_httpx_pinned_for_d04():
    # Temporary (test D-04): fails when Dependabot bumps httpx, so the PR Gate goes red.
    assert httpx.__version__ == "0.28.0"
