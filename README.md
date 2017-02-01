# Encryptpy
Simple example of file encryption using a unique symmetric key for each file
It uses the cryptography standard library (in particular Fernet's method) in order to encrypt your files. Each file is encrypted with a single symmetric key, and its information is stored into a token.txt. It's important to keep the token.txt in a safe place, because it's the only way to decrypt your data. 

Example of Encrypting:./encryptpy 1 fileinput.txt fileoutput.txt

Example of Decrypting:./encryptpy 0 fileencrypted.txt cleartext.txt 

When you encrypt a file, it's asked to you if you would like to remove original clear text file. It's up to you to choose. If you decide to keep clear text, it's advised to keep it separated from encrypted file. 
