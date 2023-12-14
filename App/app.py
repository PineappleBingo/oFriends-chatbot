from decouple import config
from embedchain import Pipeline as App

# app = App.from_config(config_path="config.yaml")
# app = App.from_config(config_path="config.json")
OPENAI_API_KEY = config("OPENAI_API_KEY")

app = App()

app.add("https://en.wikipedia.org/wiki/Elon_Musk")
app.add("https://www.forbes.com/profile/elon-musk")
# app.add("path/to/file/elon_musk.pdf")

print(app.query("What is the net worth of Elon Musk today?"))
# Answer: The net worth of Elon Musk today is $258.7 billion.
