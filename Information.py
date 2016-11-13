class Information(object):
	def __init__(self, url, username, pwd, notes):
		self.url = url
		self.username = username
		self.pwd = pwd
		self.notes = notes

	def __str__(self):
		return self.__dict__

	def __hash__(self):
		#override default hash
		prime = 31
		result = 1
		result = prime * result + (hash(self.url) if self.url != None else 0)
		result = prime * result + (hash(self.username) if self.username != None else 0)
		result = prime * result + (hash(self.pwd) if self.pwd != None else 0)
		result = prime * result + (hash(self.notes) if self.notes != None else 0)
		return result

	def __eq__(self, other):
		#override default equality
		#defined like the Java behavior
		if not isinstance(other, self.__class__):
			return False
		if other is None:
			return False
		if other is self:
			return True

		if self.url != other.url:
			return False
		if self.username != other.username:
			return False
		if self.pwd != other.pwd:
			return False
		if self.notes != other.notes:
			return False
		return True

	def __ne__(self, other):
		return not self.__eq__(other)