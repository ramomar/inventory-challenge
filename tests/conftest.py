import pytest
import redacted.memory as mem


@pytest.fixture(scope="function", autouse=True)
def reset_memory():
    mem._reset()
