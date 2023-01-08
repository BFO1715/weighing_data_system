import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('WeighingData')


def get_inweight():
    """
    Get inweight from user
    """
    print("Please enter inweight values for 5 vehicles, seperated by commas.")
    data_str = input("Enter value here: ")
    
    inweight = data_str.split(",")
    validate_data(inweight)


def validate_data(values):
    """
    Check values are intergers and 5 values given
    """
    try:
        if len(values) != 5:
            raise ValueError("Please enter 5 values")
    except ValueError as e:
        print(f"Invalid data: {e}, 1try again.")


get_inweight()