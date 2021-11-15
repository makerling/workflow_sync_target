
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project uses Github Actions to create sync a folder of files from one repository to the target repository triggered by a pull request. Once files have been synced, the pipeline commits any updated files to the repository. 
	
## Technologies
Project is created with:
* bash: 
* Python: 3.8.1
* Dirsync (python library): 2.2.5 
* Ubuntu runner (Github Actions): 20.04
	
## Setup
To run this project, submit a pull request and the pipeline will be triggered. Alternatively the pipeline can be manually triggered through a workflow-dispatch in the UI. 
