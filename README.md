# File Encoding Detector and Converter

## Description:

This is a Python script that verifies the encoding of a file. It uses chardet (`http://chardet.readthedocs.io/en/latest/usage.html`) to detect the encoding.

Finally, it generates an output file from the source with utf-8 encoding. 


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

## License
Please see license.txt
 