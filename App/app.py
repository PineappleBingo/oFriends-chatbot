from decouple import config
from embedchain import Pipeline as App

# app = App.from_config(config_path="config.yaml")
# app = App.from_config(config_path="config.json")
OPENAI_API_KEY = config("OPENAI_API_KEY")

app = App()


app.add("https://overline.network/")
app.add("https://overline.network/oland")

# youtube
# https://www.youtube.com/watch?v=oQsEEdNxVOg&t=2s


# app.add("path/to/file/elon_musk.pdf")

print(app.query("What is oland?"))
# Answer: The net worth of Elon Musk today is $258.7 billion.
