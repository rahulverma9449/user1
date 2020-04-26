import boto3
ec2 = boto3.resource('ec2')
def lambda_handler(event, context): 
    filter = [
       {
           
 	    'Name': 'tag:Name',
 	    'Values':['amazon-ec2']
 	}
	]
   instances = ec2.instances.filter(Filters=filter)
   for instance in instances:
       instance.stop()
   return 'Check your EC2 instance'
		