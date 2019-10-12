## Token Generator

This small tool is for generating tokens for your web accounts


### How to run
First,
- Generate a new key
```bash
python3 main.py generate
```
The generated key would be saved in `secret_key` file. IMPORTANT: make sure you save your key seperately in some safe place. You do not want someone else to know your secret key :).

Then,
- Generate a token for your account
```bash
python3 main.py encrypt --account accountName
```
Your token will be displayed in console

- To verify your key
```bash
python3 main.py verify --account accountName --token 123456abcd12345 
```
It will display `True` or `False`

