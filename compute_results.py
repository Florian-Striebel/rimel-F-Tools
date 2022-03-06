NB_VAR = 0
NB_ARCH = 0
NB_OS = 0

def set_of_feature():
    global NB_VAR
    fileobj = open('listoffeatures.csv','r')
    list_of_var = set([])
    for line in fileobj:
        line_str = line.strip().split(",")
        if len(line_str)>1 :
            const_str_list = line_str[1].split(";")
            for i in range(len(const_str_list)):
                NB_VAR = NB_VAR + 1
                list_of_var.add(const_str_list[i])
    fileobj.close()
    return list_of_var

ARCHS = ["arch64","arm32","arm","amd","i386","mips","powerpc","risc"]
OS = ["linux","win32","win64","windows","macos","mac_os"]

def main():
    global NB_OS
    global NB_ARCH
    features = set_of_feature()
    print("number of variation :",NB_VAR)
    print("number of constant :",len(features))
    for constant in features : 
        for arch in ARCHS:
            if arch in constant.lower():
                NB_ARCH = NB_ARCH + 1
                
        for os in OS :
            if arch in constant.lower():
                NB_OS = NB_OS + 1
    print("number of architecture :",NB_ARCH)
    print("number of os :", NB_OS)
main()
