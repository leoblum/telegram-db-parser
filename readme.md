### Telegram SQLite Database Parser for MacOS / iPhone

This is example project of parsing SQLite Telegram database on Python.
For example of usage see: `main.py`

Supported database for:
- Telegram for iOS
- Telegram for MacOS

Telegram for Desktop is not tested, but most likely that's uses different data structures.

To launch project you need to use Python 3.8 or less.
Python 3.9 is not supported because of [this issue](https://github.com/rigglemania/pysqlcipher3/issues/22) in dependency package.

Python 3.8 can be used together with other Python versions. Example of installation: 

```
brew install python@3.8
git clone https://github.com/totaleo/telegram-db-parser.git
cd telegram-db-parser
/usr/local/opt/python@3.8/bin/python3 -m pip -r requirements.txt
/usr/local/opt/python@3.8/bin/python3 main.py
```

Current supported only limited set of data types. 
Be free to send PR if you add new data structures.
