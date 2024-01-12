AWS Services Model

**maxyph_generate_puzzle**
- guesswords.txt
- lambda_function.py

This is a function scheduled via AWS Eventbridge to run at midnight mountain time daily to push a new puzzle to a dynamodb table containing the days puzzle.
Components used:
- AWS Eventbridge
- AWS Dynamodb
- AWS Lambda

**maxyph_get_puzzle**
- lambda_function.py

This is a function called via AWS API Gateway unauthenticated to retrieve the puzzle input for the day.
https://u2qy92og0i.execute-api.us-west-2.amazonaws.com/puzzle

Components used:
- AWS API Gateway
- AWS Lambda

