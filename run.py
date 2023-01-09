import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    while True:
        print("Please enter inweight for 5 vehicles, seperated by commas.")
       
        data_str = input("Enter value here: ")
   
        inweight = data_str.split(",")

        if validate_data(inweight):
            print("Data Valid")
            break

    return inweight


def get_outweight():
    """
    Get outweight from user
    """
    while True:
        print("Please enter outweight for 5 vehicles, seperated by commas.")
       
        data_str = input("Enter value here: ")
   
        outweight = data_str.split(",")

        if validate_data(outweight):
            print("Data Valid")
            break

    return outweight


def validate_data(values):
    """
    Check values are intergers and 5 values given
    """
    try:
        [int(value) for value in values]
        if len(values) != 5:
            raise ValueError("Please enter 5 values")
    except ValueError as e:
        print(f"Invalid data: {e}, try again.")
        return False

    return True


def update_inweight_worksheet(data):
    """
    Update inweight worksheet and add new row with csv data input
    """
    print("Updating inweight worksheet...")
    inweight_worksheet = SHEET.worksheet("inweight")
    inweight_worksheet.append_row(data)
    print("Inweight worksheet updated successfully")


def update_outweight_worksheet(data_two):
    """
    Update outweight worksheet and add new row with csv data input
    """
    print("Updating outweight worksheet...")
    outweight_worksheet = SHEET.worksheet("outweight")
    outweight_worksheet.append_row(data_two)
    print("Outweight worksheet updated successfully")
    

def calculate_netweight(inweight_row):
    """
    Calculate netweight by subtracting inweight from outweight.
    """
    print("Calculating netweight...")


def main():
    data = get_inweight()
    inweight = [int(num) for num in data]
    update_inweight_worksheet(inweight)
    data_two = get_outweight()
    outweight = [int(num) for num in data_two]
    update_outweight_worksheet(outweight)

    calculate_netweight(inweight)


print("Weighing Control System")
main()