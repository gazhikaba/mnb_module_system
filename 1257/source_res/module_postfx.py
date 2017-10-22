from header_postfx import *

####################################################################################################################
#  Each postfx_param contains the following fields:
#  1) id (string): 
#  2) flags (int). 
#  3) tonemap operator type (0,1,2,3)
#  4) shader parameters1 [ HDRRange, HDRExposureScaler, LuminanceAverageScaler, LuminanceMaxScaler ]
#  5) shader parameters2 [ BrightpassTreshold, BrightpassPostPower, BlurStrenght, BlurAmount ]
#  6) shader parameters3 [ AmbientColorCoef, SunColorCoef, SpecularCoef, -reserved ]
# 
	#define postfxParams1	(PFX1)	float4(postfx_editor_vector[1].x, postfx_editor_vector[1].y, postfx_editor_vector[1].z, postfx_editor_vector[1].w) 
	#define postfxParams2	(PFX2)	float4(postfx_editor_vector[2].x, postfx_editor_vector[2].y, postfx_editor_vector[2].z, postfx_editor_vector[2].w)
	#define postfxParams3	(PFX3)	float4(postfx_editor_vector[3].x, postfx_editor_vector[3].y, postfx_editor_vector[3].z, postfx_editor_vector[3].w)

####################################################################################################################

postfx_params = [

("default", 0, 0, [125.992203, 1.058800, 1.451000, 9.176500], [0.960800, 1.137300, 1.137300, 0.196100], [1.000000, 1.000000, 1.000000, 1.000000]),
("map_params", 0, 3, [128.000000, 1.040000, 1.294100, 10.000000], [2.372500, 2.156900, 1.843100, 0.486300], [1.000000, 1.000000, 1.050000, 1.000000]),
("indoors", 0, 0, [128.000000, 1.000000, 1.254900, 10.000000], [0.647100, 4.784300, 4.161600, 0.001550], [0.980400, 0.980400, 1.529400, 1.000000]),
("sunset", 0, 0, [128.000000, 0.588200, 0.980400, 0.980400], [0.078400, 2.117600, 1.372500, 0.125500], [0.980400, 0.980400, 1.764700, 1.000000]),
("night", 0, 0, [128.000000, 1.000000, 1.254900, 10.000000], [0.647100, 4.784300, 1.215700, 0.000000], [0.980400, 0.980400, 1.529400, 1.000000]),
("sunny", 0, 0, [128.000000, 0.588200, 0.980400, 0.980400], [0.078400, 2.117600, 1.372500, 0.125500], [0.980400, 0.980400, 1.764700, 1.000000]),
("cloudy", 0, 0, [128.000000, 1.000000, 0.980400, 0.000000], [0.313700, 2.666700, 2.000000, 0.431400], [0.980400, 0.980400, 1.431400, 1.000000]),
("overcast", 0, 0, [128.000000, 1.000000, 0.980400, 0.000000], [0.313700, 2.666700, 2.000000, 0.000000], [0.980400, 0.980400, 1.031400, 1.000000]),
("high_contrast", 0, 3, [128.000000, 1.000000, 1.294100, 10.000000], [0.431400, 2.000000, 1.058800, 0.054900], [2.000000, 0.705900, 1.490200, 1.000000]),

]