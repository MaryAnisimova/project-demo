# project-demo
Building application with Python code and Terraform cluster creation

1. To create EKS cluster - used Terraform for automation and reusable reason. EKS cluster creation includes : - eks.tf - includes configuration specifiacly for EKS creation;
           - vpc.tf - created new VPC with CIDR block;
           - subnets.tf - creats subnets - 2 public and 2 private;
           - route.tf - creates route tables - private and association of this route tables with subnets;
           - gateway.tf - creates internet gateway for cluster;
           - nat.tf - creats nat-gateway for cluster;
           - iam-test.tf - creates iam role, iam policy, attacing role to the policy,  
           - iam-oids.tf - creates iam open id connect provider and also used data for tls_certification;
           - iam-autoscaler.tf - creates iam policy


2. To run Terraform code : 
     - make sure you are logged in to the correct AWS account - aws sts get-caller-identity - 
     - export your credentials if needed - export AWS_PROFILE= "profile_name"
     - use command  -terraform init-  - initializes a working directory containing Terraform configuration files;
     - use command -terraform plan-  - to see what is creating or what is changing from this code;
     - use command -terraform apply- - to apply code and create resources that are planned.
     Creation AWS EKS cluster with all attached resources may take around 30 min. 
     You are allowed to change code as many times as you need, create module, use datasurce to pull data about AWS resource from your AWS, such as - VPC, nat-gateway or any other resources.

3. After creating AWS EKS cluster :
Application code needs to be created. Using Python programing language to show a simle message on web server. The message suppose to show today's date and time. 
to run Python script use command:
  -FLASK_APP=python2.py flask run- 
  after running this command, there will be url link available on the scrin - copy and past in broweser. 
  The simple message suppose to come up on the sceen with hunam readable time and data. 



