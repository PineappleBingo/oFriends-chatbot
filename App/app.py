from decouple import config
from embedchain import Pipeline as App

# app = App.from_config(config_path="config.yaml")
# app = App.from_config(config_path="config.json")
OPENAI_API_KEY = config("OPENAI_API_KEY")

app = App()


# https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
# https://www.youtube.com/watch?v=qr2w_aEn5lc

# app.add("https://overline.network/")
# app.add("https://overline.network/oland")

# youtube
# https://www.youtube.com/watch?v=oQsEEdNxVOg&t=2s
# D:\gitprojects\oFriends-chatbot\App\overline-ama-7-14-23.pdf

# app.add("path/to/file/elon_musk.pdf")
# app.add("overline-ama-7-14-23.pdf", data_type="pdf_file")
# app.add("overline-ama-7-14-23.pdf")
# app.add("..data/ama/overline-ama-7-22-23.pdf")
# app.add("..data/ama/overline-ama-8-10-23.pdf")
# app.add("..data/ama/overline-ama-8-22-23.pdf")
# app.add("..data/ama/overline-ama-9-9-23.pdf")
# app.add("..data/ama/overline-ama-9-20-23.pdf")
# app.add("..data/ama/overline-ama-10-11-23.pdf")
# app.add("..data/ama/overline-ama-11-5-23.pdf")
# app.add("..data/ama/overline-ama-11-14-23.pdf")
# app.add("..data/ama/overline-ama-11-24-23.pdf")
# app.add("..data/ama/overline-ama-11-26-23.pdf")
# app.add("..data/ama/overline-ama-12-7-23.pdf")


# print(app.query("Tell me about Ocash mining?"))
# Answer: The net worth of Elon Musk today is $258.7 billion.
