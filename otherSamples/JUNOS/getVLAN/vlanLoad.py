import json

with open('output_vlan.json') as f:
    myVlan = json.load(f)

with open('output.json') as f:
    myDictionary = json.load(f)

contTemp1 = myDictionary.copy()
for myHardware in contTemp1['hardware']:
    contTemp1['hardware'][myHardware].update({'vlans': {'vlanID': {},'vlanName': {}}})
    for vlanID in myVlan:
        contTemp1['hardware'][myHardware]['vlans']['vlanID'].update(
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
        if myVlan[vlanID]['vlan_interfaceMember'] is not None:
            if isinstance(myVlan[vlanID]['vlan_interfaceMember'], str) == True:
                contTemp1['hardware'][myHardware]['vlans']['vlanID'][vlanID].update(
                    {myVlan[vlanID]['vlan_interfaceMember']:
                        {
                            'tagnessMember': myVlan[vlanID]['vlan_tagnessMember'],
                            'portModeMember': myVlan[vlanID]['vlan_portModeMember']
                        }
                    }
                )
            else:
                for interfaceMember in range(0,len(myVlan[vlanID]['vlan_interfaceMember'])):
                    contTemp1['hardware'][myHardware]['vlans']['vlanID'][vlanID].update(
                        {myVlan[vlanID]['vlan_interfaceMember'][interfaceMember]:
                            {
                                'tagnessMember': myVlan[vlanID]['vlan_tagnessMember'][interfaceMember],
                                'portModeMember': myVlan[vlanID]['vlan_portModeMember'][interfaceMember]
                            }
                        }
                    )

print(json.dumps(contTemp1, indent=2))
