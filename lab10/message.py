class Message:
	"""
	Class representing a single message.
	"""

	def __init__(self, message, author):
		self.message = message
		if author:
			self.author = author
		else:
			self.author = 'No Author'
