import click
from hashlib import blake2b
from hmac import compare_digest
from cryptography.fernet import Fernet

@click.command()
@click.argument('action')
@click.option('--account')
@click.option('--token')
def main(action, account, token):
	if action == 'generate':
		key = generate_key()
		write_key_to_file(key.decode('utf-8'))
		click.echo(key)
	
	if action == 'encrypt':
		key = get_key_from_file().encode()
		
		password = encrypt(key, account)
		click.echo(password)

	if action == 'verify':
		key = get_key_from_file().encode()
		
		original = verify(key, account, token.encode())
		click.echo(original)

def generate_key():
	return Fernet.generate_key()

def get_key_from_file():
	with open('secret_key', 'r') as file:
		key = file.readline()
	return key

def write_key_to_file(key):
	with open('secret_key', 'w') as file:
		file.write(key)
	
def encrypt(key,account):
	h = blake2b(key=key, digest_size=16)
	h.update(account.encode())
	return h.hexdigest().encode('utf-8')

def verify(key,account, token):
	good_token = encrypt(key, account)
	return compare_digest(token, good_token)

if __name__ == '__main__':
	main()
