import os

path = r"C:\Users\Administrator\Desktop\分布式系统"

# 字节bytes转化kb\m\g
def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"

    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%fG" % (G)
        else:
            return "%fM" % (M)
    else:
        return "%fkb" % (kb)


def getDocSize(path):

    try:
        size = os.path.getsize(path)
        new_size = formatSize(size)
        num = float(new_size.split('kb')[0])

        return num

    except Exception as err:
        print(err)

def get_txt(path):
    files = os.walk(path)
    for item in files:
       for i in item[2]:
           filename = os.path.join(path,i)
           size = getDocSize(filename)
           if size <= 1.0:
              os.remove(filename)


if __name__ == '__main__':

    get_txt(path)
