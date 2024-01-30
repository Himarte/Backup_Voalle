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

1. **Credenciais:**
   Certifique-se de acertar as credenciais no script, contendo as informações necessárias para autenticação no servidor remoto. Exemplo:

```python
# remote server credentials

host = "synsuite.himarte.com.br"
username = "backup_erp"
password = "4WCDfvq!"
port = 22
```

2. **Configurações de Backup:**
Personalize as configurações de backup no script, como os caminhos locais e remotos, bem como a frequência do agendamento.

 ```python
 local_file_path = "/root/bkp_voalle/bkp/"
 remote_file_path = "/bkp/"
 ```

3.**Agendamento**
Agendar a função de backup para ser executada todos os dias às 5 horas da manhã

```bash
schedule.every().day.at("05:00").do(backup)
```

# Acessar servidor local

Para acessar o server local é recomendando acessar via SSH port:22, sendo possivel outros meios também.

```bash
ssh root@192.168.254.151 -22
```

Entrar no diretório em que o code se localiza:
```bash
cd bkp_voalle
```

## Execução em Segundo Plano

Certifique-se de executar o script em segundo plano, por exemplo, utilizando o utilitário `nohup`:

```bash
nohup python3 backup.py > backup.log 2>&1 &
```

    `python3 backup.py`: Executa o script Python.
    `> backup.log`: Redireciona a saída padrão para um arquivo chamado output.log.
    `2>&1`: Redireciona os erros padrão para a mesma localização da saída padrão (ou seja, para output.log).
    `&`: Permite que o comando seja executado em segundo plano.

Nota: Este comando redireciona tanto a saída padrão quanto os erros padrão para o arquivo output.log. Isso é útil para registrar todos os resultados, incluindo mensagens de erro, em um arquivo de log.

## Notas

Lembre-se sempre de revisar e adaptar o script de acordo com os requisitos específicos do seu ambiente e política de segurança.

3. **Verificar se o código está rodando**

```bash
ps aux | grep '[b]ackup.py'
```

Nota: A resposta padrão deve ser algo como:

```bash
root@truenas[~/bkp_voalle]# ps aux | grep '[b]ackup.py'
root        7647   0.8  0.4   39224  26772  5  SN   10:55        0:00.12 python3 backup.py (python3.9)
```

4. **Acessar diretório para transferir arquivo com WinSCP**

WinSCP é o programa utilizado apra realizar acesso SSH para ter uma inrterface visual mais amigával. Através dela a transferência de arquivos é fácil, possibilitanto transferencia entre máquinas.
