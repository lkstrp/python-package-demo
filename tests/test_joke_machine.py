import pytest
import sys
import io
from unittest.mock import patch, MagicMock
import random
import os
import json
# Import functions from the joke_machine module
from joke_machine import (
    print_header,
    get_joke,
    get_fun_fact,
    generate_dad_joke_response,
    tell_joke_with_delay,
    save_favorite,
    list_favorites,
    interactive_mode,
    main,
)


def test_print_header(capsys):
    """Test that the header prints correctly"""
    print_header()
    captured = capsys.readouterr()
    assert "JokeMachine" in captured.out
    assert "Your daily dose of humor" in captured.out


@patch("random.choice")
def test_get_joke_no_category(mock_choice, mock_jokes):
    """Test getting a random joke with no category specified"""
    # Setup mock to return all jokes flattened
    all_jokes = []
    for jokes in mock_jokes.values():
        all_jokes.extend(jokes)
    mock_choice.return_value = "Selected joke"

    with patch("joke_machine.JOKES", mock_jokes):
        result = get_joke()

    assert result == "Selected joke"
    mock_choice.assert_called_once()


@patch("random.choice")
def test_get_joke_with_category(mock_choice, mock_jokes):
    """Test getting a joke from a specific category"""
    mock_choice.return_value = "Test joke 1"

    with patch("joke_machine.JOKES", mock_jokes):
        result = get_joke("test")

    assert result == "Test joke 1"
    mock_choice.assert_called_once_with(mock_jokes["test"])


@patch("random.choice")
def test_get_fun_fact(mock_choice, mock_facts):
    """Test getting a random fun fact"""
    mock_choice.return_value = "Test fact 1"

    with patch("joke_machine.FUN_FACTS", mock_facts):
        result = get_fun_fact()

    assert result == "Test fact 1"
    mock_choice.assert_called_once_with(mock_facts)


@patch("random.choice")
def test_generate_dad_joke_response(mock_choice):
    """Test generating a response to a dad joke"""
    mock_choice.return_value = "*groans*"

    result = generate_dad_joke_response()

    assert result == "*groans*"
    mock_choice.assert_called_once()


@patch("time.sleep")
def test_tell_joke_with_delay_question_format(mock_sleep, capsys):
    """Test telling a joke with a question mark format"""
    joke = "Why did the chicken cross the road? To get to the other side"

    tell_joke_with_delay(joke, delay=0.1)

    captured = capsys.readouterr()
    assert "Why did the chicken cross the road?" in captured.out
    assert "To get to the other side" in captured.out
    mock_sleep.assert_called_once_with(0.1)


@patch("time.sleep")
def test_tell_joke_with_delay_sentence_format(mock_sleep, capsys):
    """Test telling a joke with multiple sentences"""
    joke = "I have a joke. But it's not funny."

    tell_joke_with_delay(joke, delay=0.1)

    captured = capsys.readouterr()
    assert "I have a joke." in captured.out
    assert "But it's not funny." in captured.out
    mock_sleep.assert_called_once_with(0.1)


@patch("time.sleep")
def test_tell_joke_with_delay_simple_format(mock_sleep, capsys):
    """Test telling a simple joke without special formatting"""
    joke = "Simple joke"

    tell_joke_with_delay(joke, delay=0.1)

    captured = capsys.readouterr()
    assert "Simple joke" in captured.out
    mock_sleep.assert_not_called()


@patch("datetime.datetime")
def test_save_favorite(mock_datetime, favorites_path_patch, capsys):
    """Test saving a joke to favorites"""
    # Mock datetime.now() to return a fixed time
    mock_now = MagicMock()
    mock_now.strftime.return_value = "2023-01-01 12:00:00"
    mock_datetime.now.return_value = mock_now

    joke = "Test joke to save"

    save_favorite(joke)

    # Check that the joke was saved to the file
    with open(favorites_path_patch, "r") as f:
        saved_data = json.load(f)

    assert len(saved_data) == 1
    assert saved_data[0]["joke"] == "Test joke to save"

    # Check console output
    captured = capsys.readouterr()
    assert "Joke saved to favorites" in captured.out


def test_list_favorites_with_data(setup_favorites_file, capsys):
    """Test listing favorites when there are saved jokes"""
    list_favorites()

    captured = capsys.readouterr()
    assert "Your Favorite Jokes" in captured.out
    assert "Test joke 1" in captured.out
    assert "Test joke 2" in captured.out
    assert "Saved on: 2023-01-01" in captured.out


def test_list_favorites_empty(favorites_path_patch, capsys):
    """Test listing favorites when there are no saved jokes"""
    # Create empty favorites file
    with open(favorites_path_patch, "w") as f:
        json.dump([], f)

    list_favorites()

    captured = capsys.readouterr()
    assert "Your favorites list is empty" in captured.out


def test_list_favorites_no_file(favorites_path_patch, capsys):
    """Test listing favorites when the favorites file doesn't exist"""
    # Ensure file doesn't exist
    if os.path.exists(favorites_path_patch):
        os.unlink(favorites_path_patch)

    list_favorites()

    captured = capsys.readouterr()
    assert "You haven't saved any favorites yet" in captured.out
