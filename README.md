# Simple AI Chatbot

## Requirement
have docker installed

## Build with
* [fast API](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [asyncio]() - asynchronous frameworks for websocket
* [jinja]() - template engine
* [Bootstrap](https://getbootstrap) - The CSS framework used
* [SASS](https://sass-lang.com/documentation) - CSS script language
* [Docker](https://docs.docker.com/) - Container for deployment
* [numpy](https://numpy.org/doc/stable/), 
  [tensorflow](https://www.tensorflow.org/overview),
  [scikit-learn](https://scikit-learn.org/stable/getting_started.html), and 
  [pickle](https://docs.python.org/3/library/pickle.html) - 
  training data(AI)

## Deployment
change model(run if you change the database)
```
python train.py
```
deploy server
```
docker-compose up
```
chatbot can be accessed at: http://localhost:8000/
## Source
* [How To Build Your Own Chatbot Using Deep Learning](https://developers.sap.com/tutorials/conversational-ai-faq-chatbot-beginner.html) -
[data](https://github.com/amilavm/Chatbot_Keras/blob/main/intents.json)
* [Sample for ChatBot](https://www.kaggle.com/code/himanshu01dadhich/sample-for-chatbot) - [data](https://www.kaggle.com/code/himanshu01dadhich/sample-for-chatbot/data?select=intents.json)

## Authors
**Syihabuddin Yahya Muhammad**  - [LastAeon](https://github.com/LastAeon), [SyihabuddinYahyaMuhammad](https://github.com/SyihabuddinYahyaMuhammad)