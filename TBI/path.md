
A path is a string consist of the folowing

prefix:///path/to/file/fileName.ext1.ext2

- prefix:// -> refers to file system. each prefix is linked ot a file system name.
for example 'file://' is the 'Local' storage and 's3://' is the 'AWS-S3' storage
- /path/to/file/ -> is the path to file. if it starts with a / it means the path is absolute and from the root of the file system. otherwise the path is considered relative.
- fileName
- .ext1.ext2 -> (variable number of prefix) tells you about the format and the compression of the file. i.e. .tsv.gz means the format is tsv and the compression is gzip.

Note: the file name may consist '.' character too. Only known extensions in the tail are considerd as extensions.
examples:
- abc.def.tsv.gz -> .tsv.gz
- abc.tsv.def.gz -> .gz (tsv is not in the tail and is not considered as extension also 'def' is not a known extension)

the path may involve wildcards and environemnt-variables like:
file://users/${USER}/chr-*.vcf.bgz

the above path may refe to all the following paths
file://users/me/chr-1.vcf.bgz
file://users/me/chr-2.vcf.bgz
file://users/me/chr-3.vcf.bgz

os.path has the following function: 
expandvars (i think it works on any string contain $VarName or ${VarName})
abspath

also there is glob.glob to expand wildcard and regex in path
https://docs.python.org/3/library/glob.html

All above are for local storage. for hdfs, s3 and others we need to find other functions

there are many library to work with path on different file system.
but they are all utility. that means they provide functions to work with path.

This class is going to be the path object that holds the path in itself

The user may define a path with a string but the full path specification is an object as below
- rawPath: file://users/${USER}/chr-*.vcf.bgz 
- path: file://users/me/chr-2.vcf.bgz
- format: vcf
- compression: bgz
- type: file (file, directory, table, database) (table is a table in a database)
- exist: boolean

This class mimic a list object where a list of path can be assigned to it.

The list may consist of either string (simpl path) or a path object (not necessarly with all field).

This class hold the list until the process function is called.
Then it look on each item in the list. if it is an string it should be convered to a path object
the string may refer to multiple files (wildcard) in this case multiple path obj is added to the list
if the item is path object it should be checked for consistency.

there are 2 property
paths: return the 'path' part of all path object as a list
path : return the only path in the list (exception if there are more)

This class should be YAML and JSON dump compatible

the path object has a Exist() function
this class has a ExistAll() and ExistAny() function

the class also have this property
- format: 'multiple' if paths in the list have different format 
- compression: 'multiple' if paths in the list have different format 
- type: 'multiple' if paths in the list have different format 
- existAll: boolean
- existAny: boolean
- exist: alias for existAll


## Room for future improvement
- to be able to look at the contet of the file to infer its format.

## Notes for other module
- overide export format (compression) based on the infered or given format.


```python
def Examples():
    res = PathList(data='/bla/bla/xxx.tsv')
    res = PathList(data={'path':'/bla/bla/yyy.tsv', 'format':'csv'})


    res = PathList(data=[
        'file://a*.tsv',
        {'path':'hdfs://b*.tsv', 'format':'csv'}
        ])

    res == [
        {'raw':'file://a*.tsv', 'path':'file://a1.tsv', 'format':'tsv', 'fileSystem': 'local'},
        {'raw':'file://a*.tsv', 'path':'file://a2.tsv', 'format':'tsv', 'fileSystem': 'local'},
        {'raw':'hdfs://b*.tsv', 'path':'hdfs://b1.tsv', 'format':'tsv', 'fileSystem': 'hdfs'},
        {'raw':'hdfs://b*.tsv', 'path':'hdfs://b2.tsv', 'format':'tsv', 'fileSystem': 'hdfs'}
    ]
    all=={'raw':'#'            , 'path':'#'            , 'format':'tsv', 'fileSystem': 'multi'}
```