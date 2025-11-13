IAM Text info in Json format







{

&nbsp;   "Version": "2012-10-17",               ---> Indicates the version of the aws upto date

&nbsp;   "Statement": \[

&nbsp;       {

&nbsp;           "Sid": "VisualEditor0",        ---> Mentions ID of IAM

&nbsp;           "Effect": "Allow",             ---> Allows all the resources 

&nbsp;           "Action": \[

&nbsp;               "iam:GetUserPolicy",

&nbsp;               "iam:ListUsers",

&nbsp;               "iam:ListUserPolicies",

&nbsp;               "iam:GetUser"

&nbsp;           ],

&nbsp;           "Resource": "\*" ---> Indicates from all the resources in AWS can access users info similar to \* in "SQL"

&nbsp;       }

&nbsp;   ]

}







Administrator Access to all resources in AWS.





{

&nbsp;   "Version": "2012-10-17",

&nbsp;   "Statement": \[

&nbsp;       {

&nbsp;           "Effect": "Allow",

&nbsp;           "Action": "\*",

&nbsp;           "Resource": "\*"

&nbsp;       }

&nbsp;   ]

}







EC2 INSTANCE



When we stop the EC2 instance and then start the instance the Public IP will change and the Private Ip will remain same so once stopped and started need to check the IP opened in a new tab. 



Whenever we are working with EC2 instance in a terminal never ever share the Access key and Access Key id in the terminal directly there is a chance to misuse them so instead use IAMreadonly policy access in security the we get the IAM user details in the EC2 instance directly using the command "aws iam list-users".



If we need to work on SSH in terminal we can use connect to EC2 instance in AWS it will directly open the terminal and connect to the SSH through AWS.





Info about the load balance

-> Initially there is one pod with some users when the users increases we need to depoly the more pods. so, these can be done by load balancer when the

   users increased to access app then the load balancer deploys more pods.

-> Real-world scenario, At the time of Big-Billon-Days the active users for amazon and filpkart will be huge and there are n number of users can access so

   they can deploy more pods and increases the count of pods for access this can be done using the load balancer once the sale is ended the users decreases

   and the pods will scale out automatically using load balancers.



























AWS LAMBDA

-----------





























AWS BEANSTALK

-------------



response🌱 What is AWS Elastic Beanstalk?



AWS Elastic Beanstalk is a Platform-as-a-Service (PaaS) offering from Amazon Web Services that allows you to deploy and manage applications in the cloud without worrying about the infrastructure (like servers, load balancers, scaling, etc.).



* Simplifies deployment: Just upload your code, and Beanstalk handles the rest.
* Auto-scaling: Automatically adjusts capacity based on traffic.
* Monitoring: Integrated with CloudWatch for health and performance metrics.
* Customizable: You can still access the underlying resources (EC2, RDS, etc.) if needed.











