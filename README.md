# UntrackChanges
Removes trackchanges from LaTeX

The LaTeX package [`trackchanges`](http://trackchanges.sourceforge.net/) is great! However, sometimes I want to quickly convert all the commands to plain LaTeX. This sometimes happens if I don't have `trackchanges` installed somewhere, or if it's interfering with the wordcount. This is where this python script comes in!

## Features

This script does three things:

1. Replaces `\add{foo}` with `foo`.
2. Deletes `\delete{bar}`.
3. Replaces `\change{foo}{bar}` with `bar`.

**Warning:** This script will **not** proceed if the `trackchanges` commands are invalid. I.e. if the curly brackets are unbalanced, this code will error.

## Usage

Currently, this is used as a script on a plain `.tex` file, e.g.

`python untrackchanges.py file.tex`

This will produce a new file with a `.untrack` extension. 

## Todo

- [x] Complete tests
- [x] Add options for changes
- [x] Add checking before computations
- [x] Better file naming
