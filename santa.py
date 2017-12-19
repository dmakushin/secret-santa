#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText
import argparse
import os
import json
import random

parser = argparse.ArgumentParser(
    description='make e-mail list')

parser.add_argument("--u", required=True, help='e-mail account')
parser.add_argument("--p", required=True, help='e-mail password')
parser.add_argument("--s", required=True, help='e-mail server')

args = parser.parse_args()


class OfficeBoy(object):

    def __init__(self, username, password, server):
        self.username = username
        self.password = password
        self.server_address = server
        self.recipients = list()
        self.msg_text = 'Prepare your gift for '
        self.server = smtplib.SMTP(self.server_address)
        self.server.starttls()
        self.server.login(self.username, self.password)
        self.msg = None

    def __add_recipient(self, recipient):
        self.recipients.append(recipient)

    def add_recipients(self):
        source_dir = os.getenv("PWD", os.getcwd())
        path = os.path.join(source_dir, "santas_list.json")
        with open(path, 'rb') as gift_list:
            json_list = json.load(gift_list)
            recipients_list = json_list["email"]
            for r in recipients_list:
                self.__add_recipient(r)

    def send_email(self, kid):
        msg_text = self.msg_text + kid.get_next().email
        self.msg = MIMEText(msg_text)
        self.msg['From'] = 'Santa Claus'
        self.msg['To'] = kid.email
        self.msg['Subject'] = 'Santas Anonymous'
        self.server.sendmail(self.username, kid.email, self.msg.as_string())

    def terminate(self):
        self.server.quit()


class Player(object):

    def __init__(self, email):
        self.email = email
        self.gifted = None

    def set_next(self, gifted):
        self.gifted = gifted

    def get_next(self):
        return self.gifted


class Shuffle(object):

    def __init__(self, emails):
        self.players = list()
        for email in emails:
            player = Player(email)
            self.players.append(player)

    def get_gifted_players(self):
        random.shuffle(self.players)
        for i in range(0, len(self.players) - 1):
            self.players[i].set_next(self.players[i + 1])
        self.players[-1].set_next(self.players[0])
        return self.players


if __name__ == '__main__':
    try:
        santa = OfficeBoy(args.u, args.p, args.s)
        santa.add_recipients()
        shuffle = Shuffle(santa.recipients)
        players = shuffle.get_gifted_players()
        with open("roles_backup.txt", 'w+') as f:
            for player in players:
                santa.send_email(player)
                f.write(player.email + '-->' + player.get_next().email + '\n')
    finally:
        santa.terminate()
        f.close()
