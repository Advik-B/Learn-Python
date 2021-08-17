from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

uploaded = drive.CreateFile({'title': 'sample_doc.txt'})
uploaded.SetContentString('Sample upload file content this will be later replaced with some text')
uploaded.Upload()
print(f'Uploaded file with ID {0}'.format(uploaded.get('id')))
