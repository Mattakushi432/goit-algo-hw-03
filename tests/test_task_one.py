from datetime import date


def test_valid_date() -> None:
    """Test valid date input."""
    from Task_one import get_days_from_today
    result = (date.today()  - date(year=2021, month=10, day=9)).days
    assert get_days_from_today("2021-10-09") == result


def test_future_date() -> None:
    """Test future date input."""
    from Task_one import get_days_from_today
    result = (date.today() - date(year=2030, month=6, day=15)).days
    assert get_days_from_today("2030-06-15") == result


def test_invalid_date_format() -> None:
    """Test invalid date format input."""
    from Task_one import get_days_from_today
    assert get_days_from_today("2021/10/09") is None


def test_invalid_input() -> None:
    """Test completely invalid input."""
    from Task_one import get_days_from_today
    assert get_days_from_today(3456) is None