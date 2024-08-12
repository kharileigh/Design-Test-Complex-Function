from lib.age_checker import *
import pytest


# ----- NO INPUT GIVEN 
def test_age_checker_no_input():

    with pytest.raises(Exception) as err:
        age_checker("")
    error_message = str(err.value)
    
    assert error_message == "No text entered, please enter you date of birth: YYYY-MM-DD"


# ------ ACCESS DENIED
def test_age_checker_denied():

    assert age_checker("2010-11-04") == "Access denied, your current age is: 14 years and the required age is 16"


# ------ ACCESS GRANTED
def test_age_checker_granted():

    assert age_checker("2007-04-04") == "Access granted"