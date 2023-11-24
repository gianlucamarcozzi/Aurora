class MicrowaveDummy:
    def __init__(self):
        # Connection to instrument via visa

        print('A new connection was established with mw_dummy')
        pass

    def set_frequency(self, freq):
        # here there should be something like:
        # self.connection.query('set_the_new_mw_freq')
        # mw_freq = self.connection.query('what is the mw freq?')

        # now instead I return exactly the input value
        mw_freq = freq
        return mw_freq

