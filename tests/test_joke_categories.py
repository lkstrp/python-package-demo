from unittest.mock import patch

import pytest

# Import functions from the joke_machine module
from joke_machine.app import generate_dad_joke_response, get_joke, tell_joke_with_delay


@pytest.mark.parametrize("category", ["programming", "dad", "puns"])
def test_joke_categories_exist(category):
    """Test that all expected joke categories exist"""
    with patch(
        "joke_machine.app.JOKES",
        {
            "programming": ["Programming joke"],
            "dad": ["Dad joke"],
            "puns": ["Pun joke"],
        },
    ):
        joke = get_joke(category)
        assert joke is not None


@patch("random.choice")
def test_programming_jokes(mock_choice):
    """Test getting programming jokes"""
    mock_choice.return_value = (
        "Why do programmers prefer dark mode? Because light attracts bugs!"
    )

    with patch(
        "joke_machine.app.JOKES",
        {
            "programming": [
                "Why do programmers prefer dark mode? Because light attracts bugs!"
            ]
        },
    ):
        joke = get_joke("programming")

    assert "programmers" in joke
    assert "bugs" in joke


@patch("random.choice")
def test_dad_jokes(mock_choice):
    """Test getting dad jokes"""
    mock_choice.return_value = (
        "I told my wife she was drawing her eyebrows too high. She looked surprised."
    )

    with patch(
        "joke_machine.app.JOKES",
        {
            "dad": [
                "I told my wife she was drawing her eyebrows too high. She looked surprised."
            ]
        },
    ):
        joke = get_joke("dad")

    assert joke is not None


@patch("random.choice")
def test_pun_jokes(mock_choice):
    """Test getting pun jokes"""
    mock_choice.return_value = "I'm on a seafood diet. I see food and I eat it."

    with patch(
        "joke_machine.app.JOKES",
        {"puns": ["I'm on a seafood diet. I see food and I eat it."]},
    ):
        joke = get_joke("puns")

    assert "seafood" in joke


@patch("time.sleep")
@patch("random.choice")
def test_dad_joke_response(mock_choice, mock_sleep, capsys):
    """Test that dad jokes get a response"""
    mock_choice.side_effect = [
        "Why don't eggs tell jokes? They'd crack each other up.",  # The joke
        "*groans*",  # The response
    ]

    with patch(
        "joke_machine.app.JOKES",
        {"dad": ["Why don't eggs tell jokes? They'd crack each other up."]},
    ):
        joke = get_joke("dad")
        tell_joke_with_delay(joke, delay=0)
        response = generate_dad_joke_response()
        print(f"\n{response}")

    captured = capsys.readouterr()
    assert "Why don't eggs tell jokes?" in captured.out
    assert "They'd crack each other up" in captured.out
    assert "*groans*" in captured.out
