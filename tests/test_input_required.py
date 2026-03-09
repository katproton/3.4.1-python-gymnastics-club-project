from validations import input_required, valid_name


# Test that valid input is accepted
def test_input_required_accepts_valid_input(monkeypatch):

    # Simulate user typing "kat"
    monkeypatch.setattr("builtins.input", lambda _: "kat")

    result = input_required("Name: ", valid_name)

    assert result == "Kat"


# tests that invalid input reprompts user
def test_input_required_reprompts_on_invalid(monkeypatch):
    from validations import input_required, valid_age

    inputs = iter(["25", "10"])  # first invalid, then valid
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = input_required("Age: ", valid_age)

    assert result == 10

