# python-vtu-api
A python package that scrapes results.vtu.ac.in to retrieve results in a developer friendly format.

# Usage:
1) Clone the repo

2) cd python-vtu-api/

3) Install python dependencies:

```
pip install -r requirements.txt
```

4) Use the get_results function to retrieve the results for a given usn.

```
from vtu import results

results.get_results(usn=xxx)
```

Output format:

```
{
	name: "..",
	usn: "...",
	total: "...",
	result: "...",
	marksheet: [
		{
			subject: "..",
			internal: "..",
			external: "..",
		    semester: "..",
			total: "..",
			result: "..:,
		},
		{
			subject: "..",
			internal: "..",
            semester: "..",
			external: "..",
			total: "..",
			result: "..:,
		},
		..
	]
}
```

# Todo
- [ ] Add support for revaluation results and backlogs.

- [x]  Refactor code for reusability, maybe a function that returns the result as JSON.

# License
MIT. Do whatever you want with it.
