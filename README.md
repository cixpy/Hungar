# Hungar - Discord Bot

Um bot multifuncional para Discord escrito em Python usando a biblioteca discord.py.

## Funcionalidades

- **Comandos de matemática**: Operações básicas (soma, subtração, multiplicação, divisão) e cálculo de porcentagens
- **Sincronização de comandos**: Comando administrativo para sincronizar comandos de barra (slash commands)
- **Eventos de membro**: Mensagem automática quando membros saem do servidor
- **Sistema de cogs**: Arquitetura modular para fácil extensão
- **Integrações adicionais**: Música, IA, jogos, e muito mais

## Estrutura do Projeto

```
hungar/
├── main.py              # Arquivo principal do bot
├── requirements.txt     # Dependências do projeto
├── .env-example         # Exemplo de arquivo de variáveis de ambiente
├── cogs/                # Módulos (extensões) do bot
│   ├── math.py          # Comandos de matemática
│   ├── cleanup.py       # Funções de limpeza
│   ├── gym.py           # Comandos relacionados à academia/fitness
│   ├── lol.py           # Comandos relacionados ao League of Legends
│   ├── messages.py      # Manipulação de mensagens
│   ├── music.py         # Sistema de reprodução de música
│   ├── openroute_ai.py  # Integração com IA (OpenRouter)
│   └── cog_model/       # Modelo para criação de novos cogs
└── .git/                # Repositório Git
```

## Pré-requisitos

- Python 3.8 ou superior
- Conta no Discord com permissão para criar aplicações/bots
- Token do bot do Discord

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/yourusername/hungar.git
   cd hungar
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Copie `.env-example` para `.env`
   - Edite `.env` e adicione seu token do Discord:
     ```
     DISCORD_TOKEN=seu_token_aqui
     ```

## Uso

1. Ative o ambiente virtual (se criou um):
   ```bash
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

2. Execute o bot:
   ```bash
   python main.py
   ```

3. O bot mostrará "BOT ON!" no console quando estiver pronto e conectado ao Discord.

## Comandos Principais

### Matemática (disponíveis como slash commands)
- `/somar <número1> <número2>` - Soma dois números
- `/subtrair <número1> <número2>` - Subtrai o segundo número do primeiro
- `/multiplicar <número1> <número2>` - Multiplica dois números
- `/dividir <número1> <número2>` - Divide o primeiro número pelo segundo (não permite divisão por zero)
- `/porcentagem <percentual> <valor>` - Calcula a porcentagem de um valor

### Administração
- `/syncro` - Sincroniza os comandos de barra (apenas para usuários autorizados específicos)

## Configuração

O bot pode ser configurado através das seguintes variáveis de ambiente no arquivo `.env`:

- `DISCORD_TOKEN`: Token do seu bot do Discord (obrigatório)

Alguns cogs podem requerer configurações adicionais. Verifique os arquivos individuais em `cogs/` para mais detalhes.

## Contribuindo

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Faça commit das suas alterações (`git commit -m 'Add some AmazingFeature'`)
4. Faça push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## Aviso Legal

Este bot é para uso educacional e de entretenimento. Certifique-se de cumprir os Termos de Serviço do Discord ao usar este bot.