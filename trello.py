import requests
import json

class Trello:
    def __init__(self, api_key, api_token, username):
        self.key = api_key
        self.token = api_token
        self.querystring = {"key": self.key, "token": self.token}
        self.username = username

    def get_board_id(self, board_name):
        url = "https://api.trello.com/1/members/{0}/boards".format(self.username)
        response = requests.request("GET", url, params=self.querystring)
        boards = json.loads(response.text)
        board_id = 0
        for board in boards:
            if board["name"] == board_name:
                board_id = board["id"]
        if board_id == 0:
            board_id = self.create_board(board_name)
        return board_id

    def create_board(self, board_name):
        url = "https://api.trello.com/1/boards/"
        querystring = {"name": board_name, "key": self.key, "token": self.token}
        response = requests.request("POST", url, params=querystring)
        board_id = response.json()["shortUrl"].split("/")[-1].strip()
        return board_id

    def get_list_id(self, list_name):
        url = "https://api.trello.com/1/boards/{0}/lists".format(self.board_id)
        response = requests.request("GET", url, params=self.querystring)
        lists = json.loads(response.text)
        list_id = 0
        for list_ in lists:
            if list_["name"] == list_name:
                list_id = list_["id"]
        if list_id == 0:
            list_id = self.create_list(list_name)
        return list_id

    def create_list(self, list_name):
        url = "https://api.trello.com/1/boards/{0}/lists".format(self.board_id)
        querystring = {"name": list_name, "key": self.key, "token": self.token}
        response = requests.request("POST", url, params=querystring)
        list_id = response.json()["id"]
        return list_id

    def get_labels_id(self, labels):
        url = "https://api.trello.com/1/boards/{0}/labels".format(self.board_id)
        response = requests.request("GET", url, params=self.querystring)
        all_labels = json.loads(response.text)
        self.labels_id = []
        name_labels = []
        for i in all_labels:
            if i["name"] in labels:
                name_labels.append(i['name'])
                self.labels_id.append(i['id'])
        self.new_labels = list(set(labels) - set(name_labels))
        if len(self.new_labels) > 0:
            self.create_labels()
        return self.labels_id
    
    def create_labels(self):
        for label in self.new_labels:
            url = "https://api.trello.com/1/boards/{0}/labels".format(self.board_id)
            querystring = {"key": self.key, "token": self.token, "name": str(label)}
            response = requests.request("POST", url, params=querystring)
            self.labels_id.append(response.json()["id"])

    def create_card(self, board, list_name, cardname, labels):
        self.board_id = self.get_board_id(board)
        self.list_id = self.get_list_id(list_name)
        self.labels_id = self.get_labels_id(labels)
        url = "https://api.trello.com/1/cards"
        querystring = {"key": self.key,
                       "token": self.token,
                       "name": cardname,
                       "idList": str(self.list_id),
                       "idLabels": self.labels_id
                    }
        response = requests.request("POST", url, params=querystring)
        self.card_id = response.json()["id"]
        return self.card_id

    def create_comment(self, comment):
        url = "https://api.trello.com/1/cards/{0}/actions/comments".format(self.card_id)
        querystring = {
            "key": self.key,
            "token": self.token,
            "text": comment
        }
        response = requests.request("POST", url, params=querystring)