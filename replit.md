# Discord Bot - Comandos com Embeds

## Visão Geral
Bot Discord em Python usando discord.py que responde a comandos slash (/) com embeds organizados contendo links para recursos de executors de Roblox.

## Arquitetura
- **bot.py**: Arquivo principal do bot com todos os comandos e lógica
- **Biblioteca**: discord.py 2.x com suporte a comandos slash (app_commands)
- **Configuração**: Token via variável de ambiente DISCORD_TOKEN

## Comandos Disponíveis
| Comando | Descrição |
|---------|-----------|
| `/volcano` | Link do Volcano Executor |
| `/delta` | Link do Delta Executor |
| `/xeno` | Link do Xeno Executor |
| `/fluxus` | Link do Fluxus Z APK |
| `/deltadesync` | Link do Delta Desync APK |
| `/help` | Lista todos os comandos |

## Estrutura dos Embeds
- **Cor**: Amarelo (#FFFF00)
- **Título**: Nome do executor
- **Descrição**: "Obter link do executor [nome]"
- **Campo**: Link clicável
- **Timestamp**: Data/hora atual
- **Footer**: "Solicitado por [usuário]" com avatar

## Configuração do Token

### 1. Criar Aplicação Discord
1. Acesse [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique em "New Application" e dê um nome
3. Vá para "Bot" no menu lateral
4. Clique em "Reset Token" e copie o token

### 2. Configurar Intents
1. Na seção "Bot", role até "Privileged Gateway Intents"
2. Ative "Message Content Intent"

### 3. Convidar o Bot
1. Vá para "OAuth2" > "URL Generator"
2. Em Scopes, selecione: `bot` e `applications.commands`
3. Em Bot Permissions, selecione as permissões necessárias
4. Copie a URL gerada e abra no navegador para convidar

### 4. Configurar Token no Replit
1. Vá para a aba "Secrets" no Replit
2. Adicione:
   - Key: `DISCORD_TOKEN`
   - Value: (seu token copiado)

## Executando o Bot
Clique em "Run" no Replit. O bot vai:
1. Conectar ao Discord
2. Sincronizar os comandos slash
3. Ficar online aguardando comandos

## Tratamento de Erros
- Token ausente: Mensagem clara com instruções
- Token inválido: Alerta de login failure
- Erros de comando: Resposta ephemeral ao usuário + log no console

## Dependências
- discord.py >= 2.0
- python-dotenv

## Mudanças Recentes
- **01/12/2025**: Criação inicial do bot com 5 comandos de recursos + comando /help
