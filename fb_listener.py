from fbchat import Client
from fbchat.models import *

from gtts import gTTS
import subprocess

from ghome_methods import *


allowedUIDS = ['100002275640165']


class ghomeBot(Client) :
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)

        if author_id == self.uid :
            return

        if author_id not in allowedUIDS :
            self.send(Message(text='You are not authorised.'), thread_id=thread_id, thread_type=thread_type)
            return
        cmd = message_object.text

        processCommand(cmd)

        self.send(Message(text='Done'), thread_id=thread_id, thread_type=thread_type)
