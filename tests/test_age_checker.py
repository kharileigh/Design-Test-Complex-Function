from lib.age_checker import *
import pytest


# ----- NO INPUT GIVEN 
def test_age_checker_no_input():

    with pytest.raises(Exception) as err:
        age_checker("")
    error_message = str(err.value)
    
    assert error_message == "No text entered, please enter you date of birth: YYYY-MM-DD"