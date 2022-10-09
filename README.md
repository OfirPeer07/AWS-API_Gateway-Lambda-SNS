# AWS Services: API Gateway ==> Lambda ==> SNS

Here you can find examples of Lambda function usage and a full tutorial explaining how to use AWS API Gateway and SNS (Simple Notification Service) to send an email with the response from the Lambda source code.

![This is image](https://user-images.githubusercontent.com/6509926/52906603-cbb6cb80-3214-11e9-8a97-a5ea2d4036d3.png)

### **A little about "Lambda"**
Lambda is a compute service that lets you run code without provisioning or managing servers, with Lambda, you can run code for virtually any type of application or backend service.  
Lambda runs your function only when needed and scales automatically, from a few requests per day to thousands per second.  
Lambda functions allows us to use the Lambda API, or Lambda can run your functions in response to events from other AWS services.

![This is image](https://i.ibb.co/dGwtcFZ/tumblr-p3ixzlxw-W81s74q07o1-1280.jpg)

- Go to Lambda ==> Functions ==> Click on "Create function".  

On this step we will create a "Lambda function", first you have to choose a name (for example: Calc2Parameters), then we choose a language in "Runtime" (I am using Python 3.8).  
You can leave all the other options at default and click on "Create function".

![This is image](https://serving.photos.photobox.com/05385919cf27e171943e54baac41e3a00aec6887eb8833f1e5ae6755eed7f781c9269e9b.jpg)

- Go to SNS ==> Topics ==> Click on "Create topic".

On this step we will create a "SNS topic", first you have to choose "Standard" in "Topic type", then we choose a name (my topic is called "Calc2Parameters").  
It is not mandatory to fill in "Display name" and all options can be left on default mode and click on "Create topic".  

![This is image](https://i.postimg.cc/s25KJTJQ/Create-Topic-SNS.jpg)

After we created a topic, we have to go to "Subscriptions" and click on "Create subscription".  
Then select your "Topic ARN".  
In "Protocol" select the "Email" option and in "Endpoint" fill your email.  
You can leave all the other options at default and click on "Create subscription".

![This is image](https://i.postimg.cc/s3w0f2x7/ARNtopic.jpg)

We will return to "Subscriptions", where you can see in the "Status" tab that our email is awaiting confirmation.  
In order to confirm the email, we will enter the email, where we will find an email with a link to confirm and verify the selected email.

![This is image](https://i.postimg.cc/g2xYSTr0/Subscription.jpg)

- Go to IAM ==> Roles ==> Click on "Create role".    
In "Trusted entity type" select "AWS service".   
In "Use case" select "Lambda" and click "Next".

![This is image](https://i.postimg.cc/JhpJjh6F/IAMRole1.jpg)

In "Permissions policies" we will search "AmazonSNSFullAccess", we will mark it and click on "Next".

![This is image](https://i.postimg.cc/s2VztYPM/IAMRole2.jpg)

In "Role name" select a name (my role is called "Calc2Parameters"), then click on "Create role".

![This is image](https://i.postimg.cc/T2Qt9r1k/IAMRole3.jpg)

- Go to API Gateway ==> APIs ==> Click on "Create API".  
In "API type" select "REST API" (no Private) and click on "Build".  

![This is image](https://i.postimg.cc/DzjNDbPh/API1.jpg)

Select "REST" to choose the protocol, and "New API" to create a new API, then give a name to your API.  
It is not mandatory to fill in a "Description".  
In "Endpoint Type" select "Regional", when done, click on "Create API".

![This is image](https://i.postimg.cc/HxrNCs6y/API2.jpg)

After we created an API, We click on "Actions" to "Create Resource", then we choose a name (my resource is called "calc2parameters") and click on "Create Resource".

![This is image](https://i.postimg.cc/85x0kQYn/API3.jpg)

Next step is to create Method (POST) - Click on "Actions" to "Create Method", select "Lambda Function" in "Integration type", mark the "Proxy integration", choose your "Lambda Function", when done, click on "Save".

![This is image](https://i.postimg.cc/mkM6tpfZ/API4.jpg)

Click "OK" to give API Gateway permission to invoke your Lambda function.

![This is image](https://i.postimg.cc/RVJvTv9q/API5.jpg)

Click on "Actions" then "Deploy API".  
In "Deployment stage" select "New Stage", choose a "Stage name" (my stage is called "Clac2Parameters_Test").  
It is not mandatory to fill in a "Stage/Deployment description", click on "Deploy" to create a stage.

![This is image](https://i.postimg.cc/RhVN0ynK/API6.jpg)

![This is image](https://images.squarespace-cdn.com/content/v1/61f2d23be98e94537d76e95d/9aa6bb3c-66b5-48ae-af4c-72147f86ea36/sofarsogood_website_Logo_white1.png)

After completing all the steps so far, we will check that the "API Gateway" and "SNS" (Simple Notification Service) services are connected as in the example image.

![This is image](https://i.postimg.cc/nhRsXQjs/Calc2-Parameters.jpg)

In order to connect the SNS to the Lambda function, we must click on "Add destination".  
In "Source" select "Asynchronous invocation".  
In "Condition" select "On failure".  
In "Destination type" select "SNS topic".  
In "Destination" select the name of the topic we created.

![This is iamge](https://i.ibb.co/KjjF5MK/SNSdestination.jpg)
