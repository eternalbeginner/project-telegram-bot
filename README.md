# PROGRESS Bot

This repository is a repository for storying python-based [Telegram][url-telegram] chatbot applications using the [Pyrogram][url-pyrogram]. We created this chatbot with the aim of making it easier for us to take care of simple things related to the [Telegram][url-telegram] application.

## Installation 🍀

The installation process of this application is quite simple. Starting from activating the virtual environment and then installing some required dependencies. Here are the step-by-step instructions.

#### Clone the repository

Before doing the installation, clonse the repository first to continue to the steps below.

```sh
git clone https://github.com/eternalbeginner/python-progress-bot.git
```

#### Activate the virtual environment

First-thing-first is to activate the python virtual environment to save the dependencies locally in the venv directory. But, before activating let's first install the virtual environment.

```sh
python3 -m venv ./venv
```

After that proceed with activating virtual environment with the command below

```sh
source venv/bin/activate # for linux
.\\venv\\scripts\\Activate # for windows
```

#### Installing the necessary dependencies

Then after activation, the next step is to install dependencies. This step is quite simple because it only requires one command to install it.

```sh
pip install --no-cache-dir -r requirements.txt
```

## Usage 🚀

The use of this application is very simple because you only need to run or execute one file. That is, we just need to run the `main.py` file with the command below.

```sh
python3 main.py
```

[url-telegram]: https://telegram.org
[url-pyrogram]: https://docs.pyrogram.org
