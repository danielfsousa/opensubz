# opensubz
Two-click subtitle search script

## Requirements
* [Python 3.x](https://www.python.org/downloads/)
* [opensubtitles.org](https://www.opensubtitles.org/newuser) Account

## How to Install
Clone project
```bash
$ git clone https://github.com/danielfsousa/opensubz.git
```

Install package
```bash
$ cd opensubz
$ pip install . --upgrade
```

For the first time you run opensubz you will be prompted to login into your opensubtitles account.
```bash
$ opensubz --help
```

Add opensubz shortcut to Windows context menu
```bash
$ opensubz --install
```

## How to Use
**Command line:**
```bash
$ opensubz -s [PATH] -l [LANGUAGE CODE]
```

Ex:
```bash
$ opensubz -s . -l "pob"
$ opensubz --search "C:\TvShows"
$ opensubz --search "C:\Movies" --language "eng"
```

**Context menu:**
Rigth click on any folder than click "Download Subtitles"

