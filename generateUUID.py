#!/usr/bin/python
'''Generate UUID from (reverse) DNS notation. Useful for e.g. macOS
configuration profile generation.

Uses uuid module. NOTE! Generates the same UUID every time from same (reverse) DNS notation!

Usage: ./generateUUID.py my.reverse.dns.notation.identifier

Antti Pettinen
Copyright 2016 Tampere University of Technology


Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

'''
import uuid
import sys

if len(sys.argv) == 2:
    reverseDNS = sys.argv[1]
else:
    print ('Too many or no reverse DNS notation identifiers present')
    sys.exit(1)

if reverseDNS in {"-h","--help"}:
    print('Usage: ./generateUUID.py my.reverse.dns.notation.identifier')
else:
    newUUID = uuid.uuid3(uuid.NAMESPACE_DNS, reverseDNS)
    print reverseDNS + ':', newUUID
