# Python project template

## File structure

    .
    ├── README.md
    ├── source
    |   ├── app.py
    |   ├── setup.py
    |   ├── requirements.txt
    |   ├── modules
    |   ├── config
    |   |    └── logging.yml
    |   └── logs
    └── .gitignore

## Functionality included

- Logging

## Use the template

    wget https://github.com/adagio/pytemplate/archive/v0.1.tar.gz
    mv v0.1.tar.gz template.tar.gz
    tar xzf template.tar.gz
    cp -r template myproject
    cd myproject

## Work inside source folder

- Enter `cd source`

## Run application

- Do `python app.py`

## Use venv if python3 is not default

- Do `python3 -m venv myenv`
- Do `source myenv/bin/activate`