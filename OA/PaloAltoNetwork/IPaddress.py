'''
Write a method that increments an IP address. The IP address is given as a string, and returned as a string.

Example input and output:
incr_ip("192.168.1.1") => "192.168.1.2"
incr_ip("192.168.1.255") => "192.168.2.0"
incr_ip("192.168.255.255") => "192.169.0.0"
incr_ip("255.168.255.10") => "255.168.255.11"


'''



def incrementIP(s):
    iparr = (s.split('.'))
    iparr = list(map(int, iparr))
    i = len(iparr) - 1 
    while i > 0:
        if i == 3:
            if iparr[i] == 255:
                iparr[i] = 0
                if iparr[i-1] == 255:
                    iparr[i-1] = 0
                    if iparr[i-1] == 0: 
                        iparr[i-2] += 1
                else:
                    iparr[i-1] += 1
            else: 
                iparr[i] += 1 
        i -= 1
    return (str(iparr).replace(",", ".").replace("'", ""))[1:-1]


print(incrementIP("192.168.255.255")) #  "192.169.0.0"
print(incrementIP("192.168.1.255")) # "192.168.2.0"
print(incrementIP("192.168.1.1")) #  "192.168.1.2"
print(incrementIP("255.168.255.10"))  # "255.168.255.11"



# incr_ip("192.168.1.1") => "192.168.1.2"
# incr_ip("192.168.1.255") => "192.168.2.0"
# incr_ip("192.168.255.255") => "192.169.0.0"
# incr_ip("255.168.255.10") => "255.168.255.11"
