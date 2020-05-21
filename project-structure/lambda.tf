resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_lambda_function" "test_lambda" {
  filename      = "function.zip"
  function_name = "owl_request_validator"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "src.main.python.com.johnowl.hello.service.hello_service.lambda_handler.lambda_handler"
  source_code_hash = filebase64sha256("function.zip")
  runtime = "python3.8"
}