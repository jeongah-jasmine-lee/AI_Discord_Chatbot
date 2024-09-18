# AI_Discord_Chatbot (RLO Project 5)

### Members
- Jeongah Lee
- Patrick Do
- Mingchen Li
- Zeyuan Yang

### Requirements
```
pip install discord openai python-dotenv 
```

### Steps
1. Make a new server in Discord App

2. Create a new application Bot in Discord Website
https://discord.com/developers/applications <br> Allow (1) PRESENCE INTENT (2) SERVER MEMBERS INTENT (3) MESSAGE CONTENT INTET in the settings

3. Connect Server and Bot<br>
Go to Setting in Discord Website -> Click OAuth2 -> Check 'bot' in OAuth2 URL Generator

4. Open Discord and paste the URL in Step3
5. Make an .env file and fill your DISCORD_TOKEN
    ```
    ex. DISCORD_TOKEN = "123abc"
    ```
6. Run bot.py
