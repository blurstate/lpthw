formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight.",
	)
# made the mistake of not putting commas in after each of the poem lines.
# it failed to print properly. it gave a TypeError of 'not enough arguments for format string'
