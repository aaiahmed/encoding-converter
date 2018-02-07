#!/usr/bin/env python3

"""
This program detects the encoding of a file and converts to UTF-8

__author__          = "Abdullah Ahmed"
__version__         = "0.1"
__email__           = "iftekhar.ahmed @ mun . ca"
__status__          = "Production"
__python_vesrion__  = "3.6"

Example:
    $ python encoding_converter.py --source="source_file" --source_enc='ascii'
"""

import os
import argparse
import chardet

# ------------------------------
# configurations
DETECTION_THRESHOLD = 0.8

encodings = [['ascii', 'English'],
             ['utf-8', 'all languages'],
             ['big5', 'Traditional Chinese'],
             ['big5hkscs', 'Traditional Chinese'],
             ['cp037', 'English'],
             ['cp273', 'German'],
             ['cp424', 'Hebrew'],
             ['cp437', 'English'],
             ['cp500', 'Western Europe'],
             ['cp720', 'Arabic'],
             ['cp737', 'Greek'],
             ['cp775', 'Baltic languages'],
             ['cp850', 'Western Europe'],
             ['cp852', 'Central and Eastern Europe'],
             ['cp855', 'Bulgarian, Byelorussian, Macedonian, Russian, Serbian'],
             ['cp856', 'Hebrew'],
             ['cp857', 'Turkish'],
             ['cp858', 'Western Europe'],
             ['cp860', 'Portuguese'],
             ['cp861', 'Icelandic'],
             ['cp862', 'Hebrew'],
             ['cp863', 'Canadian'],
             ['cp864', 'Arabic'],
             ['cp865', 'Norwegian'],
             ['cp866', 'Russian'],
             ['cp869', 'Greek'],
             ['cp874', 'Thai'],
             ['cp875', 'Greek'],
             ['cp932', 'Japanese'],
             ['cp949', 'Korean'],
             ['cp950', 'Traditional Chinese'],
             ['cp1006', 'Urdu'],
             ['cp1026', 'Turkish'],
             ['cp1125', 'Ukrainian'],
             ['cp1140', 'Western Europe'],
             ['cp1250', 'Central and Eastern Europe'],
             ['cp1251', 'Bulgarian, Byelorussian, Macedonian, Russian, Serbian'],
             ['cp1252', 'Western Europe'],
             ['cp1253', 'Greek'],
             ['cp1254', 'Turkish'],
             ['cp1255', 'Hebrew'],
             ['cp1256', 'Arabic'],
             ['cp1257', 'Baltic languages'],
             ['cp1258', 'Vietnamese'],
             ['cp65001', 'Windows UTF-8'],
             ['euc-jp', 'Japanese'],
             ['euc-jis_2004', 'Japanese'],
             ['euc-jisx0213', 'Japanese'],
             ['euc-kr', 'Korean'],
             ['gb2312', 'Simplified Chinese'],
             ['gbk', 'Unified Chinese'],
             ['gb18030', 'Unified Chinese'],
             ['hz', 'Simplified Chinese'],
             ['iso2022-jp', 'Japanese'],
             ['iso2022-jp-1', 'Japanese'],
             ['iso2022-jp-2',	'Japanese, Korean, Simplified Chinese, Western Europe, Greek'],
             ['iso2022-jp-2004', 'Japanese'],
             ['iso2022-jp-3', 'Japanese'],
             ['iso2022-jp-ext', 'Japanese'],
             ['iso2022-kr', 'Korean'],
             ['latin_1', 'West Europe'],
             ['iso8859-2', 'Central and Eastern Europe'],
             ['iso8859-3', 'Esperanto, Maltese'],
             ['iso8859-4', 'Baltic languages'],
             ['iso8859-5', 'Bulgarian, Byelorussian, Macedonian, Russian, Serbian'],
             ['iso8859-6', 'Arabic'],
             ['iso8859-7', 'Greek'],
             ['iso8859-8', 'Hebrew'],
             ['iso8859-9', 'Turkish'],
             ['iso8859-10', 'Nordic languages'],
             ['iso8859-11', 'Thai languages'],
             ['iso8859-13', 'Baltic languages'],
             ['iso8859-14', 'Celtic languages'],
             ['iso8859-15', 'Western Europe'],
             ['iso8859_16', 'South-Eastern Europe'],
             ['johab', 'Korean'],
             ['koi8-r', 'Russian'],
             ['koi8-t', 'Tajik'],
             ['koi8-u', 'Ukrainian'],
             ['kz1048', 'Kazakh'],
             ['mac-cyrillic', 'Bulgarian, Byelorussian, Macedonian, Russian, Serbian'],
             ['mac-greek', 'Greek'],
             ['mac-iceland', 'Icelandic'],
             ['mac-latin2', 'Central and Eastern Europe'],
             ['mac-roman', 'Western Europe'],
             ['mac-turkish', 'Turkish'],
             ['ptcp154', 'Kazakh'],
             ['shift-jis', 'Japanese'],
             ['shift-jis_2004', 'Japanese'],
             ['shift-jisx0213', 'Japanese'],
             ['utf-32', 'all languages'],
             ['utf-32-be', 'all languages'],
             ['utf-32-le', 'all languages'],
             ['utf-16', 'all languages'],
             ['utf-16-be', 'all languages'],
             ['utf-16-le', 'all languages'],
             ['utf-7', 'all languages'],
             ['utf-8-sig', 'all languages']]

# ------------------------------
# helper functions

def arg_parse():
    """parse input arguments"""

    parser = argparse.ArgumentParser(description='Encoding Detector & Converter')
    parser.add_argument('--source', help='source file.')
    parser.add_argument('--source_enc', default='utf-8', help='source file.')
    args = parser.parse_args()
    return args

def clear_output_file(output_file):
    """overwrite output_file (if exists)"""

    with open(output_file, 'w+', encoding='utf-8') as fw:
        pass

def write_file(file_name, file_enc, file_content):
    """write content with passed encoding"""

    with open(file_name, 'a', encoding=file_enc) as fw:
        fw.write(file_content.rstrip()+'\n')

def manually_detect(line, line_num):
    """if chardet fails, manually loop through the supported encodings"""

    line_content = ''
    for enc in encodings:
        try:
            line_content = line.decode(enc[0])
            line_content = line_content.encode(enc[0]).decode('utf-8')
            print('Line %s: "%s" has encoding: "%s", Language/Region: "%s" [manual].' % \
            (line_num, line_content.rstrip(), enc[0], enc[1]))
            break
        except:
            pass
    return line_content

def detect_and_convert(source_file, source_enc, output_file):
    """detect and convert"""

    clear_output_file(output_file)
    with open(source_file, 'rb') as fr:
        for line_num, line in enumerate(fr):
            try:
                line_content = line.decode(source_enc)
            except:
                detected = chardet.detect(line)
                if float(detected['confidence']) > DETECTION_THRESHOLD:
                    try:
                        line_content = line.decode(detected['encoding'])
                        line_content = line_content.encode(detected['encoding']).decode('utf-8')
                        print('Line %s: "%s" has encoding: "%s". Confidence: %s [chardet]' % \
                        (line_num, line_content.rstrip(), detected['encoding'], detected['confidence']))
                    except:
                        line_content = manually_detect(line, line_num)
                else:
                    line_content = manually_detect(line, line_num)
            write_file(output_file, 'utf-8', line_content)


# start operation
def main():
    """main function"""

    args = arg_parse()
    print('------------------------------------------------------------------------------------')
    print('Starting encoding detection and conversion to utf-8 for file: %s' % (args.source))
    print('------------------------------------------------------------------------------------')
    output_file = os.path.join(os.getcwd(), os.path.splitext(args.source)[0] + '_converted.txt')
    detect_and_convert(args.source, args.source_enc, output_file)
    print('------------------------------------------------------------------------------------')
    print('File "%s" successfully converted to "utf-8" encoding.' % (args.source))
    print('Output File: "%s"' % output_file)

if __name__ == "__main__":
    main()
