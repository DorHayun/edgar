from pathlib import Path
from benedict import benedict
import os
import json

#getting all the json files pathes from a given directory
raw_files = Path('/home/ubuntu/bp-tmp-volatile').rglob('*.json')
with open('output.jsonl', 'a') as outfile:


    #iterating over the json files
    for file in raw_files:
        print(f"starting to modify {Path(file).name}")

        #opening the json file with writing permission
        with open(file, 'r') as f:
            #getting the file as dictionary
            data = json.load(f, strict=False)

            #deleting the HTML attribute
            del data["HTML"]

            #initialize benedict object in order to normalize the keys to lower cases
            d = benedict(data) 
            #convert all string keys to snalower case (nested dict keys included)
            d.standardize()   
            print(Path(file).name+ " successfully changed")    
            json.dump(data, outfile)
            outfile.write(os.linesep)
            print(Path(file).name+ " successfully added to Json lines file ")
