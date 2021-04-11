import asyncio
from xknx import XKNX
from xknx.io import ConnectionConfig
from xknx.io import ConnectionType
from xknx.devices import Light, Sensor

async def main():
    connection_config = ConnectionConfig(
        connection_type=ConnectionType.TUNNELING,
        gateway_ip="10.0.0.197",
        gateway_port=3671,
        local_ip="10.0.0.70")
    xknx = XKNX(connection_config=connection_config)
    await xknx.start()
    print(len(xknx.devices))
    for device in xknx.devices:
        print(device)
    print("Start done")
    light = Light(xknx,
                  name = 'Lamp Pieter',
                  group_address_switch='0/2/18')
    print(light)
    await light.set_off()
    await xknx.stop()
asyncio.run(main())