#!/usr/bin/python
# Muhammad Adeel | Founder UrduSecurity (c) 2014
# Just Check remaining days of a ssl cert ;)

import ssl, OpenSSL, socket, sys
from datetime import datetime

print '\n######################################################\n'
print ' Muhammad Adeel | Founder UrduSecurity (c) 2014'
print '######################################################\n'

host = raw_input('Host: ')
port = input('Port: ')

try:
  crt = ssl.get_server_certificate((host, port))
  x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, crt)
  crt_end_date = x509.get_notAfter()[:-1]
except socket.error, e:
  print e
  sys.exit(1)

end_date = datetime.strptime(crt_end_date, "%Y%m%d%H%M%S")
now_date = datetime.now()
delta = (end_date - now_date)/24/3600
days = delta.seconds
print '\n[+] Remaining Days: {0}'.format(days)
