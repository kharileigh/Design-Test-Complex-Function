## 1. Describe the Problem
As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

------- Check Age
------- Under 16, DENIED ACCESS
------- 16 or OLDER, ACCESS GRANTED


## 2. Design the Function/Class Signature
NAME
def age_checker(DOB):

    PARAMETERS
    DOB : str -- holding users date of birth


    RETURN
    str -- access granted
    OR 
    str -- access denied


    FUNCTIONALITY 
    if DOB >= 16:
        return "Access Granted"

    return str f"Access denied, your current age is: {age today} and the required age is 16


    SIDE EFFECTS
    need to get today's date from datetime
    need to get user's age from datetime
    subtract user's date from today's date to get user's age
    
        

## 3. Create Examples as Tests
def test_age_checker_no_input():

    with pytest.raises(Exception) as err:
        age_checker("")
    error_message = str(err.value)
    assert error_message == "No text entered, please enter you date of birth: YYYY-MM-DD"


def test_age_checker_denied():
    
    assert age_checker("2010-11-04") == "Access denied, your current age is: 14 years and the required age is 16"


def test_age_checker_granted():
    assert age_checker("2007-04-04") == "Access granted"


## 4. Implement the Behaviour