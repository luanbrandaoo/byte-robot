
# Byte Robot

The Byte Robot is a school project, with the aim of building an interactive and intelligent autonomous robot.


## Server

### Installing on server

- Install Python 3.9

- Install eSpeak 
```bash
  sudo apt install espeak
```

- Install FFmpeg
```bash
  sudo apt install ffmpeg
```

- Install Python requirements
```bash
  pip install -r requirements.txt
```

- Install Spacy portuguese models
```bash
  python3 -m spacy download pt_core_news_lg
```

- Install Ngrok

- Set api keys on credentials.json
```bash
{
  "openweathermap": ""
}
```

- Start server running main.py

### Using Docker

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

 - [basmilius/weather-icons](https://github.com/basmilius/weather-icons)
 - [Icons8](https://icons8.com)


## Other

#### The "tools" folder includes some useful files for the development.

- "xlsx_to_json.py" can be used to convert an xlsx file into a json file. It is specially used to write the jokes file.