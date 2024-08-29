# Method 1

Open pcap in Wireshark, add filter `ip.dst == 8.8.8.8`. Click File > Export Packet Dissections > Export as CSV

Write a python script [solve.py](solve.py) to process output

# Method 2

Follow above steps to export filtered packets as CSV

Use Microsoft excel to import CSV.

Select the `Info` column, then click Data > Text to Columns > Use space to separate (should be default option)

Copy paste the DNS query URLs into another sheet for easier processing

Use search and replace to replace all ".welc0mectf.gr3yh4ts.com" with nothing.

Join all the cells together. This can be done by the formula `=CONCAT(...)`

Base64 decode and you should get the full text

Flag: grey{dn5_3xf11724710n_15_c001}