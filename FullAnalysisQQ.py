# -*- coding: utf-8 -*-
# Script: FullAnalysisGQQ
#
# GOM-Script-Version: 6.3.1-2
# Script to run a fully automated Aramis analysis
# Written by: Gustavo Quino, 2019
# Available in the GitHub repository: 
# The / in the end of the path name is very important
# If numbers at the beginning or end of directories names add // instead of /
# Paste the file in the Aramis script folder: C:\Users\USERX\AppData\Roaming\gom\v6.3.1\aramis_scripts


import gom

# Definition of functions

def CreateIndex(n):
	x = []
	for i in range (n):
		x.append(i)
	return x

def CreateDataArray(proj_file, n):
	x = []
	for i in range (n):
		x.append(gom.app.aramis_projects[proj_file].stages[str(i)])
	return x
	
gom.script.aramis.switch_to_aramis_mode ()

################ PARAMETERS #####################

proj_name = 'd12-02'
imag_dir  = 'C:/Users/exet3775//Documents/A_Fantastical/F_Experiments/W-Tm55-HR-1145-03//DIC/aramis/'
proj_dir  = imag_dir + proj_name
proj_file = proj_name + '.dap'

# Images
n_images     = 180
pref_images  = '4503'
digit_images = 4
imag_ext     = '.tif'

# Square facet size x size
facet_size = 15
facet_step = 10

# Create indexes
im_index = CreateIndex(n_images)
#print(im_index)

###################################################

#
# Create New Project
#
ARAMIS_PRJ=gom.script.aramis.create_new_project (
	project_directory=proj_dir, 
	images_per_stage=1,
	requires_2d_calibration=False)

#
# Project Parameter
#
gom.script.aramis.set_project_parameter (
	data=ARAMIS_PRJ, 
	field_mode=gom.List ('quadrangle', ['rectangular', 'quadrangle']), 
	samples_x=facet_size, 
	samples_y=facet_size, 
	step_x=facet_step, 
	step_y=facet_step, 
	quad_0=gom.Vec2d (0.00000000e+00, 0.00000000e+00), 
	quad_1=gom.Vec2d (0.00000000e+00, 0.00000000e+00), 
	quad_2=gom.Vec2d (0.00000000e+00, 0.00000000e+00), 
	quad_3=gom.Vec2d (0.00000000e+00, 0.00000000e+00), 
	strain_type='linear', 
	tensor_size=3, 
	validity_quote=5.50000000e+01, 
	material_thickness=1.00000000e+00, 
	strain_location='surface', 
	stress_model=gom.List ('planestress', ['planestress', 'planestrain']), 
	strain_stage_list=gom.List ('total', ['total', 'step-by-step']), 
	default_visu='VisuMajor', 
	token_keys=['inspector', 'company', 'department', 'location', 'date', 'project', 'charge_nr', 'part_nr', 'test_method', 'material', 'temperature', 'test_speed', 'length', 'width', 'thickness', 'comment1', 'comment2', 'comment3'], 
	token_types=['string', 'string', 'string', 'string', 'date', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'], 
	token_descriptions=['Inspector', 'Company', 'Department', 'Location', 'Date', 'Project', 'Charge-Nr.', 'Part-Nr.', 'Test method', 'Material', 'Temperature', 'Test Speed', 'Length', 'Width', 'Thickness', 'Comment 1', 'Comment 2', 'Comment 3'], 
	token_contents=['', '', '', '', '12/07/2019', '', '', '', '', '', '°C', '', 'mm', 'mm', 'mm', '', '', ''], 
	token_dont_overwrite=['false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false'])

gom.script.aramis.set_2d_parameter (
	data=ARAMIS_PRJ, 
	mode_2d=gom.List ('camera', ['parallel', 'camera', 'correction']), 
	ref_p1=gom.Vec2d (0.00000000e+00, 0.00000000e+00), 
	ref_p2=gom.Vec2d (1.00000000e+00, 0.00000000e+00), 
	ref_distance_3d=1.00000000e-01)

#
# Stage Defaults
#
gom.script.aramis.set_stage_defaults (
	data=ARAMIS_PRJ, 
	interpolation_method=gom.List ('bilinear', ['bilinear', 'bicubic']), 
	accuracy=4.00000000e-02, 
	residual=2.00000000e+01, 
	lower_limit=10, 
	upper_limit=99, 
	intersection_error=3.00000000e-01)

#
# Set System Value Names
#
gom.script.stagedata.set_system_value_parameters (
	data=ARAMIS_PRJ, 
	substitutions=[', system=\'stage time\', name=\'stage time\'', ', system=\'ad channel 0\', name=\'ad channel 0\'', ', system=\'ad channel 1\', name=\'ad channel 1\'', ', system=\'ad channel 2\', name=\'ad channel 2\'', ', system=\'ad channel 3\', name=\'ad channel 3\'', ', system=\'ad channel 4\', name=\'ad channel 4\'', ', system=\'ad channel 5\', name=\'ad channel 5\'', ', system=\'ad channel 6\', name=\'ad channel 6\'', ', system=\'ad channel 7\', name=\'ad channel 7\''])

#
# Set Automatic Definition
#
gom.script.stagedata.set_automatic_parameters (
	data=ARAMIS_PRJ, 
	automatics=[', system=\'stage time\', destination=\'stage time trans\', display=\'Time\', active=True, use_trafo=True, offset=0.00000000e+00, gain=1.00000000e+00, unit=\'s\'', ', system=\'ad channel 0\', destination=\'ad channel 0 trans\', display=\'AD 0 (transformed)\', active=True, use_trafo=False, offset=0.00000000e+00, gain=1.00000000e+00, unit=\'V\'', ', system=\'ad channel 1\', destination=\'ad channel 1 trans\', display=\'AD 1 (transformed)\', active=True, use_trafo=False, offset=0.00000000e+00, gain=1.00000000e+00, unit=\'V\'', ', system=\'ad channel 2\', destination=\'ad channel 2 trans\', display=\'AD 2 (transformed)\', active=True, use_trafo=False, offset=0.00000000e+00, gain=1.00000000e+00, unit=\'V\'', ', system=\'ad channel 3\', destination=\'ad channel 3 trans\', display=\'AD 3 (transformed)\', active=True, use_trafo=False, offset=0.00000000e+00, gain=1.00000000e+00, unit=\'V\'', ', system=\'ad channel 4\', destination=\'ad channel 4 trans\', display=\'AD 4 (transformed)\', active=True, use_trafo=False, offset=0.00000000e+00, gain=1.00000000e+00, unit=\'V\'', ', system=\'ad channel 5\', destination=\'ad channel 5 trans\', display=\'AD 5 (transformed)\', active=True, use_trafo=False, offset=0.00000000e+00, gain=1.00000000e+00, unit=\'V\'', ', system=\'ad channel 6\', destination=\'ad channel 6 trans\', display=\'AD 6 (transformed)\', active=True, use_trafo=False, offset=0.00000000e+00, gain=1.00000000e+00, unit=\'V\'', ', system=\'ad channel 7\', destination=\'ad channel 7 trans\', display=\'AD 7 (transformed)\', active=True, use_trafo=False, offset=0.00000000e+00, gain=1.00000000e+00, unit=\'V\''])

INFO_LABEL=gom.script.strain.create_info_label (
	data=ARAMIS_PRJ, 
	name='Text label')

gom.script.cad.set_properties (
	data=INFO_LABEL, 
	label_template_type=gom.List ('info_label', ['angle', 'angle_measurement', 'body', 'border_line', 'cad_section', 'caliper_disc', 'caliper_edge', 'circle', 'circular_fitting_section', 'cmm_angle_inspection', 'cmm_circle', 'cmm_distance_inspection_scalar', 'cmm_distance_inspection_vector', 'cmm_edge_point_1v', 'cmm_edge_point_2v', 'cmm_point', 'cmm_rectangular_hole', 'cmm_referenced_distance', 'cmm_referenced_symmetric_point', 'cmm_regular_poly_hole', 'cmm_slotted_hole', 'cmm_touch_point_disc', 'cmm_touch_point_edge', 'cmm_vector_point', 'colored_polygonization', 'cone', 'coordinate_system', 'cylinder', 'cylindrical_fitting_points', 'cylindrical_fitting_surface', 'deviation_mesh', 'deviation_point_cloud', 'deviation_section', 'directed_distance', 'disc', 'displacement_field_measurement', 'distance', 'dof6_measurement', 'edge_deviation_border_line', 'edge_deviation_point_cloud', 'edge_point', 'edge_section', 'flat_fitting_points', 'flat_fitting_surface', 'gdat_angularity', 'gdat_concentricity', 'gdat_cylindricity', 'gdat_datum_system', 'gdat_flatness', 'gdat_parallelism', 'gdat_perpendicularity', 'gdat_position', 'gdat_roundness', 'gdat_straightness', 'info_label', 'inspection2d_point', 'inspection2d_section', 'keywords', 'limited_plane', 'line', 'line_measurement', 'line_segment', 'nurbs_curve', 'nurbs_surface', 'paraboloid', 'plane', 'point', 'point_cloud', 'point_line_measurement', 'point_measurement', 'point_plane_measurement', 'polygonization', 'polynomial_surface', 'probe_border_segment', 'probe_center_point', 'probe_circle', 'probe_cone', 'probe_cylinder', 'probe_online_element', 'probe_picker', 'probe_plane', 'probe_point', 'probe_poly_line', 'probe_rectangular_hole', 'probe_slotted_hole', 'probe_sphere', 'rectangular_hole', 'reference_points', 'regular_poly_hole', 'section', 'slotted_hole', 'sphere', 'stage_matching_point', 'stage_pixel_point', 'stage_reference_point', 'straight_fitting_section', 'strain_section', 'strain_stage_point', 'surface_point', 'tape_line', 'text_label', 'thickness_mesh', 'thickness_picker']), 
	label_template_name='Info (current visualization)', 
	label_template_text='<table border=1 cellspacing=-1>\n<tr>\n<td align=center valign=center colspan=2><p>$prj_n$</p></td>\n</tr>\n<tr>\n<td align=right valign=center><p>Visualization</p></td>\n<td align=right valign=center><p>$prj_visualization$</p></td>\n</tr>\n<tr>\n<td align=right valign=center><p>Stage from to</p></td>\n<td align=right valign=center><p>$.0stage_from$ -> $.0stage_to$</p></td>\n</tr>\n</table>', 
	label_template_use_system_font=True, 
	label_template_font_family='Verdana', 
	label_template_font_size=9.00000000e+00, 
	label_template_font_style=[], 
	label_template_font_underline=False, 
	label_template_font_strikeout=False, 
	label_template_text_color=gom.Color (0, 0, 0, 255), 
	label_template_draw_border=True, 
	label_template_draw_back=True, 
	label_template_back_color=gom.Color (255, 255, 255, 255), 
	label_template_border_width=1.00000000e-01, 
	label_template_border_color=gom.Color (0, 0, 0, 255), 
	label_template_connector_color=gom.Color (0, 0, 0, 255), 
	label_template_connector_width=1.00000000e-01, 
	label_show=True)

gom.script.fg.snap_file_video (
	target=gom.app.aramis_projects[proj_file], 
	image_indices=im_index,
	convert=gom.List ('gray8', ['none', 'gray8']), 
	name_prefixes  = [imag_dir + pref_images], 
	name_postfixes = [imag_ext], 
#	name_digitcounts=[7], 
#	image_offsets=[1230001],
	name_digitcounts=[digit_images], 
	image_offsets=[0001], 
	calibration=gom.File (''))

# Create Data Mask array
arrayData = CreateDataArray(proj_file, n_images)
#print(arrayData)

gom.interactive.aramis.create_mask (data = arrayData)

gom.script.aramis.create_automatic_start_point (
	data = arrayData, 
	centers=[])

gom.script.aramis.compute_project (data = arrayData)

# Show evaluation mode (check the results)
gom.script.aramis.switch_to_evaluation_mode ()
