import pymssql

try:
    conn = pymssql.connect(server='<Public_IP_or_FQDN>', user='sa', password='surabhi@21', database='healthDB')
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
