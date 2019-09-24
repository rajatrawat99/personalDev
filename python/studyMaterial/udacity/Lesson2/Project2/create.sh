#!/bin/bash
aws cloudformation create-stack \
--stack-name $1 \
--template-body file://$2 \
--parameters file://$3 \
--region=us-west-2 \

aws cloudformation create-stack --stack-name project2Udacity --template-body file://project2Udacity.yml --parameters file://project2Udacity.json --region=us-west-2
aws cloudformation update-stack --stack-name project2Udacity --template-body file://project2Udacity.yml --parameters file://project2Udacity.json --region=us-west-2