
# Byte - Server

The Byte Robot is a school project, with the aim of building an interactive and intelligent autonomous robot.




## Installing

- Install python 3.9

- Install espeak 
```bash
  sudo apt install espeak
```

- Install ffmpeg
```bash
  sudo apt install ffmpeg
```

- Install requirements
```bash
  pip install -r requirements.txt
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


## Environment Variables

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

