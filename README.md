# kurssim.me lambda scraper

The Opintoni/Weboodi scraper turned into AWS Lambda function with Serverless.

# How to run locally

You should already have Python 3.6 installed.

If you want to deploy this to your own AWS environment then you should also install `aws-cli` and then create a local profile with full admin rights (hihi) and a S3 bucket.

Also you need Docker if you want to deploy to AWS. Yeah...

## TODO this maybe works

1) Install Node.js version >=8 using nvm
2) Download this repo and enter `npm i`
3) Install serverless globally: `npm i -g serverless`
4) Install virtualenv if you don't have it already: `pip3 install virtualenv` (or just pip if you don't have Python2 locally)
4) Generate virtual environment: `virtualenv venv`
5) Activate virtual environment: `source venv/bin/activate`
6) Before invoking the lambda if you want to upload the file to S3 you need to have AWS account locally with permissions to a bucket
7) Then you should invoke the Lambda locally: `export AWS_PROFILE=<your-profile> && sls invoke local --function crawl --stage local --uploadBucket <your-bucket>` where you should replace the profile and bucket with your values.
8) If you don't want to upload to S3 you can use: `sls invoke local --function crawl --stage local`

# Additional information

You should comment: `- schedule: rate(24 hours)` from the `serverless.yml` unless you want to wait 24 hours between your CloudWatch events. Instead you should comment out the block on top of it so you can try invoke the crawler just by visiting your API endpoint (it's displayed on your console after deploying).

# TODO

Disable Scrapy logging. Seriously annoying to read million rows in CloudWatch Logs.

Enable local development. Lol.

Maybe add to CI pipeline eg. Travis. Or not. Admin rights is tricky business.



