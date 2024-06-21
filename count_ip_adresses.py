'''
Count IP Addresses

Implement a function that receives two IPv4 addresses, 
and returns the number of addresses between them 
(including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. 
The last address will always be greater than the first one.

Examples:
* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246
'''



def ips_between(start, end):
    start = [int(x) for x in start.split('.')]
    end = [int(x) for x in end.split('.')]
    
    num_s = start[3] + start[2]*256 +start[1]*256**2 + start[0]*256**3
    num_e = end[3] + end[2]*256 + end[1]*256**2 + end[0]*256**3

    return abs(num_e - num_s)


print(ips_between("10.0.0.0", "10.0.0.50"))
print(ips_between("20.0.0.10", "20.0.1.0"))
print(ips_between("4.73.119.147", "4.74.140.180")) # Expecting: 70945