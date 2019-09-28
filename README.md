# humanice

[![CircleCI](https://circleci.com/gh/timwedde/humanice.svg?style=svg)](https://circleci.com/gh/timwedde/humanice)
[![codecov](https://codecov.io/gh/timwedde/humanice/branch/master/graph/badge.svg)](https://codecov.io/gh/timwedde/humanice)

This modest package contains various common humanization utilities, like turning a number into a fuzzy human readable duration (i.e. `3 minutes ago`) or into a human readable size or throughput. It works with Python 3 and is localized to a bunch of languages.


## Installation

`humanice` can be installed via pip:
```bash
$ pip install humanice
```

Alternatively you can build the package by cloning this repository:
```bash
$ git clone https://github.com/timwedde/humanice.git
$ cd humanice/
$ python3 setupy.py install
```

## Usage

### Integer humanization

```python
>>> import humanice
>>> humanice.intcomma(12345)
'12,345'
>>> humanice.intword(123455913)
'123.5 million'
>>> humanice.intword(12345591313)
'12.3 billion'
>>> humanice.apnumber(4)
'four'
>>> humanice.apnumber(41)
'41'
```

### Date & time humanization

```python
>>> import datetime
>>> humanice.naturalday(datetime.datetime.now())
'today'
>>> humanice.naturaldelta(datetime.timedelta(seconds=1001))
'16 minutes'
>>> humanice.naturalday(datetime.datetime.now() - datetime.timedelta(days=1))
'yesterday'
>>> humanice.naturalday(datetime.date(2007, 6, 5))
'Jun 05'
>>> humanice.naturaldate(datetime.date(2007, 6, 5))
'Jun 05 2007'
>>> humanice.naturaltime(datetime.datetime.now() - datetime.timedelta(seconds=1))
'a second ago'
>>> humanice.naturaltime(datetime.datetime.now() - datetime.timedelta(seconds=3600))
'an hour ago'
```

### Filesize humanization

```python
>>> humanice.naturalsize(1000000)
'1.0 MB'
>>> humanice.naturalsize(1000000, binary=True)
'976.6 KiB'
>>> humanice.naturalsize(1000000, gnu=True)
'976.6K'
```

### Human-readable floating point numbers

```python
>>> humanice.fractional(1/3)
'1/3'
>>> humanice.fractional(1.5)
'1 1/2'
>>> humanice.fractional(0.3)
'3/10'
>>> humanice.fractional(0.333)
'1/3'
>>> humanice.fractional(1)
'1'
```

## Localization

### How to change locale in runtime

```python
>>> humanice.naturaltime(datetime.timedelta(seconds=3))
3 seconds ago
>>> _t = humanice.i18n.activate('ru_RU')
>>> humanice.naturaltime(datetime.timedelta(seconds=3))
3 секунды назад
>>> humanice.i18n.deactivate()
>>> humanice.naturaltime(datetime.timedelta(seconds=3))
3 seconds ago
```

You can pass additional parameter *path* to `activate` to specify a path to search locales in:

```python
>>> humanice.i18n.activate('pt_BR')
IOError: [Errno 2] No translation file found for domain: 'humanice'
>>> humanice.i18n.activate('pt_BR', path='path/to/my/portuguese/translation/')
<gettext.GNUTranslations instance ...>
```

### How to add new phrases to existing locale files

```bash
$ xgettext -o humanice.pot -k'_' -k'N_' -k'P_:1c,2' -l python humanice/*.py  # extract new phrases
$ msgmerge -U humanice/locale/ru_RU/LC_MESSAGES/humanice.po humanice.pot # add them to locale files
$ msgfmt --check -o humanice/locale/ru_RU/LC_MESSAGES/humanice{.mo,.po} # compile to binary .mo
```

### How to add a new locale

```bash
$ msginit -i humanice.pot -o humanice/locale/<locale name>/LC_MESSAGES/humanice.po --locale <locale name>
```

Where `<locale name>` is locale abbreviation, eg `en_GB`, `pt_BR` or just `ru`, `fr` etc.


## Supported Languages

* German
* Finnish
* French
* Indonesian
* Italian
* Japanese
* Korean
* Dutch
* Portugese
* Russian
* Slovak
* Turkish
* Vietnamese
* Simplified Chinese
