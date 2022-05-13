# mdseo
> Analyze Markdown Documents Used In Static Sites For SEO


[![CI](https://github.com/outerbounds/mdseo/actions/workflows/main.yml/badge.svg)](https://github.com/outerbounds/mdseo/actions/workflows/main.yml)
 [![](https://img.shields.io/pypi/v/nbdoc)](https://pypi.org/project/mdseo/)
[![](https://img.shields.io/static/v1?label=fastai&message=nbdev&color=57aeac&labelColor=black&style=flat&logo=data:image/png;base64,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)](https://github.com/fastai/nbdev)

## Table of Contents


- [Installation](#installation)
- [Usage](#usage)
- [Ignoring Checks](#ignoring-checks)
    - [With Front Matter](#with-front-matter)
    - [With The Keyword `mdseo-ignore-all`](#with-the-keyword-mdseo-ignore-all)


## Installation

> pip install mdseo

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


```
!mdseo_slug -h
```

    usage: mdseo_slug [-h] [--srcdir SRCDIR]
    
    Check if docs do not have the field `slug` in their front matter. Ignore with
    front matter `mdseo-ignore: [slug]`
    
    optional arguments:
      -h, --help       show this help message and exit
      --srcdir SRCDIR  directory of files to check (default: .)


```
!mdseo_slug_len -h
```

    usage: mdseo_slug_len [-h] [--srcdir SRCDIR] [--n N]
    
    Check if docs have a `slug` field in their front matter that is less than `n`
    characters. Ignore with front matter `mdseo-ignore: [slug]`
    
    optional arguments:
      -h, --help       show this help message and exit
      --srcdir SRCDIR  directory of files to check (default: .)
      --n N            max number of characters for slug (default: 45)


```
!mdseo_author -h
```

    usage: mdseo_author [-h] [--srcdir SRCDIR]
    
    Check if docs do not have the field `authors` in their front matter. Ignore with
    front matter `mdseo-ignore: [authors]`
    
    optional arguments:
      -h, --help       show this help message and exit
      --srcdir SRCDIR  directory of files to check (default: .)


## Ignoring Checks

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

If you want to ignore all seo rules, you can also pass `all` like so:

```
---
mdseo-ignore: all
---
```

### With The Keyword `mdseo-ignore-all`

Some markdown files may not have front matter, or it may not be appropriate to add front matter to a file.  In this case you can place the text `mdseo-ignore-all` anywhere in the file and all checks will be ignored, the most common way to add this keyword is with a markdown comment:

```
<-- mdseo-ignore-all -->
```

