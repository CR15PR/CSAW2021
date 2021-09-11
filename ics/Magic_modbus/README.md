# The Magic Modbus

![](question.png)

1) view the pcap file in wireshark
- ![](pcap.png)

2) right click a packet > Follow > TCP Steam
- ![](message.png)
- interesting, it's a message.  Changing the TCP Stream to stream 2 reveals the flag

3) ![](flag.png)
- `flag{Ms_Fr1ZZL3_W0ULD_b3_s0_Pr0UD}`
