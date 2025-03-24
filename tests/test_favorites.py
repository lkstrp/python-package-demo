import json
import os
from unittest.mock import MagicMock, patch

# Import functions from the joke_machine module
from joke_machine.app import list_favorites, save_favorite


def test_save_favorite_new_file(favorites_path_patch, capsys):
    """Test saving a favorite when the file doesn't exist yet"""
    joke = "This is a new favorite joke"

    with patch("datetime.datetime") as mock_datetime:
        mock_now = MagicMock()
        mock_now.strftime.return_value = "2023-01-01 12:00:00"
        mock_datetime.now.return_value = mock_now

        save_favorite(joke)

    # Verify file was created with correct content
    assert os.path.exists(favorites_path_patch)

    with open(favorites_path_patch) as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["joke"] == "This is a new favorite joke"

    captured = capsys.readouterr()
    assert "Joke saved to favorites" in captured.out


def test_save_favorite_append(setup_favorites_file, capsys):
    """Test appending a joke to existing favorites"""
    joke = "Another favorite joke"

    with patch("datetime.datetime") as mock_datetime:
        mock_now = MagicMock()
        mock_now.strftime.return_value = "2023-01-03 12:00:00"
        mock_datetime.now.return_value = mock_now

        save_favorite(joke)

    # Verify joke was appended
    with open(setup_favorites_file) as f:
        data = json.load(f)

    assert len(data) == 3  # Original 2 + new one
    assert data[2]["joke"] == "Another favorite joke"

    captured = capsys.readouterr()
    assert "Joke saved to favorites" in captured.out


def test_save_favorite_corrupted_file(favorites_path_patch, capsys):
    """Test saving a favorite when the file exists but is corrupted"""
    # Create a corrupted JSON file
    with open(favorites_path_patch, "w") as f:
        f.write("{this is not valid json")

    joke = "Joke to save after corruption"

    with patch("datetime.datetime") as mock_datetime:
        mock_now = MagicMock()
        mock_now.strftime.return_value = "2023-01-04 12:00:00"
        mock_datetime.now.return_value = mock_now

        save_favorite(joke)

    # Verify file was fixed and has the new joke
    with open(favorites_path_patch) as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["joke"] == "Joke to save after corruption"

    captured = capsys.readouterr()
    assert "Joke saved to favorites" in captured.out


def test_list_favorites_corrupted_file(favorites_path_patch, capsys):
    """Test listing favorites when the file is corrupted"""
    # Create a corrupted JSON file
    with open(favorites_path_patch, "w") as f:
        f.write("{this is not valid json")

    list_favorites()

    captured = capsys.readouterr()
    assert "Error reading favorites file" in captured.out
    assert "corrupted" in captured.out
