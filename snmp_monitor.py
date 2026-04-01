from pysnmp.hlapi import *

def get_snmp_data(ip, community='public'):
    try:
        # CPU OID (generic example)
        oid = '1.3.6.1.4.1.2021.11.9.0'

        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((ip, 161), timeout=1, retries=1),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication or errorStatus:
            return "N/A"

        for varBind in varBinds:
            return int(varBind[1])

    except:
        return "N/A"