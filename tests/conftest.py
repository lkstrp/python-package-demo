import pytest
import os
import json
import tempfile
from unittest.mock import patch


@pytest.fixture
def mock_jokes():
    """Fixture providing test joke data"""
    return {
        "test": [
            "Test joke 1",
            "Test joke 2?With a punchline",
            "Test joke 3. With multiple sentences.",
        ],
        "programming": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
        ],
    }


@pytest.fixture
def mock_facts():
    """Fixture providing test facts data"""
    return ["Test fact 1", "Test fact 2"]


@pytest.fixture
def temp_favorites_file():
    """Create a temporary file for favorites"""
    temp_dir = tempfile.gettempdir()
    temp_file = os.path.join(temp_dir, "test_favorites.json")

    # Ensure the file doesn't exist at start
    if os.path.exists(temp_file):
        os.unlink(temp_file)

    yield temp_file

    # Cleanup after test
    if os.path.exists(temp_file):
        os.unlink(temp_file)


@pytest.fixture
def favorites_path_patch(temp_favorites_file):
    """Patch os.path.expanduser to return our temp favorites file"""
    with patch("os.path.expanduser", return_value=temp_favorites_file):
        yield temp_favorites_file


@pytest.fixture
def sample_favorites():
    """Sample favorites data"""
    return [
        {"joke": "Test joke 1", "saved_at": "2023-01-01 12:00:00"},
        {"joke": "Test joke 2", "saved_at": "2023-01-02 12:00:00"},
    ]


@pytest.fixture
def setup_favorites_file(favorites_path_patch, sample_favorites):
    """Setup a favorites file with sample data"""
    with open(favorites_path_patch, "w") as f:
        json.dump(sample_favorites, f)
    return favorites_path_patch
