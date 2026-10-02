from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def main():
    current_dir = Path(__file__).resolve().parent
    credentials_path = current_dir / 'credentials.json'
    
    flow = InstalledAppFlow.from_client_secrets_file(str(credentials_path), SCOPES)
    creds = flow.run_local_server(port=8080)
    
    print("YOUR REFRESH TOKEN:")
    print(creds.refresh_token)
    print("YOUR CLIENT ID:")
    print(creds.client_id)
    print("YOUR CLIENT SECRET:")
    print(creds.client_secret)

if __name__ == '__main__':
    main()
