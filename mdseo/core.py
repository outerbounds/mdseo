# AUTOGENERATED! DO NOT EDIT! File to edit: core.ipynb (unless otherwise specified).

__all__ = ['get_meta', 'meta_list', 'find_dupe', 'chk_dupe_title', 'alias_map', 'chk_fm', 'chk_len']

# Cell
from fastcore.all import globtastic, Path, merge, L, AttrDict, str_enum
from fastcore.script import call_parse
import re
import yaml
import json
import sys
from functools import partial
from collections import Counter

# Cell
_re_fm = re.compile(r'^---\s*(.*?)---\s*', flags=re.DOTALL)

def _load_yml(yml):
    if not yml: return {}
    else: return yaml.load(yml, Loader=yaml.FullLoader)

def get_meta(fname:str):
    "get metadata and front matter from `fname`."
    txt = Path(fname).read_text()
    fm = _re_fm.findall(txt)
    fm = _load_yml(fm[0] if fm else {})
    fm['mdseo-ignore'] = list(L(fm.get('mdseo-ignore', [])))
    clean_txt = re.sub('<[^<]+?>', '', _re_fm.sub('', txt))
    ignore = 'all' in fm['mdseo-ignore'] or 'mdseo-ignore-all' in txt
    if not ignore:
        return merge(dict(fname=fname,
                          n_words=len(clean_txt.split())),
                     fm)

# Cell
def meta_list(srcdir:str):
    "Get list of all metadata for markdown files in `srcdir`."
    docs = globtastic(srcdir, file_glob='*.md',
                      skip_folder_re='^[.]',
                      skip_file_re='^[_.]')
    return docs.map(get_meta).filter()

# Cell
def find_dupe(srcdir:str, key):
    "find duplicate values in front matter."
    c = Counter()
    for m in meta_list(srcdir):
        if 'dupe_title' in m['mdseo-ignore']: continue
        val = m.get(key)
        if val: c.update({f'{val}': 1})

    return [el[0] for el in c.items() if el[1] >= 2] if c else []

# Cell
@call_parse
def chk_dupe_title(srcdir:str='.', # directory of files to check
                  ):
    "Check for duplicate titles. Ignore with front matter `mdseo-ignore: [dupe_title]`"
    dupes = find_dupe(srcdir, 'title')
    msg = '\n\t'.join(dupes)
    if dupes: raise Exception(f"The following titles were found in multiple posts:\n\t{msg}")

# Cell
alias_map = {'description':['desc'],
             'slug': [],
             'image': ['img'],
             'authors': ['author']}
_en = str_enum('_en', *alias_map.keys())

# Cell
def _intersect(d, key): return set(d['mdseo-ignore']).intersection(set(alias_map.get(key, []) + [key]))

def _missing_fm(d, key):
    if _intersect(d, key): return False
    else: return key not in d

# Cell
def _min_len_err(d, key, n):
    if _intersect(d, key): return False
    # Return true if it is less than n length. Ignore with front matter `mdseo-ignore: [chk_fm slug]`.
    else: return key in d and not f"chk_fm {key}" in d["mdseo-ignore"] and len(d[key]) < n

def _max_len_err(d, key, n):
    if _intersect(d, key): return False
    # Return true if greater than n length. Ignore with front matter `mdseo-ignore: [chk_fm slug]`.
    else: return key in d and not f"chk_fm {key}" in d["mdseo-ignore"] and len(d[key]) > n

def _checker(func, msg:str, srcdir:str):
    fnames = meta_list(srcdir).filter(func).attrgot('fname')
    files = '\n\t'.join(fnames)
    if fnames: raise Exception(f"The following files {msg}:\n\t{files}")

# Cell
@call_parse
def chk_fm(key:_en, # front matter field to check
           srcdir:str='.', # directory of files to check
           minlen:int=None, #the minimum character length allowed for the field
           maxlen:int=None  #the maximum character length allowed for the field
          ):
    '''
    Check front matter for various rules.
    Ignore with front matter `mdseo-ignore: [chk_fm <key>]` - e.g. `mdseo-ignore: [chk_fm slug]`.
        Filtering happens in `_max_len_err` and `_min_len_err`.
    '''
    if not hasattr(_en, key): raise Exception(f'No rule exists for {key}')
    if minlen:
        return _checker(partial(_min_len_err, key=key, n=minlen),
                        f"have the field `{key}` in their front matter that is less than {minlen} characters", srcdir)
    elif maxlen:
        return _checker(partial(_max_len_err, key=key, n=maxlen),
                        f"have the field `{key}` in their front matter that is greater than {maxlen} characters", srcdir)

    _checker(partial(_missing_fm, key=key), f"do not have the field `{key}` in their front matter", srcdir)

# Cell
def _lt_n(d, n):
    if 'len' in d['mdseo-ignore'] or 'length' in d['mdseo-ignore']: return False
    return d['n_words'] < n

@call_parse
def chk_len(n:int=50, # minimum number of words a document should contain
            srcdir:str='.', # directory of files to check
           ):
    "Check if docs contain less than `n` words. Ignore with front matter `mdseo-ignore: [length]`"
    return _checker(partial(_lt_n, n=n), "contain less than 50 words", srcdir)