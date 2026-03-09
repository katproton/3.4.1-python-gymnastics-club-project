from validations import valid_name


def test_valid_name_formats_correctly():
    # Arrange
    raw_name = "  kat perry  "

    # Act
    result = valid_name(raw_name)

    # Assert
    assert result == "Kat Perry"


def test_valid_name_raises_error_when_empty():
    # Arrange
    raw_name = ""

    # Act
    try:
        valid_name(raw_name)
        assert False, "Expected ValueError was not raised"

    except ValueError as e:
        # Assert
        assert "Name cannot be empty" in str(e)


def test_valid_name_rejects_numbers():
    # Arrange
    raw_name = "Kat123"

    # Act
    try:
        valid_name(raw_name)
        assert False, "Expected ValueError was not raised"

    except ValueError as e:
        # Assert
        assert "alphabetic" in str(e)
