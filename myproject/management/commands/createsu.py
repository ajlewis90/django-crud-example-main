print("Inside createsu.py")
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

print("What's happening")


class Command(BaseCommand):

	def handle(self, *args, **options):
		print("Did it even get here?")
		# Check if a user record with the username 'awsadmin' exists in the database
		# If it does not exist, then create a super-user with that username,
		# Supply an email address and a password to it
		# So, now we have an admin user to manage our AWS RDS database
		if not User.objects.filter(username="awsadmin").exists()
			print("Whats happening here- IS IT EVEN EHRE??")
			User.objects.create_superuser("awsadmin", "arthur.lewis420@gmail.com", "AWSAdmin123")