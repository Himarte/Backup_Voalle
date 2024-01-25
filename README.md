# Backup Automático com Paramiko e Schedule

Este é um script Python projetado para rodar em segundo plano em um servidor TrueNAS, realizando backups automáticos de arquivos de um servidor remoto para um diretório local. O script utiliza as bibliotecas `paramiko` para conexão SSH e `schedule` para agendamento de tarefas.

## Descrição

O script realiza a seguinte operação:

1. Conecta-se ao servidor remoto por meio de uma conexão SSH utilizando a biblioteca `paramiko`.
2. Verifica o número de arquivos no diretório de backup local e exclui os mais antigos se houver mais de 10.
3. Estabelece uma conexão SFTP (SSH File Transfer Protocol) para o servidor remoto.
4. Baixa cada arquivo do diretório remoto para o diretório local de backup, exibindo o progresso da transferência.
5. Agendamento da função de backup para ser executada a cada 12 horas usando a biblioteca `schedule`.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas no ambiente onde o script será executado:

```bash
pip install paramiko schedule
```

## Configuração

1. **Arquivo de Credenciais:**
   Certifique-se de ter um arquivo de credenciais (por exemplo, `credentials.py`) no mesmo diretório do script, contendo as informações necessárias para autenticação no servidor remoto. Exemplo:

   ```python
   # credentials.py
   link = "endereco_do_servidor"
   user = "nome_de_usuario"
   senha = "senha_secreta"
   ```

2. **Configurações de Backup:**
   Personalize as configurações de backup no script, como os caminhos locais e remotos, bem como a frequência do agendamento.

    ```python
    local_file_path = "/mnt/MestreDosMagos/Sistemas/bkp"
    remote_file_path = "/bkp/"
    ```

    Schedule the backup function to run every 12 hours

    ```python
    schedule.every(12).hours.do(backup)
    ```

## Execução em Segundo Plano

Certifique-se de executar o script em segundo plano, por exemplo, utilizando o utilitário `nohup`:

```bash
nohup python3 seu_script.py > output.log 2>&1 &
```

    `python3 backup.py`: Executa o script Python.
    `> output.log`: Redireciona a saída padrão para um arquivo chamado output.log.
    `2>&1`: Redireciona os erros padrão para a mesma localização da saída padrão (ou seja, para output.log).
    `&`: Permite que o comando seja executado em segundo plano.

Nota: Este comando redireciona tanto a saída padrão quanto os erros padrão para o arquivo output.log. Isso é útil para registrar todos os resultados, incluindo mensagens de erro, em um arquivo de log.

## Notas

Lembre-se sempre de revisar e adaptar o script de acordo com os requisitos específicos do seu ambiente e política de segurança.
