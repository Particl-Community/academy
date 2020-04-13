# academy

The Particl Academy documentation is based on Read the Docs. Content is written in RestfulText.

## Local setup

1. Install python 3.x
2. Have sublime-text
3. Have sublime-merge
4. Clone this repository

### Install Python 3.x MacOS

##### Install Homebrew 
Homebrew is a powerful software package manager for the commandline.

```
xcode-select --install
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

##### Set Path for Homebrew 

Once you've installed Homebrew, insert the Homebrew directory at the top of your PATH environment variable. Copy this line to the terminal and hit enter.

```
echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.profile
```

##### Install Python 

```
brew install python
brew link python
```

##### Check versions
For python it should be 3.7.x and for pip 20.x pointing to the same python version. 
```
python --version
pip -V
```

If this is not the case set an alias.
```
echo 'alias python=python3' >> ~/.bash_aliases
echo 'alias pip=pip3' >> ~/.bash_aliases
source ~/.bash_aliases
```


##### Install sphinx and rtd theme locally
Python package manager should do the job. 

```
pip install sphinx sphinx-rtd-theme sphinx-copybutton
```

##### clone this repository
Business as usual. If no git is installed use brew to do so: ```brew install git```

```
git clone https://github.com/Particl-Community/academy.git
```

### Install sublime-text & submlime-merge

Go to https://www.sublimetext.com/ and https://www.sublimemerge.com and install them both

## Render a local copy
The local copy is build into the ```_build``` directory.
```
rm -Rf _build && make html
```