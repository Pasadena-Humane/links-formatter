# links-formatter

Script to format links (i.e., emails, phones, websites) into code blocks for the wiki.

Related [issue](https://github.com/Pasadena-Humane/Wildlife/issues/7).

## Prerequisites

Python 3.x.

Create `input_files` and `output_files` directories inside this project directory. 

```bash
mkdir ./links-formatter/input_files
mkdir ./links-formatter/output_files
```

## Usage

1. Put the files to be formatted in `input_files`. 
2. While inside this project directory, run the main app.

```bash
python3 -m main
```

3. The output will display matches found and formatted. Finished files will be in `output_files`.

```
Matches found: ['email@domain.com', ...]
Matches found: ['(123) 456-7899', ...]
Matches found: ['https://website.com', ...]
```