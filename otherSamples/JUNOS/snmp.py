from pysnmp.entity.rfc3413.oneliner import cmdgen
import time

SNMP_HOST = '10.151.2.251'
SNMP_PORT = 161
SNMP_COMMUNITY = 'GrupoPython'

def myOID(host, port, community, searchOID):
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData(SNMP_COMMUNITY),
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
          #print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
          #print(f"{name.prettyPrint()}")
          #print(f"{val.prettyPrint()}")
          return val.prettyPrint()

#myResult = myOID(SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY, "1.3.6.1.2.1.1.5.0")
print(f'         Modelo: {myOID(SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY, "1.3.6.1.4.1.2636.3.40.1.4.1.1.1.8.0")}')
print(f'Número de Série: {myOID(SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY, "1.3.6.1.4.1.2636.3.1.3.0")}')
print(f'Versão do JUNOS: {myOID(SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY, "1.3.6.1.4.1.2636.3.40.1.4.1.1.1.5.0")}')
print(f'       Hostname: {myOID(SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY, "1.3.6.1.2.1.1.5.0")}')


"""
Exemplo de Utilizacao SNMP:
snmpbulkget -v 2c -c GrupoPython 10.151.2.251 1.3.6

             Modelo: EX2200-48T-4G - jnxVirtualChassisMemberModel.0 - 1.3.6.1.4.1.2636.3.40.1.4.1.1.1.8.0
    Número de Série: CU0213394777  - jnxVirtualChassisMemberSerialnumber.0 - jnxBoxSerialNo.0 - 1.3.6.1.4.1.2636.3.1.3.0
    Versão do JUNOS: 12.3R12-S7    - jnxVirtualChassisMemberSWVersion.0 - 1.3.6.1.4.1.2636.3.40.1.4.1.1.1.5.0
           Hostname: ACT-SW-03-CPS - sysName.0 - 1.3.6.1.2.1.1.5.0
Tipo de Dispositivo: SWITCH        - jnxBoxDescr.0
"""
