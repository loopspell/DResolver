#!/usr/bin/python

#Author: loopspell (twitter.com/loopspell)

import dns.resolver
import sys

if len(sys.argv) < 3:
		print "\nUsage: python " + sys.argv[0] + " <ip_list> <output_file>"
		print "Example: python DResolver.py ip_list.txt output.txt"
		sys.exit()

myResolver = dns.resolver.Resolver()
num_readlines = sum(1 for line in open(sys.argv[1]))
read_file = open(sys.argv[1], "r")

write_file = open(sys.argv[2], "w")
counter = 1
for line in read_file:
	org_ip = line.strip()

	ip = org_ip.split(".")
	ip =  ".".join(ip[::-1])
	sys.stdout.write("\r[!] DNS Resolve Status - [ "+str(counter)+"/"+str(num_readlines)+" ]")
	sys.stdout.flush()
	counter += 1 
	try:
		myAnswers = myResolver.query(ip+".in-addr.arpa", "PTR")
		write_file.write("\n"+org_ip+"\n")
		for rdata in myAnswers:
			write_file.write(str(rdata)[:-1]+"\n")
	except KeyboardInterrupt:
		print "\nExiting\n"
		exit(0)
	except:
		continue
print "\n[+] DNS Resolve DONE [+]\n"
exit(0)