import datetime as dt
import boto3
from boto3.dynamodb.conditions import Key
import itertools
import json
import os
import random
import string

# globals
TEXT_FILE = os.environ['LAMBDA_TASK_ROOT'] + "/guesswords.txt"
DATETIME_FORMAT = "%Y-%m-%d"


with open(TEXT_FILE, 'r') as guesswords:
    guess_words = [line.rstrip() for line in guesswords]
    
def generate_puzzle() -> list:
    puzzle_state = []
    for i in range(6):
        if i == 0:
            while puzzle_state == []:
                seed_letter = random.choice(string.ascii_uppercase)
                seed_placement = random.choice(range(5))
                valid_count = 0
                for word in guess_words:
                    if word[seed_placement] == seed_letter.lower():
                        valid_count += 1
                    if valid_count > 4:
                        puzzle_state.append([seed_placement, seed_letter])
                        break
                else:
                    # puzzle generation failed to find 5 valid words for the first row
                    # trying again
                    pass
        else:
            valid_placements = list(range(5))
            valid_placements.remove(puzzle_state[i-1][0])
            seed_placement = random.choice(valid_placements)
            puzzle_state.append([seed_placement, ''])
    return puzzle_state

def jsonify_puzzle_for_john() -> dict:
    now = dt.datetime.now()
    puzzle_vals = {}
    puzzle = generate_puzzle()
    puzzle_vals['date'] = now.strftime(DATETIME_FORMAT)
    puzzle_vals['puzzle'] = puzzle
    return puzzle_vals

def get_puzzle_id(table) -> int:
    response = table.query(ScanIndexForward=False, Limit=1, KeyConditionExpression=Key('partition').eq(0))
    return response['Items'][0]['id'] + 1
    
    
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('maxyph_puzzles')
    # dynamodb = boto3.resource('dynamodb')
    # table = dynamodb.Table('maxyph_puzzles')
    # response = table.get_item(Key={'id' : 0 })
    # response = table.put_item(Item={'id': 0, 'puzzle': [[0, "R"]]})
    id = get_puzzle_id(table)
    puzzle = jsonify_puzzle_for_john()
    response = table.put_item(Item={'partition': 0, 'id': id, 'puzzle': puzzle['puzzle'], 'date' : puzzle['date']})
    return response


