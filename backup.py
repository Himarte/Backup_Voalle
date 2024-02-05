import paramiko
import os
import schedule
import time
import glob
import logging

logging.basicConfig(filename="backup.log", level=logging.INFO)


#def print_progress(transferred, to_be_transferred):
 #   print(f"Progress: {transferred / to_be_transferred * 100:.2f}%")


def BackupDados():
    local_file_path = "/mnt/MestreDosMagos/Sistemas/bkpVoalle/Dados"
    remote_file_path = "/bkp/"

    try:
        # create ssh client
        ssh_client = paramiko.SSHClient()

        # remote server credentials
        host = "synsuite.himarte.com.br"
        username = "backup_erp"
        password = "4WCDfvq!"
        port = 22

        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            hostname=host, port=port, username=username, password=password
        )

        # create an SFTP client object
        ftp = ssh_client.open_sftp()

        # get list of all files in remote directory
        remote_files = ftp.listdir(remote_file_path)

        # check the files in the backup directory
        files = glob.glob(os.path.join(local_file_path, "*"))
        files.sort(key=os.path.getmtime)

         # remove all local files
        for file in files:
            os.remove(file)
               

        # download each file
        for file in remote_files:
            ftp.get(
                os.path.join(remote_file_path, file),
                os.path.join(local_file_path, file),
                #callback=print_progress,
            )

        # close the connection
        ftp.close()
        ssh_client.close()
        logging.info("Backup Dados successfully completed.")
    except Exception as e:
        logging.error(f"Error during BackupDados: {e}")
    

def BackupRadius():
    local_file_path = "/mnt/MestreDosMagos/Sistemas/bkpVoalle/Radius"
    remote_file_path = "/bkp/"

    try:
        # create ssh client
        ssh_client = paramiko.SSHClient()

        # remote server credentials
        host = "190.111.179.188"
        username = "backup_erp"
        password = "4WCDfvq!"
        port = 22512

        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            hostname=host, port=port, username=username, password=password
        )

        # create an SFTP client object
        ftp = ssh_client.open_sftp()

        # get list of all files in remote directory
        remote_files = ftp.listdir(remote_file_path)

        # check the files in the backup directory
        files = glob.glob(os.path.join(local_file_path, "*"))
        files.sort(key=os.path.getmtime)

         # remove all local files
        for file in files:
            os.remove(file)

        

        # download each file
        for file in remote_files:
            ftp.get(
                os.path.join(remote_file_path, file),
                os.path.join(local_file_path, file),
               # callback=print_progress,
            )

        # close the connection
        ftp.close()
        ssh_client.close()
        logging.info("Backup Radius successfully completed.")
    except Exception as e:
        logging.error(f"Error during BackupRadius: {e}")


def BackupVoalle():
    BackupDados()
    BackupRadius()

# Agendar a função de backup para ser executada todos os dias às 5 horas da manhã
schedule.every().day.at("04:00").do(BackupVoalle)


while True:
    schedule.run_pending()
    time.sleep(1)
