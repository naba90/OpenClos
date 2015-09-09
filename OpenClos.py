#!/usr/bin/python2.7
import re

# Function To extract values
def find(path,content):
    find = open (path,'r').read()
    split_find = find.split('\n')
    filter_find = filter(lambda find: content in find, split_find)
    value = map(lambda find: re.split('>|<', find)[2].strip(), filter_find)
    return value



BGP_L1_add = '/home/BGP_LLDP/BGP_L1.txt'
BGP_L2_add = '/home/BGP_LLDP/BGP_L2.txt'
BGP_L3_add = '/home/BGP_LLDP/BGP_L3.txt'
BGP_S1_add = '/home/BGP_LLDP/BGP_S1.txt'
BGP_S2_add = '/home/BGP_LLDP/BGP_S2.txt'

LLDP_L1_add = '/home/BGP_LLDP/LLDP_L1.txt'
LLDP_L2_add = '/home/BGP_LLDP/LLDP_L2.txt'
LLDP_L3_add = '/home/BGP_LLDP/LLDP_L3.txt'
LLDP_S1_add = '/home/BGP_LLDP/LLDP_S1.txt'
LLDP_S2_add = '/home/BGP_LLDP/LLDP_S2.txt'

p_as = 'peer-as'
p_ad = 'peer-address'

p_id = 'lldp-local-port-id'
rc_id = 'lldp-remote-chassis-id>'
rp_d = 'lldp-remote-port-description'
rs_n = 'lldp-remote-system-name'

# Show BGP details

print "             Statistics of show bgp  \n"

print  "L1 "+ p_ad +':' + p_as +','+ p_ad + ':' + p_as
print dict(zip(find(BGP_L1_add, p_ad),find(BGP_L1_add, p_as)))

print  "\n"+"L2 " + p_ad +':' + p_as +','+ p_ad + ':' + p_as
print  dict(zip(find(BGP_L2_add, p_ad),find(BGP_L1_add, p_as)))

print  "\n"+"L3 " + p_ad +':' + p_as +', '+ p_ad + ':' + p_as
print  dict(zip(find(BGP_L3_add, p_ad),find(BGP_L3_add, p_as)))

print  "\n"+"S1 " + p_ad +':' + p_as +','+ p_ad + ':' + p_as +', '+p_ad + ':' + p_as
print  dict(zip(find(BGP_S1_add, p_ad),find(BGP_S1_add, p_as)))


print "\n"+"S2 " + p_ad + ':' + p_as +','+ p_ad + ':' + p_as +',  '+p_ad + ':' + p_as
print dict(zip(find(BGP_S2_add, p_ad),find(BGP_S1_add, p_as)))


# Show LLDP details

print "        \n \n   Statistics of show llpd \n"

# Leaf01
LLDP_pID_L1 = find(LLDP_L1_add, p_id)
#print LLDP_pID_L1

LLDP_rcID_L1 = find(LLDP_L1_add, rc_id)
#print LLDP_rcID_L1

LLDP_rpD_L1 = find(LLDP_L1_add, rp_d)
#print LLDP_rpD_L1

LLPD_rsN_L1 = find(LLDP_L1_add, rs_n)
#print LLPD_rsN_L1

#LLDP_L1Details = (LLDP_pID_L1 + LLDP_rcID_L1 + LLDP_rpD_L1 + LLPD_rsN_L1)
#print LLDP_L1Details

LLDP_L1Details_0 = (LLDP_pID_L1[0] +' '+ LLDP_rcID_L1[0] +' '+ LLDP_rpD_L1[0] +' '+ LLPD_rsN_L1[0]).split()
LLDP_L1Details_1 = (LLDP_pID_L1[1] +' '+ LLDP_rcID_L1[1] +' '+ LLDP_rpD_L1[1] +' '+ LLPD_rsN_L1[1]).split()
print "Leaf 01"
print "  port-id,    remote-chasis-id , remote-prt-id,  remote-system-name"
print LLDP_L1Details_0
print LLDP_L1Details_1

#Leaf02
LLDP_L2Details_0 = (find(LLDP_L2_add, p_id)[0] +' '+ find(LLDP_L2_add, rc_id)[0] +' '+ find(LLDP_L2_add, rp_d)[0] +' '+ find(LLDP_L2_add, rs_n)[0]).split()
LLDP_L2Details_1 = (find(LLDP_L2_add, p_id)[1] +' '+ find(LLDP_L2_add, rc_id)[1] +' '+ find(LLDP_L2_add, rp_d)[1] +' '+ find(LLDP_L2_add, rs_n)[1]).split()
print "\nLeaf 02"
print "  port-id,    remote-chasis-id , remote-prt-id,  remote-system-name"
print LLDP_L2Details_0
print LLDP_L2Details_1

#Leaf03
LLDP_L3Details_0 = (find(LLDP_L3_add, p_id)[0] +' '+ find(LLDP_L3_add, rc_id)[0] +' '+ find(LLDP_L3_add, rp_d)[0] +' '+ find(LLDP_L3_add, rs_n)[0]).split()
LLDP_L3Details_1 = (find(LLDP_L3_add, p_id)[1] +' '+ find(LLDP_L3_add, rc_id)[1] +' '+ find(LLDP_L3_add, rp_d)[1] +' '+ find(LLDP_L3_add, rs_n)[1]).split()
print "\nLeaf 03"
print "  port-id,    remote-chasis-id , remote-prt-id,  remote-system-name"
print LLDP_L3Details_0
print LLDP_L3Details_1

#Spine01
LLDP_S1Details_0 = (find(LLDP_S1_add, p_id)[0] +' '+ find(LLDP_S1_add, rc_id)[0] +' '+ find(LLDP_S1_add, rp_d)[0] +' '+ find(LLDP_S1_add, rs_n)[0]).split()
LLDP_S1Details_1 = (find(LLDP_S1_add, p_id)[1] +' '+ find(LLDP_S1_add, rc_id)[1] +' '+ find(LLDP_S1_add, rp_d)[1] +' '+ find(LLDP_S1_add, rs_n)[1]).split()
LLDP_S1Details_2 = (find(LLDP_S1_add, p_id)[2] +' '+ find(LLDP_S1_add, rc_id)[2] +' '+ find(LLDP_S1_add, rp_d)[2] +' '+ find(LLDP_S1_add, rs_n)[2]).split()
print "\nSpine 01"
print "  port-id,    remote-chasis-id , remote-prt-id,  remote-system-name"
print LLDP_S1Details_0
print LLDP_S1Details_1
print LLDP_S1Details_2

#Spine02
LLDP_S2Details_0 = (find(LLDP_S2_add, p_id)[0] +' '+ find(LLDP_S2_add, rc_id)[0] +' '+ find(LLDP_S2_add, rp_d)[0] +' '+ find(LLDP_S2_add, rs_n)[0]).split()
LLDP_S2Details_1 = (find(LLDP_S2_add, p_id)[1] +' '+ find(LLDP_S2_add, rc_id)[1] +' '+ find(LLDP_S2_add, rp_d)[1] +' '+ find(LLDP_S2_add, rs_n)[1]).split()
LLDP_S2Details_2 = (find(LLDP_S2_add, p_id)[2] +' '+ find(LLDP_S2_add, rc_id)[2] +' '+ find(LLDP_S2_add, rp_d)[2] +' '+ find(LLDP_S2_add, rs_n)[2]).split()
print "\nSpine 02"
print "  port-id,    remote-chasis-id , remote-prt-id,  remote-system-name"
print LLDP_S2Details_0
print LLDP_S2Details_1
print LLDP_S2Details_2

# Ports connection between Leaf 1 and Spine 1

while 'clos-spine-01' in LLDP_L1Details_0 or 'clos-spine-01' in LLDP_L1Details_1:

        if (find(LLDP_L1_add, p_id)[0]) == (find(LLDP_S1_add, rp_d)[2])  and \
           (find(LLDP_L1_add, rp_d)[0]) == ((find(LLDP_S1_add, p_id)[2])):
            print "\nLeaf 01 and Spine 01 are connected"
            break
        elif (find(LLDP_L1_add, p_id)[1]) == (find(LLDP_S1_add, rp_d)[2])  and \
             (find(LLDP_L1_add, rp_d)[1]) == ((find(LLDP_S1_add, p_id)[2])):
            print "\nLeaf 01 and Spine 01 are Connected"
            break
        else:
            print "\nPorts Disconnected! \nPlease check connection between Leaf 01 and Spine 01 "
            break

# Ports connection between Leaf 1 and Spine 2

while 'clos-spine-02' in LLDP_L1Details_0 or 'clos-spine-02' in LLDP_L1Details_1:

        if (find(LLDP_L1_add, p_id)[0]) == (find(LLDP_S2_add, rp_d)[2])  and \
           (find(LLDP_L1_add, rp_d)[0]) == ((find(LLDP_S2_add, p_id)[2])):
            print "\nLeaf 01 and Spine 02 are connected"
            break
        elif (find(LLDP_L1_add, p_id)[1]) == (find(LLDP_S2_add, rp_d)[2])  and \
             (find(LLDP_L1_add, rp_d)[1]) == ((find(LLDP_S2_add, p_id)[2])):
            print "\nLeaf 01 and Spine 02 are connected"
            break
        else:
            print "\n Disconnected! \nPlease check connection between Leaf 01 and Spine 02 "
            break

# Ports connection between Leaf 2 and Spine 1

while 'clos-spine-01' in LLDP_L2Details_0 or 'clos-spine-01' in LLDP_L2Details_1:

        if (find(LLDP_L2_add, p_id)[0]) == (find(LLDP_S1_add, rp_d)[0])  and \
           (find(LLDP_L2_add, rp_d)[0]) == ((find(LLDP_S1_add, p_id)[0])):
            print "\nLeaf 02 and Spine 01 are connected"
            break
        elif (find(LLDP_L2_add, p_id)[1]) == (find(LLDP_S1_add, rp_d)[0])  and \
             (find(LLDP_L2_add, rp_d)[1]) == ((find(LLDP_S1_add, p_id)[0])):
            print "\nLeaf 02 and Spine 01 are connected"
            break
        else:
            print "\n Ports Disconnected! \nPlease check connection between Leaf 02 and Spine 01 "
            break

# Ports connection between Leaf 2 and Spine 2

while 'clos-spine-02' in LLDP_L2Details_0 or 'clos-spine-02' in LLDP_L2Details_1:

        if (find(LLDP_L2_add, p_id)[0]) == (find(LLDP_S2_add, rp_d)[0])  and \
           (find(LLDP_L2_add, rp_d)[0]) == ((find(LLDP_S2_add, p_id)[0])):
            print "\nLeaf 02 and Spine 02 are connected"
            break
        elif (find(LLDP_L2_add, p_id)[1]) == (find(LLDP_S2_add, rp_d)[0])  and \
             (find(LLDP_L2_add, rp_d)[1]) == ((find(LLDP_S2_add, p_id)[0])):
            print "\nLeaf 02 and Spine 02 are connected"
            break
        else:
            print "\n Ports Disconnected! \nPlease check connection between Leaf 02 and Spine 02"
            break

# Ports connection between Leaf 3 and Spine 1

while 'clos-spine-01' in LLDP_L3Details_0 or 'clos-spine-01' in LLDP_L3Details_1:

        if (find(LLDP_L3_add, p_id)[0]) == (find(LLDP_S1_add, rp_d)[1])  and \
           (find(LLDP_L3_add, rp_d)[0]) == ((find(LLDP_S1_add, p_id)[1])):
            print "\nLeaf 03 and Spine 01 are connected"
            break
        elif (find(LLDP_L3_add, p_id)[1]) == (find(LLDP_S1_add, rp_d)[1])  and \
             (find(LLDP_L3_add, rp_d)[1]) == ((find(LLDP_S1_add, p_id)[1])):
            print "\nLeaf 03 and Spine 01 are connected"
            break
        else:
            print "\n Ports Disconnected! \nPlease check connection between Leaf 03 and Spine 01"
            break

# Ports connection between Leaf 3 and Spine 2

while 'clos-spine-02' in LLDP_L3Details_0 or 'clos-spine-02' in LLDP_L3Details_1:
   
        if (find(LLDP_L3_add, p_id)[0]) == (find(LLDP_S2_add, rp_d)[1])  and \
           (find(LLDP_L3_add, rp_d)[0]) == ((find(LLDP_S2_add, p_id)[1])):
            print "\nLeaf 03 and Spine 02 are connected"
            break
        elif (find(LLDP_L3_add, p_id)[1]) == (find(LLDP_S2_add, rp_d)[1])  and \
             (find(LLDP_L3_add, rp_d)[1]) == ((find(LLDP_S2_add, p_id)[1])):
            print "\nLeaf 03 and Spine 02 are connected" 
            break
        else:
            print "\nPorts Disconnected! \nPlease check connection between Leaf 03 and Spine 02 "
            break
