## Token Generator

This small tool is for generating tokens for your web accounts


### How to run
First,
- Generate a new key
```bash
./tokenator generate
```
The generated key would be saved in your user directory `.secret_key` file. IMPORTANT: make sure you save your key seperately in some safe place. You do not want someone else to know your secret key :).

Then,
- Generate a token for your account
```bash
./tokenator encrypt --account accountName
```
Your token will be displayed in console

- To verify your key
```bash
./tokenator verify --account accountName --token 123456abcd12345 
```
It will display `True` or `False`

