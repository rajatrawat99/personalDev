#!/bin/bash
aws cloudformation create-stack \
--stack-name $1 \
--template-body file://$2 \
--parameters file://$3 \
--region=us-west-2 \


aws cloudformation update-stack --stack-name ourdemoinfra --template-body file://cldfn.yml --parameters file://ourInfra-params.json --region=us-west-2