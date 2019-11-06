
# coding: utf-8

# In[97]:


# Importing Os - For getting paths in a directory and joining paths
# Importing Json for reading and writing JSON
import os
import json


# In[99]:


# Taking all the Required Inputs
folderPath =  input("Enter Folder Path :")
inputFileBaseName = input("Enter Input File Base Name :")
outputFileBaseName = input("Enter Output File Base Name :")
maxFileSize = input("Enter Max File Size :")


# In[100]:


# Getting all files for given input Directory
all_files = [file for file in os.listdir(folderPath) ]


# In[101]:


# One line Implemantation using list Comprehension to get all files with basePrefix Input Name
# ====
# filePaths = [os.path.join(folderPath,f) for f in os.listdir(folderPath) if f.startswith(inputFileBaseName) ]
# ====


# More Readable Code

filePaths = []
for file in os.listdir(folderPath):
#     Check if FileName Starts with Input File Base Name
    if(file.startswith(inputFileBaseName)):
#         Make Json File Path if true and add to filePaths list
        tempPath = os.path.join(folderPath,file)
        filePaths.append(tempPath)


# In[113]:


# In the odd case where files are not sorted alphabetically
filePaths.sort()


# In[106]:


# Get First JSON File with which we will merge all other JSON Files
# Its Called baseJSON
file = open(file_paths[0] ,"r")
rawFile = file.read()
baseJson= json.loads(rawFile)
file.close()


# In[103]:


# Loop over all the files in filePath List
# Open Each file
for counter,file in enumerate(filePaths):
    if(counter == 0):
        continue
    file = open(file ,"r")
    rawFile = file.read()
#     Get the Current File
    jsonFileCurrent= json.loads(rawFile)
    
#     Get List of All keys to make our Utility Genral to work on examples with multiple keys
#      as explained in question PDF
#     if key name is 'emplyoee' instead of 'striker'
#     or if JSON contains multiple such key Lists
    keyList = list(baseJson.keys())
    
#     Loop over all key Names and merge Key List of current file with list of base Json File
    for key in keyList:
           baseJson[key].extend(jsonFileCurrent[key])
    
    file.close()


# In[104]:


# Name of output file
outputFileBaseName = outputFileBaseName + ".json"


# In[105]:


# Wrtie base Json to output file
with open(os.path.join(folderPath,outputFileBaseName) , 'w', encoding='utf-8') as f:
    json.dump(baseJson,f,indent=4)

