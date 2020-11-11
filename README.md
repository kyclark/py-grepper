# The Grepper

Read patterns of text from a patterns file, use these to find lines from input files, write matches to output file.

```
$ ./grepper.py -h
usage: grepper.py [-h] -p FILE -f FILE [FILE ...] [-o FILE]

Find patterns in files

optional arguments:
  -h, --help            show this help message and exit
  -p FILE, --pattern FILE
                        Patterns file (default: None)
  -f FILE [FILE ...], --file FILE [FILE ...]
                        A readable file (default: None)
  -o FILE, --out_file FILE
                        Output file (default: out.txt)
```

The patterns file should write regular expressions to individual lines:

```
$ cat tests/inputs/patterns.txt
foo
bar
baz
```

The input files may have matches to these. For instance, the first input file:

```
$ cat tests/inputs/input1.txt
a
b
c foo
d
bar e
f
g baz h
```

If you run the program with these file, three lines should be written to "out.txt":

```
$ ./grepper.py -p tests/inputs/patterns.txt -f tests/inputs/input1.txt
Done, wrote 3 matches to "out.txt."
```

Verify that the lines are present:

```
$ cat out.txt
c foo
bar e
g baz h
```

Run `pytest` or `make test` to run the test suite.

## Author

Ken Youens-Clark <kyclark@gmail.com>
