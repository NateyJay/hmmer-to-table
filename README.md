# hmmer-to-table
 A simple tool for converting hmmer outputs to a complete table

#### Motivation:

Hmmer is an extremely powerful search tool. Unfortunately, it's output leaves something to be desired. Though it is capable of producing tables, they are not easily machine-readable (inconsistent header formatting, consecutive white-space delimiters, reused delimiters in fields, uncommented comment lines). **It's really _awful_**. It also lacks descriptions of other domains than the first hit for a protein sequence.

The human-readable standard output is much more informative, but still fairly useless for a tool like R.

This tool simply parses the human-readable format, outputing each domain hit as a line.



#### Usage:

```
## Writing to stdout
./hmmer-to-table.py -f ./test_files/*

## Writing to a file
./hmmer-to-table.py -f ./test_files/* -o concatenated_table.txt
```
