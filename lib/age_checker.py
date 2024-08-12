from datetime import datetime, date

def age_checker(dob):

    # ------ NO INPUT 
    if dob == "":
        raise Exception("No text entered, please enter you date of birth: YYYY-MM-DD")

    # ------ CALCULATE USER'S AGE
    # today's date - get date - convert to str
    now = str(date.today())

    # parse dob & today into a datetime object -- 1st arg must be string, 2nd arg desired format
    today = datetime.strptime(now, "%Y-%m-%d").date()
    birthday = datetime.strptime(dob, "%Y-%m-%d").date()

    # difference between current date and user's birthday
    age = today - birthday

    # convert age into years -- round to nearest integer
    current_age = round(age.days / 365)
    
    

    # -------- GIVEN INPUT -- meets age requirements, access granted -- doesn't meet, access denied
    if current_age < 16:
        return f"Access denied, your current age is: {current_age} years and the required age is 16"
    return "Access granted"