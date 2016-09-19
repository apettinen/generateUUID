#!/usr/bin/python
'''Generate UUID from (reverse) DNS notation. Useful for e.g. macOS
configuration profile generation.

Uses uuid module. NOTE! Generates the same UUID every time from same (reverse) DNS notation!

Usage: ./generateUUID.py my.reverse.dns.notation.identifier

Antti Pettinen
Copyright: Tampere University of Technology 2016
License: Apache 2.0
'''
import uuid
import sys

if len(sys.argv) == 2:
    reverseDNS = sys.argv[1]
else:
    print ('Too many or no reverse DNS notation identifiers present')
    sys.exit(1)

newUUID = uuid.uuid3(uuid.NAMESPACE_DNS, reverseDNS)
print reverseDNS + ':', newUUID
