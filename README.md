# vtu-results-scaper
A python script to scrape results.vtu.ac.in to retrieve results in a developer friendly(JSON) format.

# Usage:
1) Install the dependencies: pip install -r requirements.txt
2) python vtuscraping.py <USN>

Output format:

{
	name: "..",
	semester: "..",
	usn: "...",
	total: "...",
	result: "...",
	marksheet: [
		{
			subject: "..",
			internal: "..",
			external: "..",
			total: "..",
			result: "..:,
		},
		{
			subject: "..",
			internal: "..",
			external: "..",
			total: "..",
			result: "..:,
		},
		..
	]
}

# Bugs
1) Currently it can accurately parse regular results(without backlogs).

# Todo
1) Seperate subject name and subject code into seperate fields for each subject.

# Licence 
MIT. Do whatever you want with it.