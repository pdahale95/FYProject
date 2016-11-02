class CodeforcesProblem:
	'Class for representing problems'

	def __init__(self, problemId, name, url, tags, problemStatement, timelimit, memorylimit):
		self.id = id
		self.problemId = problemId
		self.name = name
		self.url = url
		self.tags = tags
		self.problemStatement = problemStatement
		self.timelimit = timelimit
		self.memorylimit = memorylimit
		self.desription = problemStatement
		self.process_description()

	def __str__(self):
		return "Problem name: " + self.name + " Problem tag: " + self.tags + " Problem url: "+self.url

	def process_description(self):
		description_lines = self.desription.split('\n')
		print(description_lines)
		description_lines = [line.strip() for line in description_lines]

		try:
			input_start = description_lines.index('Input')
		except ValueError:
			try:
				input_start = description_lines.index('Input :')
			except ValueError:
				input_start = description_lines.index('Input:')


		try:
			output_start = description_lines.index('Output')
		except ValueError:
			try:
				output_start = description_lines.index('Output :')
			except ValueError:
				output_start = description_lines.index('Output:')

		try:
			example_start = description_lines.index('Examples')
		except ValueError:
			try:
				example_start = description_lines.index('Examples :')
			except ValueError:
				example_start = description_lines.index('Examples:')

		self.statement = description_lines[:input_start]
		self.input = description_lines[input_start:output_start]
		self.output = description_lines[output_start:example_start]
		self.constraints = self.input
		print self.input
		print self.output


	