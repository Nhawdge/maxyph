import boto3
from boto3.dynamodb.conditions import Key
import json

def get_puzzle() -> dict:
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('maxyph_puzzles')
    response = table.query(ScanIndexForward=False, Limit=1, KeyConditionExpression=Key('partition').eq(0))
    puzzle = {}
    formatted_puzzle = [[int(x[0]), x[1]] for x in response['Items'][0]['puzzle']]
    puzzle['puzzle'] = formatted_puzzle
    puzzle['date'] = response['Items'][0]['date']
    return puzzle

def lambda_handler(event, context):
    puzzle = get_puzzle()
    return {
        'statusCode': 200,
        'body': json.dumps(puzzle)
    }
