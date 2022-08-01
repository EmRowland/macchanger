
import subprocess
import optparse
import re

def UserInput():
  parse_object =optparse.OptionParser()
  parse_object.add_option("-i", "--Interface", dest="Interface", help="specify the Interface to change")
  parse_object.add_option("-m", "--MacAddress", dest="MacAddress", help="specify the mac address you want to use")
  #(UserInput, arguments) = parse_object.parse_args()
  return parse_object.parse_args()
"""Interface = UserInput.Interface
MacAddress = UserInput.MacAddress"""
def ChecKMac(Interface):
  ifconfig = subprocess.check_output(["ifconfig", Interface])
  NewMac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)
  if NewMac:
    return NewMac.group(0)
  else :
    return None
  
    
  
def ChangeMac(Interface, MacAddress):
  subprocess.call(["ifconfig", Interface, "down"])
  subprocess.call(["ifconfig", Interface, "hw", "ether", MacAddress])
  subprocess.call(["ifconfig", Interface, "up"])
ChangeMac(UserInput.Interface, UserInput.MacAddress)
(UserInput, arguments) = UserInput()

FinalMac = ChecKMac(UserInput.Interface)
if FinalMac == UserInput.MacAddress:
  print(f"Your new MacAddress is :" MacAddress)
else:
  print("request unsuccessful check input")