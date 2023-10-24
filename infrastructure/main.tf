provider "aws" {
  region = "us-east-1"
}

/*
    Lambda function configuration
*/
data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "iam_for_xbot" {
  name               = "iam_for_xbot"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

resource "aws_lambda_function" "x_bot" {
  description   = "A lambd function which executes a bot to generate a tweet on X"
  function_name = "x_bot"
  role          = aws_iam_role.iam_for_xbot.arn
  architectures = ["arm64"]
  package_type  = "Image"
  image_uri     = var.image_uri
  timeout       = 180
}

resource "aws_lambda_permission" "allow_eventbridge_to_trigger_function" {
  statement_id  = "AllowExecutionFromEventbridge"
  function_name = aws_lambda_function.x_bot.function_name
  action        = "lambda:InvokeFunction"
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.x_bot_lambda_event_rule.arn
}

/*
    Eventbridge configuration
*/

resource "aws_cloudwatch_event_rule" "x_bot_lambda_event_rule" {
  description         = "An eventbridge rule used to trigger a lambda function every 2 hours"
  schedule_expression = "rate(2 hours)"
}

resource "aws_cloudwatch_event_target" "lambda_func" {
  rule = aws_cloudwatch_event_rule.x_bot_lambda_event_rule.name
  arn  = aws_lambda_function.x_bot.arn
}
