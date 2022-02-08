# CASE STUDY 1

### 1. Config
Edit the `.env` file

    `API_KEY` = The api token
    
    `OUTPUT_DIR` = Local folder you want to create to store the results


### 2. Instructions to install dependencies

It creates a virtual environment and install all libraries in it.

```javascript
bash run.sh
```

### 3. Instructions to run project

It will ask to input on screen the Content type and Content name, and the results will be exported to a local directory in the format of csv.

```javascript
python3 main.py
```

##### Params:

  `Content type` = It can be Movie / Series / Episode.
  
  `Content name` = The name of the content you want to search for
  
  `year` = (Optional) The release year of the content.
 
##### Output:
A csv file with the results will be generated and exported to the local directory
