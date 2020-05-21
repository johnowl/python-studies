terraform {
  backend "s3" {
    bucket = "owl-request-validator"
    key    = "terraform/lambdas/"
    region = "us-east-1"
  }
}