# CASE STUDY 1

### Description
We want you to implement a REST API that, given a movie or series title, returns the results available in the OMDb API, which is a RESTful web service to obtain that information.
We will positively evaluate it if you develop it in Python.

##### Config
-  Edit the .env file

    `API_KEY` = The api token
    
    `OUTPUT_DIR` = Local folder you want to create to store the results

##### Instructions to create project
```javascript
bash run.sh
```

##### Instructions to run project
```javascript
python3 main.py
```
params:

  `Content type` = It can be Movie / Series / Episode.
  
  `Content name` = The name of the content you want to search for
  
  `year` = (Optional) The release year of the content.
 
output:
- A csv file with the results will be generated and exported to the local directory
