#!/usr/bin/env python3
# coding: utf-8

__doc__ = """
Transliteration of files containing Serbian word corpus.
Text is transliterated from Croatian Latin into Serbian Cyrillic script.
"""

import argparse
import codecs
import os
import sys

import py2srbcyr as py2c


def parse_args(arguments):

    parser = argparse.ArgumentParser(usage="CONLLU Serbian Transliterator")
    parser.add_argument('-i', '--input-file',
        help="Input file or files (wildcards supported)", required=True, nargs='+')
    parser.add_argument('-o', '--output-file',
        help="Output file or directory, if multiple files are selected", required=True)

    return parser.parse_args(arguments)


# Transliterates elements of .CONLLU file
def process_line(line, cyr):
    if line.startswith('# text ='):
        # Got "text = ...", needs transliteration
        l = line.split('=')
        return f"# text = {cyr.text_to_cyrillic(l[1])}"
    elif line == '':
        return line
    elif line[0].isdigit():
        l = line.split('\t')
        l[1] = cyr.text_to_cyrillic(l[1]) # word form
        l[2] = cyr.text_to_cyrillic(l[2]) # lemma
        if len(l) == 10 and l[9].startswith('Normalized='):
            l2 = l[9].split('=') # normalized part
            l[9] = f"Normalized=${cyr.text_to_cyrillic(l2[1])}"
        return '\t'.join(l)
    else:
        return line


# Transliterates a single file
def translit(input_file, output_file):
    cyr = py2c.SerbCyr()

    with codecs.open(input_file, 'rb', 'utf-8') as inpfile:
        with codecs.open(output_file, 'wb', 'utf-8') as outfile:

            while True:
                line = inpfile.readline()
                if len(line) == 0:
                    break
                line = line.strip()
                procline = process_line(line, cyr)
                outfile.write(f"{procline}\n")


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    if len(args.input_file) == 1:
        translit(args.input_file, args.output_file)
    else:
        out_normpath = os.path.normpath(args.output_file)
        # Check if output directory exists
        if not (os.path.exists(out_normpath) and os.path.isdir(out_normpath)):
            print(f"Directory '{args.output_file}' must exist")
            exit(1)
        # Transliterate files after wildcard expansion
        for file in args.input_file:
            _, file_ext = os.path.splitext(file)
            out_basename = os.path.basename(file).replace(file_ext, f"-cyr{file_ext}")
            outfile_name = os.path.abspath(os.path.join(os.path.curdir, out_normpath, out_basename))
            translit(file, outfile_name)
