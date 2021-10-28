from user.models import User
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
	def authenticate(self, username=None, password=None):
		
		print(username)
		try:
			user = User.objects.get(email=username)

		except User.DoesNotExist:
			return None
		else:
			if user.check_password(password):
				return user
			return None
