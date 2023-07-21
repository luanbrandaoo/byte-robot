
# Byte Robot

The Byte Robot is a school project, with the aim of building an interactive and intelligent autonomous robot.


## Server

### Installing on server

- Install python 3.9

- Install espeak 
```bash
  sudo apt install espeak
```

- Install ffmpeg
```bash
  sudo apt install ffmpeg
```

- Install chatterbot
```bash
  git clone https://github.com/gunthercox/ChatterBot.git
  cd ChatterBot-master
  python3 setup.py install
```

- Install other requirements
```bash
  pip install -r requirements.txt
```

- Install spacy portuguese models
```bash
  python3 -m spacy download pt_core_news_lg
```

- Install ngrok

- Set api keys on credentials.json
```bash
{
  "openweathermap": ""
}
```

- Start server running main.py

### Using docker

```bash
docker run --network="host" -it byte
```


### Environment Variables

To run this project, you will need to add the following environment variables to "modules/credentials.json"
```bash
{
  "openweathermap": ""
}
```

## Credits

 - [sudharsanbaskars/AI-Chatbot](https://github.com/sudharsanbaskars/AI-Chatbot)
 - [basmilius/weather-icons](https://github.com/basmilius/weather-icons)
 - [Icons8](https://icons8.com)


## Other

#### The "tools" folder includes some useful files for the development.

- "train_chatterbot.py" can be used to train the chatterbot library.

- "xlsx_to_json.py" can be used to convert an xlsx file into a json file. It is specially used to write the jokes file.