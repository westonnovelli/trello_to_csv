__author__ = 'westonnovelli'

import requests
import json
import csv

"""
This script will grab some data from trello and save it as a csv file. 

This script is set up to grab card data from a given board from only the open cards.
You can of course edit the request to get other information. For details visit
trello's api docs site at "https://trello.com/docs/api"

To get started, enter values for the following variables and run
python trello_to_csv.py

Enjoy! I welcome feedback.
"""
board_id = "" # get the board id from the list of your boards at ""
key = "" # get your key from ""
csv_filename = "" + ".csv" # the filename of the output csv file
card_fields = ["name"] # add all of the card fields you want here
###--------------------------------------------------------------###

card_fields_str = ""
for field in card_fields:
    card_fields_str += "&card_fields=" + field

response = requests.get("https://api.trello.com/1/boards/"+board_id+"?key="+key+"&cards=open" + card_fields_str[:-1])

as_json = json.loads(response.text)

file_output = csv.writer(open(csv_filename, "wb+"))

cards_fields = ["id"] + card_fields
file_output.writerow(cards_fields) # headers

for card in as_json['cards']:
    card_data = [card['id'].encode('UTF-8')]
    for field in card_fields:
        card_data.append(card[field].encode('UTF-8')])
    file_output.writerow(card_data)
