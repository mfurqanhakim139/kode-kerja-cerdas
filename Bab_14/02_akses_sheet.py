import os
import sys  # Added for sys.exit
import json  # Added for more robust error handling

# Import necessary Google libraries
# Install/upgrade: pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# --- Configuration ---
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# --- !!! UPDATE THESE VALUES !!! ---
# Use YOUR Spreadsheet ID
# SPREADSHEET_ID = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"  # Original Sample ID
SPREADSHEET_ID = "1GNokDQToXnEmcd8PZ6LJxEb5CbOL5s6ALVHAmaTXpX8"  # YOUR SPREADSHEET ID

# The range to read data from. Examples:
# 'Sheet1!A1:C10' -> Range A1 to C10 on Sheet1
# 'MySheetName' -> Reads all data from sheet named 'MySheetName'
# 'A:C' -> Reads all data from columns A to C on the first visible sheet
RANGE_NAME = "Sheet1!A2:E"  # Keep Sample Range for now, CHANGE AS NEEDED

# --- File Names ---
CREDENTIALS_FILENAME = "credentials.json"  # Make sure this matches your downloaded file
TOKEN_FILENAME = "token.json"
# ---------------------


def authenticate_google_sheets():
    """Handles authentication flow for Google Sheets API."""
    creds = None
    # The file token.json stores the user's access and refresh tokens,
    # and is created automatically when the authorization flow completes
    # for the first time.
    if os.path.exists(TOKEN_FILENAME):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILENAME, SCOPES)
            print(f"Credentials loaded from {TOKEN_FILENAME}.")
        except Exception as e:
            print(f"Error loading token file '{TOKEN_FILENAME}': {e}")
            print("Attempting re-authentication.")
            creds = None  # Force re-authentication

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                print("Credentials expired, attempting refresh...")
                creds.refresh(Request())
                print("Credentials refreshed successfully.")
            except Exception as e:
                print(f"Error refreshing token: {e}")
                print("Proceeding with full authentication flow.")
                creds = None  # Force re-authentication
        else:
            # Run the full authentication flow
            try:
                print(
                    f"No valid credentials found or refresh failed. Starting authentication flow using '{CREDENTIALS_FILENAME}'..."
                )
                if not os.path.exists(CREDENTIALS_FILENAME):
                    print(
                        f"ERROR: Credentials file '{CREDENTIALS_FILENAME}' not found in the current directory."
                    )
                    print("Please download it from Google Cloud Console and place it here.")
                    return None  # Return None if credentials file is missing

                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_FILENAME, SCOPES
                )
                # run_local_server will open the browser for user authorization.  Set a port.
                creds = flow.run_local_server(port=0)  # Let it choose a free port.
                print("Authentication successful.")
            except FileNotFoundError:
                print(f"ERROR: Credentials file '{CREDENTIALS_FILENAME}' not found.")
                return None
            except Exception as e:
                print(f"Error during authentication flow: {e}")
                return None

        # Save the credentials for the next run if authentication was successful
        if creds:
            try:
                with open(TOKEN_FILENAME, "w") as token:
                    token.write(creds.to_json())
                print(f"Credentials saved to {TOKEN_FILENAME}.")
            except Exception as e:
                print(f"Error saving token file: {e}")

    return creds


def read_spreadsheet_data(creds):
    """Reads data from the specified spreadsheet and range using authenticated credentials."""
    if not creds:
        print("Authentication failed, cannot read data.")
        return

    try:
        print("\nBuilding Google Sheets service...")
        service = build("sheets", "v4", credentials=creds)
        print("Service built successfully.")

        # Call the Sheets API to get values
        sheet = service.spreadsheets()
        print(f"Reading data from Spreadsheet ID: {SPREADSHEET_ID}, Range: {RANGE_NAME}")
        result = (
            sheet.values()
            .get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])  # Get the 'values' list, default to empty list if not found

        if not values:
            print("No data found in the specified range.")
            return

        print("\n--- Data Read ---")
        # --- Customize how you process the data here ---
        # This example prints the first and fifth column (indices 0 and 4)
        # Adjust indices based on your RANGE_NAME and desired columns
        print("Example Output (Column 1, Column 5):")
        for row in values:
            # Basic check to avoid IndexError if row is shorter than expected
            col1 = row[0] if len(row) > 0 else "N/A"
            col5 = row[4] if len(row) > 4 else "N/A"
            print(f"- {col1}, {col5}")
        # ------------------------------------------------

    except HttpError as err:
        print(f"\nAn API error occurred: {err}")
        try:
            error_details = json.loads(err.content.decode('utf-8'))
            print(f"Full Error Details: {error_details}")  # Print the entire error
            if err.resp.status == 403:
                print("-> Possible causes for 403 error:")
                print(
                    "   - Google Sheets API might not be enabled in your Google Cloud project."
                )
                print(
                    "   - The account associated with the token might not have permission to access the spreadsheet."
                )
                print("   - You might need to delete 'token.json' and re-authenticate.")
            elif err.resp.status == 404:
                print("-> Possible causes for 404 error:")
                print(f"     - Spreadsheet ID '{SPREADSHEET_ID}' might be incorrect.")
                print(f"     - Sheet name or range '{RANGE_NAME}' might be incorrect.")
        except json.JSONDecodeError:
            print(f"Could not decode error response: {err.content}")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    
    return values  # Return the data


# --- Main Execution Block ---
if __name__ == "__main__":
    print("Starting Google Sheets API script...")
    credentials = authenticate_google_sheets()
    if credentials:
        data = read_spreadsheet_data(credentials)
        if data:
            print("\nData successfully read from the spreadsheet.")
            #  You can add code here to process the data.
        else:
            print("\nFailed to read data from the spreadsheet.")
    else:
        print("Could not obtain valid credentials. Exiting.")
    print("\nScript finished.")
