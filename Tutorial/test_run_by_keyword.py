# pytest -vsqrA -k login   ----- runs all the test with login keyword
# pytest -vsqrA -k _valid   ----- runs all the test with _valid keyword
# pytest -vsqrA -k "login or registration"   ----- runs all the test with _valid keyword

def test_valid_login():
    print("Valid Login")

def test_invalid_login():
    print("InValid Login")

def test_valid_registration():
    print("Valid Registration")

def test_invalid_registration():
    print("inValid Registration")