import pyshark
import re
import os
import time


# 指定ip和协议
def capturePackets(networkInterface, ip, protocol):
    display_filter = 'http'
    print('display_filter: ', display_filter)
    capturePacket = pyshark.LiveCapture(interface=networkInterface, display_filter=display_filter)
    print(111)
    return capturePacket


def getTextList(filename):
    print('save:', filename)
    for pkt in cap:
        try:
            s = str(pkt)
            lines = s.split('\n')
            for line in lines:
                m = re.findall('[\u4e00-\u9fa5]', line)
                m = "".join(m)
                if m != "":
                    save_one_line(m + '\n', filename)
                    print('save successfully', m)
        except:
            print("error......")
            pass
    return text_ls


def save_one_line(input_line, filename):
    path = os.path.join('text_output', filename)
    with open(path, 'a') as f:
        f.write(input_line)


# 是否筛选ip
set_ip = False

# 指定要选择的ip，可以筛选多个
ip_ls = ['127.0.0.1', '127.0.0.0']
display_filter = "http"

if not set_ip:
    pass
else:
    display_filter = " ".join([display_filter, 'and', '('])
    for i, ip in enumerate(ip_ls):
        if i != 0:
            display_filter += " or "
        display_filter = display_filter + ip
    display_filter += ')'

print("Start capturing......")
print(display_filter)

filename = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.txt'

cap = pyshark.LiveCapture(interface='WLAN', display_filter=display_filter)

text_ls = getTextList(filename)
