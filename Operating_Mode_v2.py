Power_down_map = {
        "PA_MNCOMP": True,
        "PA_EN": False, "PA_DSVCG": 1.9, "PA_DSVG": 0.375, # PA_DSVCG, PA_DSVG unit = V
        "PD_EN": False, "PA_PSVCG": 1.9, "PA_PSVG": 0.375, # PA_PSVCG, PA_PSVG unit = V
        "PD_VDDEN": False, "PD_OUTEN": False, "BIAS_VDDEN": False, "PD_GAIN": 0b0,
        "TEMP_OUTEN": False, "TEMP_GAIN": 6,
        "PD_RFEN": False, "COUPLER_RFEN": False, "COUPLER_50EN": True, 

        "COMPENS_VDDEN": False, "COMPENS_CPTAT": "CTAT", "COMPENS_DS": 0, "COMPENS_PS": 0,
        "TEMP_VDDEN": False,
        "TEST_CTRL": "High-Z"
 }

Normal_mode_map = {
        "PA_MNCOMP": True,
        "PA_EN": True, "PA_DSVCG": 2.3, "PA_DSVG": 0.375, # PA_DSVCG, PA_DSVG unit = V
        "PD_EN": True, "PA_PSVCG": 1.9, "PA_PSVG": 0.375, # PA_PSVCG, PA_PSVG unit = V
        "PD_VDDEN": False, "PD_OUTEN": False, "BIAS_VDDEN": True, "PD_GAIN": 0b01010,
        "TEMP_OUTEN": False, "TEMP_GAIN": 6,
        "PD_RFEN": False, "COUPLER_RFEN": False, "COUPLER_50EN": True, 

        "COMPENS_VDDEN": True, "COMPENS_CPTAT": "CTAT", "COMPENS_DS": 0.040625, "COMPENS_PS": 0.040625,
        "TEMP_VDDEN": False,
        "TEST_CTRL": "High-Z"
 }

Coupler_map = {
        "PA_MNCOMP": True,
        "PA_EN": True, "PA_DSVCG": 1.9, "PA_DSVG": 0.375, # PA_DSVCG, PA_DSVG unit = V
        "PD_EN": True, "PA_PSVCG": 1.9, "PA_PSVG": 0.375, # PA_PSVCG, PA_PSVG unit = V
        "PD_VDDEN": False, "PD_OUTEN": False, "BIAS_VDDEN": True, "PD_GAIN": 0b01010,
        "TEMP_OUTEN": False, "TEMP_GAIN": 6,
        "PD_RFEN": False, "COUPLER_RFEN": True, "COUPLER_50EN": False,

        "COMPENS_VDDEN": True, "COMPENS_CPTAT": "CTAT", "COMPENS_DS": 0.040625, "COMPENS_PS": 0.040625,
        "TEMP_VDDEN": False,
        "TEST_CTRL": "High-Z"      
    }

Term_map = {
        "PA_MNCOMP": True,
        "PA_EN": True, "PA_DSVCG": 1.9, "PA_DSVG": 0.375, # PA_DSVCG, PA_DSVG unit = V
        "PD_EN": True, "PA_PSVCG": 1.9, "PA_PSVG": 0.375, # PA_PSVCG, PA_PSVG unit = V
        "PD_VDDEN": False, "PD_OUTEN": False, "BIAS_VDDEN": True, "PD_GAIN": 0b01010,
        "TEMP_OUTEN": False, "TEMP_GAIN": 6,
        "PD_RFEN": False, "COUPLER_RFEN": False, "COUPLER_50EN": True,

        "COMPENS_VDDEN": True, "COMPENS_CPTAT": "CTAT", "COMPENS_DS": 0.040625, "COMPENS_PS": 0.040625,
        "TEMP_VDDEN": False,
        "TEST_CTRL": "High-Z"      
    }

TEMP_map = {
        "PA_MNCOMP": True,
        "PA_EN": True, "PA_DSVCG": 1.9, "PA_DSVG": 0.275, # PA_DSVCG, PA_DSVG unit = V
        "PD_EN": True, "PA_PSVCG": 1.9, "PA_PSVG": 0.300, # PA_PSVCG, PA_PSVG unit = V
        "PD_VDDEN": False, "PD_OUTEN": False, "BIAS_VDDEN": True, "PD_GAIN": 0b01010,
        "TEMP_OUTEN": True, "TEMP_GAIN": 6,
        "PD_RFEN": True, "COUPLER_RFEN": False, "COUPLER_50EN": True,

        "COMPENS_VDDEN": True, "COMPENS_CPTAT": "CTAT", "COMPENS_DS": 0.040625, "COMPENS_PS": 0.040625,
        "TEMP_VDDEN": False,
        "TEST_CTRL": "High-Z"
}

PD_map = {
        "PA_MNCOMP": True,
        "PA_EN": True, "PA_DSVCG": 1.9, "PA_DSVG": 0.375, # PA_DSVCG, PA_DSVG unit = V
        "PD_EN": True, "PA_PSVCG": 1.9, "PA_PSVG": 0.375, # PA_PSVCG, PA_PSVG unit = V
        "PD_VDDEN": True, "PD_OUTEN": True, "BIAS_VDDEN": True, "PD_GAIN": 0b01010,
        "TEMP_OUTEN": False, "TEMP_GAIN": 6,
        "PD_RFEN": True, "COUPLER_RFEN": False, "COUPLER_50EN": True,

        "COMPENS_VDDEN": True, "COMPENS_CPTAT": "CTAT", "COMPENS_DS": 0.040625, "COMPENS_PS": 0.040625,
        "TEMP_VDDEN": False,
        "TEST_CTRL": "High-Z"      
    }