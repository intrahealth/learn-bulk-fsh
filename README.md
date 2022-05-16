# Learn how to generate bulk FHIR data with FSH

This is a simple repo to show how to template and generate FSH files.

## How to use

* Create a folder at `input/examples-src/output`.
* Edit, and run the Jupyter Notebook `bulk-process.py`. 
* The Patient resources are generated from the CSV rows (minus the header) in `input/examples-src/batteries.csv`.
* The output is in the output folder. After they are generated they can be moved into `input/fsh` or into a subfolder there to be used with `sushi`.