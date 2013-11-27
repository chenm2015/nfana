l = list()
f2 = open('output', 'a')

for i in range(1,10):
    f = open('/media/doc/Data/cernet2-10min/netflow2011-10-19-15_0' + str(i) + '.txt', 'r')

    print 'file No.' + str(i)
    
    s_addr = f.readline().split()[0]
    while 1:
        
        try:
            l.index(s_addr)
        except:
            l.append(s_addr)
            if len(l)%10000 == 0:
                print 'list length = ' + str(len(l))
                
        try:
            s_addr = f.readline().split()[0]
        except:
            break

for item in l:
    f2.write(item + '\n')    

f2.close()
