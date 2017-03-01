# opensubz
Two-click subtitle downloader script

![opensubz gif](https://j.gifs.com/nZP2BY.gif)

## Requirements
* [Python 3.x](https://www.python.org/downloads/)
* [opensubtitles.org](https://www.opensubtitles.org/newuser) Account

## How to Install
Install via pip
```bash
$ pip install opensubz
```

Install via github
```bash
$ git clone https://github.com/danielfsousa/opensubz.git
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

![context menu](https://cloud.githubusercontent.com/assets/11372312/23395366/f5d0ea4c-fd6c-11e6-95b8-11ce9c3990eb.png)

