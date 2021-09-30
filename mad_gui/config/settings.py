class BaseSettings:
    BIND_Y_AXIS = True
    SENSORS_SYNCHRONIZED = True
    AUTO_DOWNSAMPLE = True

    CHANNELS_TO_PLOT = ["acc_z"]

    SNAP_RANGE_S = 0.1  # in seconds
    EVENTS = ["Positive peak", "Negative peak"]

    PLOT_WIDTH_PLAYING_VIDEO = 20  # in seconds
