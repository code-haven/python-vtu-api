# vtu-results-scaper
A python script to scrape results.vtu.ac.in to retrieve results in a developer friendly format.

# Usage:
1) Install the dependencies: 
>>pip install -r requirements.txt

2) Run the script by providing a usn as an argument. 
>>python vtuscraping.py \<\<USN\>\>

Output format:
<pre>
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
</pre>

# Bugs
1) Right now, it can accurately parse only regular results(without backlogs).

# Todo
1) Seperate subject name and subject code into seperate fields for each subject.
2) Refactor code for reusability, maybe a function that returns the result as JSON. 

# Licence 
MIT. Do whatever you want with it.
