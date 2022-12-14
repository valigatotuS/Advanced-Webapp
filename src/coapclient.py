import asyncio
from aiocoap import *

async def coapgetlampstatus(url):
    print('coapgetlampstatus on', url)
    protocol = await Context.create_client_context()
    request = Message(code=GET, uri=url)

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:', e)
    else:
        print('Result: %s\n%r'%(response.code, response.payload))
        return response.payload

async def coapsetlampstatus(url, value):
    print('coapsetlampstatus on', url, 'with value', value)
    protocol = await Context.create_client_context()
    request = Message(code=PUT, uri=url, payload=value)

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:', e)
    else:
        print('Result: %s'%(response.code))
        
async def main():
   await coapsetlampstatus('coap://lamp1a.irst.be/lamp/dimming', b'0')
   
   val = await coapgetlampstatus('coap://lamp1c.irst.be/lamp/dimming')
   print("retrieved lamp value:", val)

async def getlampstatus(lamp):
    val = await coapgetlampstatus('coap://' + lamp + '.irst.be/lamp/dimming')
    return val

async def setlampstatus(lamp, brightness):
    await coapsetlampstatus('coap://' + lamp + '.irst.be/lamp/dimming', str.encode(brightness))

def get_lamps_level()->dict:
    """Return a dictionnary containing the brightness for each lamp {<lamp_id>:<lamp_level=(0-100)>}"""
    lamp_levels = {}

    for row in range(1,6):
        for col in ['a', 'b', 'c']:
            lamp_levels['lamp' + str(row) + col] = (int((asyncio.run(coapgetlampstatus('coap://lamp' + str(row) + str(col) + '.irst.be/lamp/dimming'))).decode('utf-8')))
    return lamp_levels


if __name__ == "__main__":
   asyncio.run(main())