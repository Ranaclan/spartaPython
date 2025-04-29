# Linux Research

* [Redirecting](#redirecting)
* [Piping](#piping)
* [Streams](#streams)

## Redirecting

Using the character '>' will send the given input into a file.
```bash
echo a > a.txt
```
This will write 'a' into a file named 'a.txt'.

### Appending
Appending is done using two angular brackets: '>>'. This appends lines to the given file, rather than overwriting the file.
```bash
echo a >> a.txt
```
This will write another 'a' to 'a.txt', resulting in two 'a's on separate lines.

## Piping
Piping allows the output of one command to feed into a further command. This is done using this character: '|'
```bash
commandOne | commandTwo
```
The output of commandOne will be used as input for commandTwo.

This is different to redirection as redirection is feeding input/output to/from files.

```bash
commandOne > fileName
```
The output of commandOne will be saved in the file 'fileName'

### Examples
```bash
ls | grep fileName
```
This will list the files in the current directory, then feed that result into the grep command, resulting in just the files called 'fileName' being output.


```bash
ls | grep fileName | head -n 2
```
This will list the files in the current directory, then feed that result into the grep command to get just the files called 'fileName', then feed that result into the head command to list only the first two results.


```bash
ls | grep fileName > files.txt
```
This will list the files in the current directory, then feed that result into the grep command to get just the files called 'fileName', then sending that output into a file called 'files.txt'

## Streams
Streams are input and output to and from a program, from or to the hardware. There are 3 data streams:
* stdin: Source of input for a program
* stdout: Destination of output from a program
* stderr: Destination of error messages