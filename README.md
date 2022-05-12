# mdseo
> Analyze Markdown Documents Used In Static Sites For SEO


## Usage

`mdseo` provides CLI tools to check various statistics and metadata in markdown files.  If an unwanted property is discovered, and error is raised.  An overview of the CLI tools are below:

```
!mdseo_dupe_title -h
```

    usage: mdseo_dupe_title [-h] [--srcdir SRCDIR]
    
    Check for duplicate titles. Ignore with front matter `mdseo-ignore:
    [dupe_title]`
    
    optional arguments:
      -h, --help       show this help message and exit
      --srcdir SRCDIR  directory of files to check (default: .)


```
!mdseo_img -h
```

    usage: mdseo_img [-h] [--srcdir SRCDIR]
    
    Check if docs do not have the field `image` in their front matter. Ignore with
    front matter `mdseo-ignore: [image]`
    
    optional arguments:
      -h, --help       show this help message and exit
      --srcdir SRCDIR  directory of files to check (default: .)


```
!mdseo_len -h
```

    usage: mdseo_len [-h] [--srcdir SRCDIR] n
    
    Check if docs contain less than `n` words. Ignore with front matter `mdseo-
    ignore: [length]`
    
    positional arguments:
      n                minimum number of words a document should contain
    
    optional arguments:
      -h, --help       show this help message and exit
      --srcdir SRCDIR  directory of files to check (default: .)


```
!mdseo_desc_len -h
```

    usage: mdseo_desc_len [-h] [--n_lower N_LOWER] [--n_upper N_UPPER]
                          [--srcdir SRCDIR]
    
    Check if docs have a description that is not between `n_lower` and `n_upper`
    characters. Ignore with front matter `mdseo-ignore: [description]`
    
    optional arguments:
      -h, --help         show this help message and exit
      --n_lower N_LOWER  the lower bound number of characters a document should
                         contain (default: 50)
      --n_upper N_UPPER  the upper bound number of characters a document should
                         contain (default: 300)
      --srcdir SRCDIR    directory of files to check (default: .)


## Ignore Checks

You may wish to ignore checks on individual files, there are two ways to do this (1) Through a special front-matter field called `mdseo-ignore` or (2) by placing the word `mdseo-ignore-all` in your markdown file.

### With Front Matter

To ignore a check via front matter, supply the proper value(s) in the `mdseo-ignore` field in your front matter.  For example, if you wanted to ignore the `mdseo_dupe_title` and `mdseo_image` checks in a particular markdown file, you would inject the following front matter:

```
---
mdseo-ignore: [dupe_title, image]
---
```

You can find these values by consulting the help of the appropriate cli command, for example `mdseo_dupe_title -h` says:

```
... Ignore with front matter `mdseo-ignore:[dupe_title]`
```

### With The Keyword `mdseo-ignore-all`

Some markdown files may not have front matter, or it may not be appropriate to add front matter to a file.  In this case you can place the text `mdseo-ignore-all` anywhere in the file and all checks will be ignored, the most common way to add this keyword is with a markdown comment:

```
<-- mdseo-ignore-all -->
```

