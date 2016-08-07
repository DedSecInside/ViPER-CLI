# ViPER-CLI
Command Line Interface of ViPER Pen Testing tool.

## Running the Command Line Tool

`python Viper.py -u http://yourwebappurl.com/robots.txt?`

## Troubleshooting
------------------
1. I'm getting 'no module named requests' error. What should I do?

Sol:
Requests is not a built in module, so you will have to download it. You can get it here: [Link](https://pypi.python.org/pypi/requests)

### OSX/Linux

Use `$ sudo pip install requests if you have pip installed`

On OSX you can also use sudo easy_install -U requests if you have easy_install installed.

### Windows

Use `> Path\easy_install.exe requests` if you have a windows machine, where easy_install can be found in your Python*\Scripts folder, if it was installed. (Note Path\easy_install.exe is an example, mine is C:\Python32\Scripts\easy_install.exe)

If you don't have easy install and are running on a windows machine, you can get it here: http://www.lfd.uci.edu/~gohlke/pythonlibs/#distribute

If you manually want to add a library to a windows machine, you can download the compressed library, uncompress it, and then place it into the Lib folder of your python path.

### From Source (Universal)

For any missing library, the source is usually available at https://pypi.python.org/pypi/. Then:

On mac osx and windows, after downloading the source zip, uncompress it and from the termiminal/cmd run `python setup.py install` from the uncompressed dir.

# Contributors

`Akhil Mahendra`

`P.S Narayanan`
