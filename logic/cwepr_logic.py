class CwEprLogic:
    def __init__(self, mw_device, magnet_device, lia_device, psb_device,
                 psa_device, cs_device):
        self.mw_device = mw_device
        self.magnet_device = magnet_device
        self.lia_device = lia_device
        self.psb_device = psb_device
        self.psa_device = psa_device
        self.cs_device = cs_device

    def set_mw_frequency(self, freq):
        self.mw_freq = self.mw_device.set_frequency(freq)
        return self.mw_freq