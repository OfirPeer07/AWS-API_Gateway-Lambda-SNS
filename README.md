# AWS-API_Gateway-Lambda-SNS

Here you can find examples of Lambda function usage and a full tutorial explaining how to use AWS API Gateway and SNS (Simple Notification Service) to send an email with the response from the Lambda source code.

![This is image](https://user-images.githubusercontent.com/6509926/52906603-cbb6cb80-3214-11e9-8a97-a5ea2d4036d3.png)

### **A little about "Lambda"**
Lambda is a compute service that lets you run code without provisioning or managing servers, with Lambda, you can run code for virtually any type of application or backend service.  
Lambda runs your function only when needed and scales automatically, from a few requests per day to thousands per second.  
Lambda functions allows us to using the Lambda API, or Lambda can run your functions in response to events from other AWS services.

![This is image](https://i.ibb.co/dGwtcFZ/tumblr-p3ixzlxw-W81s74q07o1-1280.jpg)

- Go to Lambda ==> Functions ==> Click on "Create function".  

On this page we will create a "Lambda function", first you have to choose a name (for example: Calc2Parameters), then we choose a language in "Runtime" (I am using Python 3.8).  
You can leave all the other options at default and click on "Create function".

![This is image](https://serving.photos.photobox.com/05385919cf27e171943e54baac41e3a00aec6887eb8833f1e5ae6755eed7f781c9269e9b.jpg)

- Go to SNS ==> Topics ==> Click on "Create topic".

On this page we will create a "SNS topic", first you have to choose "Standard" in "Topic type", then we choose a name (my topic called "Calc2Parameters").  
It is not mandatory to fill in "Display name" and all options can be left on default mode and click on "Cearte topic".  

![This is image](https://i.postimg.cc/s25KJTJQ/Create-Topic-SNS.jpg)

After we created a topic, we have to go to "Subscriptions" and click on "Create subscription".  
Then select your "Topic ARN".  
In "Protocol" select the "Email" option and in "Endpoint" fill your email.  
You can leave all the other options at default and click on "Create subscription".

![This is image](https://i.postimg.cc/s3w0f2x7/ARNtopic.jpg)

We will return to "Subscribers", where you can see in the "Status" tab that our email is awaiting confirmation.  
In order to confirm the email, we will enter the e-mail, where we will find an e-mail with a link to confirm and verify the selected email.

![This is image](https://i.postimg.cc/g2xYSTr0/Subscription.jpg)
