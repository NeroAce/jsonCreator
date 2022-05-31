# jsonCreator

**jsonCreator** is a simple python Module/Library to create  json files.

create json file:
```python
import jsonCreator

y = {
    "student 01":
    {"Name":"Neelansh",
    "course":"A-Level",
    "Fees":3200},

    "student 02":
    {"Name":"Vivek",
    "course": "A=level",
    "Fees": 1800}
    }

jsonCreator.createJson(y,"firstFile","/workspaces/72345097/jsonCreator")
```
**output:** /workspaces/72345097/jsonCreator/firstFile.json
```json
{"student 01": {"Name": "Neelansh", "course": "A-Level", "Fees": 3200}, "student 02": {"Name": "Vivek", "course": "A=level", "Fees": 1800}}
```

Append this file:
```python
import jsonCreator

y = {
    "student 03":
    {"Name":"Vidit",
    "course":"A-Level",
    "Fees":3200},

    "student 04":
    {"Name":"Deepak",
    "course": "A=level",
    "Fees": 1800}
    }

jsonCreator.appendJson(y,"firstFile",'/workspaces/72345097/jsonCreator')


```
**output: ** /workspaces/72345097/jsonCreator/firstFile.json
```json
[{"student 01": {"Name": "Neelansh", "course": "A-Level", "Fees": 3200}, "student 02": {"Name": "Vivek", "course": "A=level", "Fees": 1800}},{"student 03": {"Name": "Vidit", "course": "A-Level", "Fees": 3200}, "student 04": {"Name": "Deepak", "course": "A=level", "Fees": 1800}}]
```

**jsonCreator** `creates` and `appends` json files.
It takes a `dictionary` as input and creates a json file, there is no need to manually add data in the file, it also appends another dictionary as `a list of dictionaries` in the previously created json file.

------------

## # The User Guide

To import  : `import jsonCreator`

jsonCreator contain two method, `createJson()` and `appendJson()`
.
### createJson()
createJson() method accepts three parameters `dic`, `"fileName"` and `[“path”]`:

			`jsonCreator.createJson(dic,”fileName”,[“path”])`
								
dic  = `dict `dataTypen\
fileName = `string` dataType\
path = `string` dataType

dic must be a `dictionary` and fileName must be `string`, path parameter is optional. If you do not specify a path directory then the file will be created in the same directory as your script.
To specify a path parameter you must pass the path directory as `string`. And the path directory must be separated with `/` or `\\` not with` \ `.

 example : “`C:/Program Files/Windows Mail`” or “`C:\\Program Files\\Windows Mail”` but not this `“C:\Program Files\Windows Mail”`
 
 Other wise you will get `SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-4`  error
 
 Must see above example for more clarification.

### appendJson()
appendJson() method also accepts three parameters dic, "fileName" and [“path”]:


    			`jsonCreator.appendJson(dic, "fileName”,[“path”])`
dic = `dict`dataType
fileName = `string` dataType
path = `string` dataType

dic must be a `dictionary` and fileName must be a `string` which is already present/exists, path parameter is optional. If you do not specify a path directory then the file will be searched in the same directory as your script, i.e If you do not specify a path, then file must be present in the same directory as your script. 

To specify a path parameter you must pass the path directory as string. And the path directory must be separated with` /` or` \\` not with`\`.

example : `“C:/Program Files/Windows Mail”` or `“C:\\Program Files\\Windows Mail”` but not this `“C:\Program Files\Windows Mail”`

Other wise you will get `SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-4` error.

Must see above example for more clarification.

