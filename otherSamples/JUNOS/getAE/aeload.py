import json

with open('interface_get_ae.json') as f:
    myAE = json.load(f)

with open('interface_get_data.json') as f:
    myDictionary = json.load(f)

contTemp1 = myDictionary.copy()
for myHardware in myDictionary['hardware']:
    for myAgg in myDictionary['hardware'][myHardware]['interface_name']:
        if 'ae' in myAgg:
            if myDictionary['hardware'][myHardware]['interface_name'][myAgg]['aeBundle']['interfacePHY'] is not None:
                del contTemp1['hardware'][myHardware]['interface_name'][myAgg]['aeBundle']['interfacePHY']
                contTemp1['hardware'][myHardware]['interface_name'][myAgg]['aeBundle'].update({'interfacePHY': {}})
                for count1 in range(0, len(myAE[myAgg]['ae_link'])):
                    contTemp1['hardware'][myHardware]['interface_name'][myAgg]['aeBundle']['interfacePHY'].update(
                        {myAE[myAgg]['ae_link'][count1]:
                            {'lacp_statistics_if':
                                {
                                    'lacp_rx_packets': myAE[myAgg]['lacp_rx_packets'][count1],
                                    'lacp_tx_packets': myAE[myAgg]['lacp_tx_packets'][count1],
                                    'unknown_rx_packets': myAE[myAgg]['unknown_rx_packets'][count1],
                                    'illegal_rx_packets': myAE[myAgg]['illegal_rx_packets'][count1]
                                }
                            }
                        }
                    )
                    interfacePHY = myAE[myAgg]['ae_link'][count1]
                    interfacePHY = interfacePHY[0:interfacePHY.find('.')]
                    contTemp1['hardware'][myHardware]['interface_name'][interfacePHY].update(
                        {'aggregate_interface':
                            {
                                'logical_name': myAE[myAgg]['logical_name']
                            }
                        }
                    )

myDictionary = contTemp1.copy()

with open('output.json', 'w') as f:
    json.dump(myDictionary, f, indent = 2)
