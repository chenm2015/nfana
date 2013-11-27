from patricia import *
from netaddr import *

l = list()
t = trie(None)
f = open('slash96_group_list', 'r')
f2 = open('detailed_slash96', 'a')
single = True
count = 1

addr = f.readline()[:128]
while addr:
    print str(count) + ':'
    count += 1

    #search a group
    while 1:
        #print addr
        l.append(addr)
        t[addr] = None
        try:
            addr = f.readline()[0:128]
            if addr == '':
                break
            elif addr[0] == 'c':
                f2.write(addr.split()[2] + ':')
                #print 'banana'
                f.readline()
                addr = f.readline()[0:128]
                #try many lengths of prefixes on each group
                for i in range(97, 129):#97~128
                    single = True
                    for item in l:
                        prefix = item[:i]
                        it = t.iter(prefix)
                        it.next()
                        try:
                            it.next()
                            single = False
                            break
                        except:
                            continue

                    if single == False:
                        continue
                    else:
                        f2.write(str(i) + '\n')
                        l = list()
                        t = trie(None)
                        break
            else:
                continue
        except:
            break

f2.close()