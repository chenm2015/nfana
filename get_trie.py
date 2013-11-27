from patricia import *
#import ipaddr
from netaddr import *

#print ipaddr.IPv4Address('192.168.0.1')

#a6 = IPAddress('2001:da8::1')

#print hex(a6)
#print a6.bin

#p6 = IPNetwork('2002:55::/32')
#print p6.netmask

#t = trie('root', key='value', king = 'kong')
#print '' in t
#print t['king']
#print len(t)
t = trie(None)
l = list()
f2 = open('result_trie', 'a')

for i in range(1, 10):
    f = open('/media/doc/Data/cernet2-10min/netflow2011-10-19-15_0' + str(i) + '.txt', 'r')

    print 'file No.' + str(i)
    
    s_addr = IPAddress(f.readline().split()[0]).bits()
    s_addr = s_addr.replace(':', '')
    #print s_addr + '/' + str(len(s_addr))
    while 1:
        
        #try:
        #    l.index(s_addr)
        #except:
        #    l.append(s_addr)
        #    if len(l)%10000 == 0:
        #        print 'list length = ' + str(len(l))
        t[s_addr] = None     

        try:
            s_addr = IPAddress(f.readline().split()[0]).bits()
            s_addr = s_addr.replace(':', '')
            #print s_addr + '/' + str(len(s_addr))
        except:
            break

ite = t.iter('')
ite.next()

while 1:
    try:
        f2.write(ite.next() + '\n')
    except:
        break

f2.close()
