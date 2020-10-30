from pathlib import Path
from benedict import benedict
import json

#getting all the json files pathes from a given directory
raw_files = Path('/Users/dorh/Desktop/exm').rglob('*.json')

#iterating over the json files
for file in raw_files:
    print(f"starting to modify {Path(file).name}")

    #opening the json file with writing permission
    with open(file, 'r+') as f:
        #getting the file as dictionary
        data = json.load(f, strict=False)

        #deleting the HTML attribute
        del data["HTML"]

        #initialize benedict object in order to normalize the keys to lower cases
        d = benedict(data) 
        #convert all string keys to snalower case (nested dict keys included)
        d.standardize() 
        #should reset file position to the beginning.   
        f.seek(0)        
        json.dump(data, f, indent=4)
        # remove remaining part
        f.truncate() 
        #printing when the change succeeded    
        print(Path(file).name+ " successfully changed")

        #assigning the data dictionary in a list in order to use it with json lines
        list = [data]
        #creating or append to an existed jsonlines file the data dictionary
        with open('output.jsonl', 'a') as outfile:
            #iterating over json file objects
            for entry in list:
                json.dump(entry, outfile)
                outfile.write('\n')
            print(Path(file).name+ " successfully added to Json lines file ")