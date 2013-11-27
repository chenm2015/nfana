from patricia import *
from netaddr import *

for ii in range(96, 121):
    t = trie(True)
    l = list()
    count_l = list()
    f = open('result_trie', 'r')
    f2 = open('group_list/slash' + str(ii) + '_group_list', 'a')
    #store source addresses in a trie
    s_addr = f.readline()[:128]
    while s_addr:
        l.append(s_addr)
        t[s_addr] = False
        try:
            s_addr = f.readline()[0:128]
        except:
            break;

    #check if continuous addresses exist 
    count = 1
    interesting = 0
    sum_addr = 0
    for addr in l:
        if t[addr] == False:
            t[addr] = True
            prefix = addr[:ii]
            it = t.iter(prefix)
            it.next()
            while 1:
                try:
                    s = it.next()
                    f2.write(s + '\n')
                    count += 1
                    sum_addr += 1
                    t[s] = True
                except:
                    if count > 1:
                        count_l.append(count)
                        interesting += 1
                        f2.write(addr + '\n')
                        sum_addr += 1
                        f2.write('count = ' + str(count) + '\n')
                        f2.write('######################' + prefix + '###########\n')
                        count = 1
                        break
                    break

    f2.write('groups number: ' + str(interesting) + '\n')
    f2.write('address number: ' + str(sum_addr) + '(' +
            str((float(sum_addr)/float(502513))*100) + '%)\n')
    f2.write('===================================================================================\n')
    f2.write('statistics:\n')

    count_l.sort()
    f2.write(str(count_l[-20:]) + '\n')
    for i in range(2, 800):
        if count_l.count(i) > 0:
            f2.write(str(i) + ' elements: ' + str(count_l.count(i)) + '\n')

    f.close()
    f2.close()
