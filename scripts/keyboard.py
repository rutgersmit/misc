from openrazer.client import DeviceManager
#from openrazer.client import constants as razer_constants

# Create a DeviceManager. This is used to get specific devices
device_manager = DeviceManager()


if len(device_manager.devices) == 0:
    print("Did not fund any Razr devices ¯\_(ツ)_/¯")

# Iterate over each device and pretty out some standard information about each
for device in device_manager.devices:
    if device.type == "keyboard":
        device.fx.static(255, 255, 255)

#    print("{}:".format(device.name))   
#    print("   type: {}".format(device.type))   
#    print("   serial: {}".format(device.serial))   
#    print("   firmware version: {}".format(device.firmware_version))   
#    print("   driver version: {}".format(device.driver_version))
#    print()
