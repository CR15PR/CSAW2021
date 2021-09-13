The objetive of this challenge is to find the message Veronica sent via an online contact us form to one of her clients. You are given a .pcap file and a TLS (Pre)-Master-Secret log that contains the TLS keys needed to decrypt some of the content.

Importing the keys can be done by going to wireshark preferences, protocols, then TLS. Upload the file; then enable the `Reassemble out-of-order segments` option under the TCP.

Wireshark is now configured to decrypt TLS data. 

Our method of attack was to filter by all streams and exclude them manually. To reduce the starting size we filtered by `ip.src == 192.168.198.135` since this was the private IP that had the most outbound connections. We made the assumption this is Veronica's workstation. Our next assumption was this will be encrypted data so either HTTP2 or TLS data so we filtered for these first. Finally we assumed this would be accompished through a POST action or some sort of application transaction.

By manually inspection and excluding streams we eventually find the following: 
