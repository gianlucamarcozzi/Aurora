from hardware.current_source.current_source_dummy import CurrentSourceDummy
from hardware.lockin.lockin_dummy import LockinDummy
from hardware.magnet.magnet_dummy import MagnetDummy
from hardware.microwave.microwave_dummy import MicrowaveDummy
from hardware.power_supply.power_supply_dummy import PowerSupplyDummy

from logic.cwepr_logic import CwEprLogic


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mw_device = MicrowaveDummy()
    magnet_device = MagnetDummy()
    lia_device = LockinDummy()
    psb_device = PowerSupplyDummy()
    psa_device = PowerSupplyDummy()
    cs_device = CurrentSourceDummy()

    cwepr_logic = CwEprLogic(mw_device, magnet_device, lia_device,
                             psb_device, psa_device, cs_device)
