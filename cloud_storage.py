import dropbox 

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AxibQnDp3UsZ3kS1AhHClzjtNrKsIEhhj4YigvWqEpnRp8RlK9CVNYp19nsTlErfs5nTiHsXjjpNtXEMAqP_tQWJkjvl_vn84coGB71Kd4RXJ5f59kQA_Ts2KX-BO9Bmf4aZ5t4'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to Dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("The file has been moved!!!")

main()