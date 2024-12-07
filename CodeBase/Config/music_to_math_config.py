class MathToMusicConfig:

    def __init__(self):
        # Band division stored as logarithmic, more data stored in the lower freqs. Mimics human ear.
        self.freq_band_division_type = "logarithmic"

        # Human ear resolution
        # How many bands do you want to store?
        self.freq_band_qty = 100