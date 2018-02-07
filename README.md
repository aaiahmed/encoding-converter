# File Encoding Detector and Converter

## Description:

This is a Python script that goes through a file line-by-line and verifies the encoding on each line. Be default, the script uses chardet (`http://chardet.readthedocs.io/en/latest/usage.html`) to detect the encoding on each line. It displays any line, that does not match with the optionally specified source encoding (default utf-8). If the confidence level from chardet detection is lower than 80%, it manually loops through all the standard encodings (`https://docs.python.org/3/library/codecs.html#standard-encodings`) and verifies by decoding with the corresponding encoding.

Finally, it generates an output file from the source with utf-8 encoding. 
 
## Requirements:

The script is written in Python 3.6.4. The only non-standard module is chardet, which can be installed by:

```
pip install -R requirements.txt
```

## How to Run the program:

The script can be run by:

```
python encoding_converter.py --source="source_file.txt" --source_enc='latin-1'
```

The source encoding is optional. It will assume 'utf-8' is the parameter is skipped. 

For help,
```
python encoding_converter.py --help
```

## Running tests:

There is an excellent example at (https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-test.txt) to test UTF-8 character decoding capability. 

## Author
Abdullah Al Iftekhar Ahmed
Email: iftekhar.ahmed @ mun . ca (remove spaces)

## License
Please see license.txt
 