import json

with open('output_vlan.json') as f:
    myVlan = json.load(f)

with open('output.json') as f:
    myDictionary = json.load(f)

def getVlanConnected(myInterface, vlanConnected):
    if '*' in myInterface:
        vlanConnected = True
        myInterface = myInterface[0:myInterface.find('.')]
    else:
        vlanConnected = False
        myInterface = myInterface[0:myInterface.find('.')]
    return myInterface, vlanConnected

interfacePHY = str()
connectedVLAN = bool()

contTemp1 = myDictionary.copy()
for myHardware in contTemp1['hardware']:
    contTemp1['hardware'][myHardware].update({'vlans': {'vlan_id': {},'vlan_name': {}}})
    for vlanID in myVlan:
        contTemp1['hardware'][myHardware]['vlans']['vlan_id'].update(
            {vlanID:
                {
                    'vlan_name': myVlan[vlanID]['vlan_name'],
                    'vlan_status': myVlan[vlanID]['vlan_status'],
                    'vlan_owner': myVlan[vlanID]['vlan_owner'],
                    'vlan_createTime': myVlan[vlanID]['vlan_createTime'],
                    'vlan_protocolPort': myVlan[vlanID]['vlan_protocolPort'],
                    'vlan_description': myVlan[vlanID]['vlan_description'],
                    'vlan_macAgingTime': myVlan[vlanID]['vlan_macAgingTime']
                }
            }
        )
        contTemp1['hardware'][myHardware]['vlans']['vlan_name'].update(
            {myVlan[vlanID]['vlan_name']:
                {
                    'vlan_id': vlanID
                }
            }
        )
        if myVlan[vlanID]['vlan_interfaceMember'] is not None:
            if isinstance(myVlan[vlanID]['vlan_interfaceMember'], str) == True:
                interfacePHY, connectedVLAN = getVlanConnected(myVlan[vlanID]['vlan_interfaceMember'], connectedVLAN)
                contTemp1['hardware'][myHardware]['vlans']['vlan_id'][vlanID].update(
                    {interfacePHY:
                        {
                            'tagnessMember': myVlan[vlanID]['vlan_tagnessMember'],
                            'portModeMember': myVlan[vlanID]['vlan_portModeMember'],
                            'connectedVlan': connectedVLAN
                        }
                    }
                )
            else:
                for interfaceMember in range(0,len(myVlan[vlanID]['vlan_interfaceMember'])):
                    interfacePHY, connectedVLAN = getVlanConnected(myVlan[vlanID]['vlan_interfaceMember'][interfaceMember], connectedVLAN)
                    contTemp1['hardware'][myHardware]['vlans']['vlan_id'][vlanID].update(
                        {interfacePHY:
                            {
                                'tagnessMember': myVlan[vlanID]['vlan_tagnessMember'][interfaceMember],
                                'portModeMember': myVlan[vlanID]['vlan_portModeMember'][interfaceMember],
                                'connectedVlan': connectedVLAN
                            }
                        }
                    )
myDictionary = contTemp1.copy()

with open('output_final.json', 'w') as f:
    json.dump(myDictionary, f, indent = 2)

print(json.dumps(contTemp1, indent=2))
