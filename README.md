## TEST PROJECT

API to be tested: 
https://api.nasa.gov/
https://epic.gsfc.nasa.gov/

## Tools used in the project
Python, Pytest, Jenkins, GIT, GitHub, DSL

## Known issues
#1 Its not possible to add option "Use commit author in changelog" in DSL for pipeline NASA_REGRESSION_DSL_GENERATED. Without this option pipeline can't pull the code with error: 
ERROR: Checkout failed
stderr: Committer identity unknown

Workaround: add option manually or move the pipeline script into DSL file itself.