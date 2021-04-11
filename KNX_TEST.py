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
                  name ='Lamp Pieter',
                  group_address_switch='0/2/18')
    print(light)
    await light.set_off()

    TempSensor = Sensor(xknx,
                        'TempSensor Bureel Pieter',
                        group_address_state='2/2/11',
                        value_type='temperature')
    await TempSensor.sync()
    print(TempSensor)
    print(TempSensor.resolve_state())
    print(TempSensor.unit_of_measurement())
    print(TempSensor.sensor_value.value)
    await xknx.stop()
#asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close