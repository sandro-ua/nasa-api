## TEST PROJECT

API to be tested: 
https://api.nasa.gov/
https://epic.gsfc.nasa.gov/

## Tools used in the project
Python, Pytest, Jenkins, GIT, GitHub, GitHub Actions, DSL

## Known issues
#1 Its not possible to add option "Use commit author in changelog" in DSL for pipeline NASA_REGRESSION_DSL_GENERATED. Without this option pipeline can't pull the code with error: 
ERROR: Checkout failed
stderr: Committer identity unknown

Workaround: (1 option) remove option "Create a tag for every build" in pipeline configuration. (2 option) move the pipeline script into DSL file itself.

## Query example
https://api.nasa.gov/EPIC/api/natural/date/2019-05-30?api_key=DEMO_KEY

## NASA EPIC documentation link 
documentation https://epic.gsfc.nasa.gov/about/api