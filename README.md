# Simple AI Chatbot

## Requirement
have docker installed
have openrouter api key

## Build with
* [fast API](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [asyncio]() - asynchronous frameworks for websocket
* [jinja]() - template engine
* [Bootstrap](https://getbootstrap) - The CSS framework used
* [SASS](https://sass-lang.com/documentation) - CSS script language
* [Docker](https://docs.docker.com/) - Container for deployment

## Deployment
create an .env file with format
```
cp ./src/.env.example ./src/.env
```

fill the OPENROUTER_API_KEY with your OPENROUTER_API_KEY
```
OPENROUTER_API_KEY=<put your key here>
```

deploy server with command
```
docker-compose up
```
chatbot can be accessed at: http://localhost:8000/
## Source
* [ai-chat-app](https://github.com/teguhss/ai-chat-app/)
* [Conversation Agent](https://gitlab.com/LastAeon/prosa-entrance-task-conversation-agent)

## Authors
**Syihabuddin Yahya Muhammad**  - [LastAeon](https://github.com/LastAeon), [SyihabuddinYahyaMuhammad](https://github.com/SyihabuddinYahyaMuhammad)