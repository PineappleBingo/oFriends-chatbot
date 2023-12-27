# import os

# path = os.path.dirname(__file__)
# my_file = path + "/12842.png"

# print("path:", path)
# print("my_file:", my_file)

css = """

"""

bot_template = """
    <div class="chat-message bot">
        <div class="avatar">
            <img src="https://ibb.co/1z0tSRZ" style="max-height: 78px; max-width: 78px; border-radius: 50%;"/>
        </div>
        <div class="message">{{MSG}}</div>
    </div>
"""

user_template = """
    <div class="chat-message user">
        <div class="avatar">
            <img src="https://ibb.co/3SRhXhf" style="max-height: 78px; max-width: 78px; border-radius: 50%;">
        </div>
        <div class="message">{{MSG}}</div>
    </div>
"""
