import paramiko
import os
import schedule
import time
import glob
import logging
import credentials

logging.basicConfig(filename="backup.log", level=logging.INFO)


def print_progress(transferred, to_be_transferred):
    print(f"Progress: {transferred / to_be_transferred * 100:.2f}%")


def BackupDados():
    local_file_path = credentials.local_file_path1
    remote_file_path = credentials.remote_file_path1

    try:
        # cria um cliente ssh
        ssh_client = paramiko.SSHClient()

        # credenciais do servidor remoto
        host = credentials.host1
        username = credentials.username1
        password = credentials.password1
        port = credentials.port1

        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            hostname=host, port=port, username=username, password=password
        )

        # cria um objeto cliente SFTP
        ftp = ssh_client.open_sftp()

        # checa os arquivos no diretório remoto
        remote_files = ftp.listdir(remote_file_path)

        # checa os arquivos no diretório de backup
        files = glob.glob(os.path.join(local_file_path, "*"))
        files.sort(key=os.path.getmtime)

        # se o arquivo local não estiver na lista de arquivos remotos, exclua-o
        for file in files:
            if os.path.basename(file) not in remote_files:
                os.remove(file)
                files.remove(file)

        # download archivo por archivo
        for file in remote_files:
            ftp.get(
                os.path.join(remote_file_path, file),
                os.path.join(local_file_path, file),
                callback=print_progress,
            )

        # fechar conexão
        ftp.close()
        ssh_client.close()
        logging.info("Backup Dados successfully completed.")
    except Exception as e:
        logging.error(f"Error during BackupDados: {e}")


def BackupRadius():
    local_file_path = credentials.local_file_path2
    remote_file_path = credentials.remote_file_path2

    try:
        # cria um cliente ssh
        ssh_client = paramiko.SSHClient()

        # credenciais do servidor remoto
        host = credentials.host2
        username = credentials.username2
        password = credentials.password2
        port = credentials.port2

        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            hostname=host, port=port, username=username, password=password
        )

        # cria um objeto cliente SFTP
        ftp = ssh_client.open_sftp()

        # checa os arquivos no diretório remoto
        remote_files = ftp.listdir(remote_file_path)

        # confere os arquivos no diretório de backup
        files = glob.glob(os.path.join(local_file_path, "*"))
        files.sort(key=os.path.getmtime)

        # se o arquivo local não estiver na lista de arquivos remotos, exclua-o
        for file in files:
            if os.path.basename(file) not in remote_files:
                os.remove(file)
                files.remove(file)

        # download arquivo por arquivo
        for file in remote_files:
            ftp.get(
                os.path.join(remote_file_path, file),
                os.path.join(local_file_path, file),
                callback=print_progress,
            )

        # fecha conexão
        ftp.close()
        ssh_client.close()
        logging.info("Backup Radius successfully completed.")
    except Exception as e:
        logging.error(f"Error during BackupRadius: {e}")


# agendar a função de backup para ser executada todos os dias às 5 horas da manhã
schedule.every().day.at("05:00").do(BackupDados, BackupRadius)

while True:
    schedule.run_pending()
    time.sleep(1)
