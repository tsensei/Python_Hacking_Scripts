#!/usr/bin/env python

import subprocess
import optparse
import re

# Parser input options and arguments

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
	parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specify an interface, use --help for more info.")
	elif not options.new_mac:
		parser.error("[-] Please specify a new mac, use --help for more info.")
	else:
		return options

# Changes MAC address using system calls
	
def change_mac(interface, new_mac):
	print("[+] Changing MAC address for " + interface + " to " + new_mac)

	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

# Returns the current MAC address

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
	current_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
	if current_mac:
		return current_mac.group(0)
	else:
		print("[-] Could not read MAC address")
		
		
		
# Main Functionalities

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("[+] Current MAC : " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
	print("[+] MAC address was successfully changed to " + current_mac)
else:
	print("[-] MAC address could not be changed")



