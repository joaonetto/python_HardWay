from pysnmp.entity.rfc3413.oneliner import cmdgen
import json

SNMP_HOST = '10.151.2.251'
SNMP_PORT = 161
SNMP_COMMUNITY = 'GrupoPython'

# OIDs de getDevice:
getDevice = dict()
getDevice = { 'OID':
                {
                    'jnxPlatform': '1.3.6.1.4.1.2636.3.1.2.0',
                    'jnxSerialNumber': '1.3.6.1.4.1.2636.3.1.3.0',
                    'jnxVersion': '1.3.6.1.2.1.25.6.3.1.2.2',
                    'jnxHostname': '1.3.6.1.2.1.1.5.0'
                }
            }

def myOID(host, port, community, searchOID):
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData(community),
    cmdgen.UdpTransportTarget((host, port)), searchOID
    )

    # Check for errors and print out results
    if errorIndication:
      print(errorIndication)
    else:
      if errorStatus:
        print('%s at %s' % (
          errorStatus.prettyPrint(),
          errorIndex and varBinds[int(errorIndex)-1] or '?'
          )
        )
      else:
        for name, val in varBinds:
          return val.prettyPrint()

def getOIDKey(myOID, myDict):
    for description, OID in myDict['OID'].items():
        if myOID == OID:
            break
    return description

def getPlatformHW(myPlatform):
    myPlatform = myPlatform[len('Juniper '):len(myPlatform)]
    myPlatform = myPlatform[0:myPlatform.find(' ')]
    return myPlatform

def getPlatformSW(myPlatform):
    myPlatform = myPlatform[myPlatform.find('[')+1:len(myPlatform)]
    myPlatform = myPlatform[0:myPlatform.find(']')]
    return myPlatform

for OID in getDevice['OID'].values():
    result = myOID(SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY, OID)
    if getOIDKey(OID, getDevice) == 'jnxPlatform':
        print(f'Junos Platform: {getPlatformHW(result)}')
    elif getOIDKey(OID, getDevice) == 'jnxVersion':
        print(f'Junos Version: {getPlatformSW(result)}')
    else:
        print(result)
