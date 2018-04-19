#!/usr/bin/python
# -*- coding: UTF-8 -*-

#pcap文件地址
#filename="test.pcap"
filename=r"E:\路测数据\2018-3-2-WR36-500-66-59-day-road.pcap"
#打开文件
file=open(filename,'rb')

#读取pcap文件头24Byte
pcaphead=file.read(24)

#读取数据包个数
cycle=999999

#临时存储时间戳数据
stamptem=0
#双回波，判断数据已经出现两次
dual=0
#时间间隔为以下时间戳的次数
n545=n546=n547=n548=n549=n550=n551=n552=n553=n554=n555=n556=n557=n558=n559=n560=0

#开始读取数据
while cycle>0:

    #读取Packet包头
    packethead=file.read(16)
    #根据包头信息判断数据长度
    length=packethead[8]+packethead[9]*256+packethead[10]*256*256+packethead[11]*256*256*256
    #读取数据
    packet=file.read(int(length))

    if length==1298:#PointCloud数据
        dual=dual+1
        #隔两个packet取一次时间戳
        if dual%2==0:
            timestamp=packet[1292]+packet[1293]*256+packet[1294]*256*256+packet[1295]*256*256*256
            if timestamp - stamptem == 545:
                n545 = n545 + 1
            elif timestamp - stamptem == 546:
                n546 = n546 + 1
            elif timestamp - stamptem == 547:
                n547 = n547 + 1
            elif timestamp - stamptem == 548:
                n548 = n548 + 1
            elif timestamp - stamptem == 549:
                n549 = n549 + 1
            elif timestamp - stamptem == 550:
                n550 = n550 + 1
            elif timestamp - stamptem == 551:
                n551 = n551 + 1
            elif timestamp - stamptem == 552:
                n552 = n552 + 1
            elif timestamp - stamptem == 553:
                n553 = n553 + 1
            elif timestamp - stamptem == 554:
                n554 = n554 + 1
            elif timestamp - stamptem == 555:
                n555 = n555 + 1
            elif timestamp - stamptem == 556:
                n556 = n556 + 1
            elif timestamp - stamptem == 557:
                n557 = n557 + 1
            elif timestamp - stamptem == 558:
                n558 = n558 + 1
            elif timestamp - stamptem == 559:
                n559 = n559 + 1
            elif timestamp - stamptem == 560:
                n560 = n560 + 1
            stamptem=timestamp
    #elif length==554:#GPS数据

    cycle=cycle-1
print("从545us到560us\n总次数：",int(dual/2),"\n",n545,"\n",n546,"\n",n547,"\n",n548,"\n",n549,"\n",n550,"\n",n551,"\n",n552,"\n",n553,"\n",n554,"\n",n555,"\n",n556,"\n",n557,"\n",n558,"\n",n559,"\n",n560)

