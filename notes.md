
# Outputs

BucketArnVPCFlowLogs	arn:aws:s3:::cand-c3-vpc-flow-logs-787614237147
BucketNameRecipesFree	cand-c3-free-recipes-787614237147
BucketNameRecipesSecret	cand-c3-secret-recipes-787614237147

ApplicationInstanceIP	ec2-3-224-223-36.compute-1.amazonaws.com
ApplicationURL	c1-web-service-alb-143963776.us-east-1.elb.amazonaws.com
AttackInstanceIP	ec2-52-202-180-62.compute-1.amazonaws.com

# Upload data

aws s3 cp free_recipe.txt s3://cand-c3-free-recipes-787614237147/ --region us-east-1

aws s3 cp secret_recipe.txt s3://cand-c3-secret-recipes-787614237147/ --region us-east-1

# Test app

http://c1-web-service-alb-143963776.us-east-1.elb.amazonaws.com/free_recipe