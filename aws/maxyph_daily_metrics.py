import boto3
from boto3.dynamodb.conditions import Key
import datetime as dt
import itertools
import json

#globals
DATETIME_FORMAT = "%Y-%m-%d"
today = dt.datetime.now().strftime(DATETIME_FORMAT)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('maxyph_daily_metrics')

def get_daily_metric(puzzle: list) -> dict:
    score = len(set(itertools.chain.from_iterable(puzzle)))
    response = table.query(ScanIndexForward=False, Limit=1, KeyConditionExpression=Key('partition').eq(0))
    if response['Items'] != []:
        if response['Items'][0]['date'] == today:
            if score > response['Items'][0]['score']:
                update_new_score(puzzle, response['Items'][0]['submissions'] + 1, score)
            else:
                # score was worse or equal, only incrememnt count
                update_new_count(response['Items'][0]['submissions'] + 1, )
            
        else:
            # last date not today, write new row
            write_new_row(puzzle, score)
    else:
        # empty response returned, write new row
        write_new_row(puzzle, score)
            
def update_new_score(puzzle: list, count: int, score: int) -> None:
    response = table.update_item(
        Key={
            'partition' : 0,
            'date' : today,
        },
        UpdateExpression='SET words = :words, submissions = :submissions, score = :score',
        ExpressionAttributeValues={
            ':words': puzzle,
            ':submissions': count,
            ':score' : score
                    })

def update_new_count(count: int) -> None:
    response = table.update_item(
        Key={
            'partition' : 0,
            'date' : today,
        },
        UpdateExpression='SET submissions = :submissions',
        ExpressionAttributeValues={
            ':submissions': count
                    })

def write_new_row(puzzle: list, score: int) -> None:
    response = table.put_item(Item={
        'partition' : 0,
        'date' : today,
        'puzzle' : puzzle,
        'score' : score,
        'submissions' : 1
    }
        )



def lambda_handler(event, context):
    get_daily_metric(event['puzzle'])
    response = table.query(ScanIndexForward=False, Limit=1, KeyConditionExpression=Key('partition').eq(0))
    score = int(response['Items'][0]['score'])
    date = (response['Items'][0]['date'])
    submissions = response['Items'][0]['submissions']
    return {
        'statusCode': 200,
        'high_score': score,
        'date' : date,
        'submissions' : submissions
    }

