# Make sure to install flask!
# I did this with the following command:
# python3 -m pip install flask 

# Run with the following command:
# flask --app message_board run

from flask import Flask
from flask import render_template
from flask import request
from message import Message



message_dict = {}  # data structure to store all messages

app = Flask(__name__)  # create a new instance of Flask


# This application supports a single URL -- /messages
@app.route('/messages/')
def messages():
    # retrieve the message parameter (if present)
    message = request.args.get('message')
    author = request.args.get('author')


    # if there was a message
    if message and len(message) > 0:
        # create a new message Object
        new_message_info = Message(message, author)
        # add the message to the list
        if new_message_info.author in message_dict:
            message_dict[new_message_info.author].append(new_message_info.message)
        else:
            message_dict[new_message_info.author] = [new_message_info.message]
    # render using the message_board template in the templates directory
    return render_template('message_board.html', items=message_dict)


# style learned from https://www.w3schools.com/css/css_padding.asp
