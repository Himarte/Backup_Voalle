import paramiko
import os
import schedule
import time
import os
import glob
import credentials

def print_progress(transferred, to_be_transferred):
    print(f"Progress: {transferred / to_be_transferred * 100:.2f}%")


def backup():
    local_file_path = "/mnt/MestreDosMagos/Sistemas/bkp"
    remote_file_path = "/bkp/"

    # check the number of files in the backup directory
    files = glob.glob(os.path.join(local_file_path, "*"))
    files.sort(key=os.path.getmtime)

    # if there are more than 10 files, delete the oldest ones
    while len(files) > 10:
        os.remove(files[0])
        del files[0]

    # create ssh client
    ssh_client = paramiko.SSHClient()

    # remote server credentials
    host = credentials.link
    username = credentials.user
    password = credentials.senha
    port = 22

    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)

    # create an SFTP client object
    ftp = ssh_client.open_sftp()

    # get list of all files in remote directory
    remote_files = ftp.listdir(remote_file_path)

    # download each file
    for file in remote_files:
        ftp.get(
            os.path.join(remote_file_path, file),
            os.path.join(local_file_path, file),
            callback=print_progress,
        )

    # close the connection
    ftp.close()
    ssh_client.close()


# schedule the backup function to run every 15 minutes
schedule.every(12).hours.do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)
