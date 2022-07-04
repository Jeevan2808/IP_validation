#function to check IP Address
def check(ip):
    ip = ip.split('.')
    if len(ip) == 4:
        ls = {int(x) for x in ip}
        for i in ls:
            if i >= 0 and i <=255:
                continue
            else:
                return False
    else:
        return False

ip_list = []

#function to enter and store IP Address
def enterIP():
    ip = input("Enter IP: ")
    if check(ip) != False:
        ip_list.append(ip)
    else:
        print("Invalid IP Address")
        return enterIP()

#range function used to take 10 IP addresses
for i in range(1,11):
    enterIP()

#file handing operation
file = open("conversion.txt", "w")

#function for IP Conversion and writing onto file
def convertIP():
    val = 0
    for ip in ip_list:
        deci = []
        bina = []
        octa = []
        hexa = []
        val += 1
        org = ip
        ip = ip.split('.')
        ip = [int(x) for x in ip]
        for i in ip:
            deci.append(str(i))
            bina.append(str(bin(i).replace("0b","")))
            octa.append(str(oct(i).replace("0o","")))
            hexa.append(str(hex(i).replace("0x","")))
        txt = "IP: " + org
        print(txt)
        file.write(txt)
        file.write("\n")
        txt= "Decimal: " + ".".join(deci)
        print(txt)
        file.write(txt)
        file.write("\n")
        txt = "Binary: " + ".".join(bina)
        print(txt)
        file.write(txt)
        file.write("\n")
        txt = "Octal: " + ".".join(octa)
        print(txt)
        file.write(txt)
        file.write("\n")
        txt = "Hexadecimal: " + ".".join(hexa)
        print(txt,"\n")
        file.write(txt)
        file.write("\n")
        file.write("\n")

convertIP()
