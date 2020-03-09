#!/usr/bin/python
import pyotp
import pyperclip
from sys import argv
#author: sudeep
#this script generates an OTP for following web portals
try:
 if argv[1] == "adc":
  vpn = pyotp.TOTP('auth code removed intentionally')
  v = vpn.now()
  pyperclip.copy(str(v))
  print 'ADC VPN: ',vpn.now()
 elif argv[1] == "ny":
  vpn2 = pyotp.TOTP('auth code removed intentionally')
  pyperclip.copy(vpn2.now())
  print 'NY VPN: ',vpn2.now()
 elif argv[1] == "aws":
  aws = pyotp.TOTP('auth code removed intentionally')
  pyperclip.copy(aws.now())
  print 'AWS: ',aws.now()
 elif argv[1] == "sso":
  sso = pyotp.TOTP('auth code removed intentionally')
  pyperclip.copy(sso.now())
  print 'SSO: ',sso.now()
  print " "
 elif argv[1] == "aka":
  aka = pyotp.TOTP('auth code removed intentionally')
  pyperclip.copy(aka.now())
  print 'AKAMAI:',aka.now()
 elif argv[1] == "zeta":
  z = pyotp.TOTP('auth code removed intentionally')
  pyperclip.copy(z)
  print 'Zeta :',z
 elif argv[1] == "gmail":
  g = pyotp.TOTP('auth code removed intentionally')
  pyperclip.copy(g)
  print 'GMAIL : ',g
 else:
  print 'enter argument either of 1 adc | ny | aws | sso | aka | zeta'
except Exception as e:
 print "Some Error",e
