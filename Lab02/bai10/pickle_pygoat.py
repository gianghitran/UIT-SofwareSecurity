import pickletools, base64
token = bytes(input("Enter the token: "), 'utf-8')
data = base64.b64decode(token)

# disassemble the pickle data
pickletools.dis(data)

data = data[0:data.find(b'K')+1] + b'\x01' + data[data.find(b'K')+2:]
print(data)
print(base64.b64encode(data))
