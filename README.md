# Scrapy Crawler for Alibaba
> A modifiable crawler for alibaba website to crawl and scrap product data

[![Python Version][python-image]][python-url]
[![Scrapy Version][scrapy-image]][scrapy-url]

This Repo is using various technique to scrap data from alibaba and
download product images. Also it outputs csv file from where it can be
converted to proper xml for uploading into any website via plugins or
another means.


## Installation & Setup
NOTE: Before anything, you should have Python 3 installed (preferable 3.6)

Download:
- [PYTHON](https://www.python.org/)
- [VS CODE](https://code.visualstudio.com/) for code editing but can be used any text editor like NOTEPAD


 Open up a command line tools and type:


Linux (terminal or bash):

```bash
git clone https://github.com/PandorAstrum/alibaba_skrapy.git
pip install -r requirements.txt
```
Windows (cmd):

```CMD
git clone https://github.com/PandorAstrum/alibaba_skrapy.git
pip install -r requirements.txt
```

## Folder Structure

(project root folder)

    ├── alibaba(folder)                 # contains the scrapper
    │   ├── spiders(folder)             # spider folder
    │   │   └── alibaba_spiders.py      # the main spider
    │   │
    │   ├── exporter.py                 # custom exporter for csv and xml
    │   ├── items.py                    # items to scrap
    │   ├── middlewares.py              # middlewares for the scrapper
    │   ├── pipelines.py                # pre processing stage
    │   └── settings.py                 # core settings fro the spider
    │
    ├── hooks(folder)                   # Hooks for building scrapy into executable
    │   └── hook-scrapy.py              # scrapy hooks file
    │
    ├── ui.py                           # main Logic for the UI
    ├── ui_support.py                   # supporting variables for ui inputs
    ├── scrapy.cfg                      # scrapy framework settings
    └── run.py                          # run spider and download image functions

## Example Usage
- on the cmd or bash cd to folder where this repo is downloaded and extracted
- then type:
```
python ui_support.py
```
It will start running the UI along with all function ready to use

- for building into an executable for windows, type:
```
pyinstaller Alibaba-Scrapper.spec
```
It will compile everything and build the executable into dist folder

## UI Inputs

**URL**
```cs
Provide an url to scrap <string>
```
Change it according to your needs
<br>

**OUTPUT FILE NAME**
```cs
Provide a name for the output file <string>
```
Change the name according to your needs
<br>

**ONLY GET CATEGORIES**
```cs
Checkmarks to get either data or categories
```
Check on or off according to your needs
<br>

**OUTPUT FOLDER**
```cs
Browse a directory to store the final result
```
e.g: "C:\\Users\\Username\\Desktop\\project\\"
NOTE: anywhere in C drive is preferred
<br>

**PREVIOUS CSV (OPTIONAL)**
```cs
Location of previously scrapped csv files
```
e.g: "C:\\Users\\Username\\Desktop\\project\\scrapped_Apr_05_2019_15_41_32.csv"
<br>

**USER AGENTS**
```cs
User Agents for each request <string>
```
NOTE: It is set by default. Dont change until you google about user agents.
<br>

**DELAY**
```cs
Delay number between each request <int>
```
NOTE: by default its 0 (zero). Only put numbers here
<br>

**CSV FILES CONTAINS "images_links"**
```cs
Location of the file having tha column name "images_links"
```
e.g: "C:\\Users\\Username\\Desktop\\project\\scrapped_Apr_05_2019_15_41_32.csv"
<br>


## Release History

* 1.0
    * simple scrapper along with image downloader

## Meta

Ashiquzzaman Khan – [@dreadlordn](https://twitter.com/dreadlordn)

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/PandorAstrum/alibaba_skrapy](https://github.com/PandorAstrum/alibaba_skrapy)

## Contributing

1. Fork it (<https://github.com/PandorAstrum/alibaba_skrapy>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[python-image]: https://img.shields.io/badge/Python-3.6-yellowgreen.svg?style=flat-square
[python-url]: https://www.python.org/

[scrapy-image]: https://img.shields.io/badge/scrapy-1.6-orange.svg?style=flat-square
[scrapy-url]: https://scrapy.org/

[travis-image]: https://travis-ci.org/PandorAstrum/_vault.svg?branch=master
[travis-url]: https://travis-ci.org/PandorAstrum/_vault

[appveyor-image]: https://ci.appveyor.com/api/projects/status/8dxrtild5jew79pq?svg=true
[appveyor-url]: https://ci.appveyor.com/project/PandorAstrum/vault

[ReadTheDoc]: https://github.com/yourname/yourproject/wiki

<!-- Header Pictures and Other media-->
[header-pic]: header.png
