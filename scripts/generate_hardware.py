from typing import Dict
import yaml
import os
from jinja2 import Environment, FileSystemLoader

# Load YAML data
lattice_location = "../output/yaml"
lattice_folders = os.listdir(lattice_location)
example_files = []
for folder in lattice_folders:
    folder_path = os.path.join(lattice_location, folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".yaml"):
                example_files.append(os.path.join(folder_path, file))

def extract_differing_keys(file_pv_maps) -> Dict[str, Dict]:

    """
    Get the diffs between two pv maps.
    """
    all_keys = set.union(*file_pv_maps.values())
    common_keys = set.intersection(*file_pv_maps.values())
    differing_keys = all_keys - common_keys
    return differing_keys

def construct_pv_map_info(pv_map) -> Dict:
    # Prepare PVs and read_only dicts for template
    pvs = {}
    read_only = {}
    pv_descriptions = {}
    for pv_name, pv_info in pv_map.items():
        pv_type = pv_info.get('type', '').lower()
        if pv_type == 'binary':
            pvs[pv_name] = 'BinaryPV'
        elif pv_type == 'state':
            pvs[pv_name] = 'StatePV'
        elif pv_type == 'scalar':
            pvs[pv_name] = 'ScalarPV'
        elif pv_type == 'statistical':
            pvs[pv_name] = 'StatisticalPV'
        elif pv_type == 'waveform':
            pvs[pv_name] = 'WaveformPV'
        elif pv_type == 'string':
            pvs[pv_name] = 'StringPV'
        else:
            pvs[pv_name] = 'PV'
        read_only[pv_name] = pv_info.get('read_only', True)
        pv_descriptions[pv_name] = pv_info.get('description', "")
    return pvs, read_only, pv_descriptions

def aggregate_pv_maps(file_pv_maps: Dict[str, Dict]) -> Dict[str, Dict]:
    """
    Aggregate the PV maps from multiple files into a single dictionary.
    """
    aggregated_map = {}
    return aggregated_map

created_classes = []
file_pv_maps = {}
file_pv_info = {}
optional_pvs = {}

# Iterate through the example files to extract hardware types and PV maps
# This will need to be done once per hardware_type so we can gather
# information about optional PVs etc.
for file in example_files:
    with open(file, 'r') as f:
        data = yaml.safe_load(f)
    properties = data.get('properties', {})
    hardware_type = properties.get('hardware_type', None)
    if hardware_type is None:
        raise ValueError("hardware_type is not defined in the YAML file")
    class_name = f"{hardware_type}"
    # Extract controls_information and properties
    controls_info = data.get('controls_information', {})
    # remove the pv_record_map from controls_info as we already have that information
    controls_info.pop('pv_record_map', None)
    pv_map = controls_info.get('pv_record_map', {})
    if class_name not in file_pv_maps:
        file_pv_maps[class_name] = {}
    if class_name not in file_pv_info:
        file_pv_info[class_name] = {}
    file_pv_maps[class_name][file] = set(pv_map.keys())
    file_pv_info[class_name].update(pv_map)

class_name = None
# Iterate through the files to construct the PV map and optional PVs
for file in example_files:
    with open(file, 'r') as f:
        data = yaml.safe_load(f)
    properties = data.get('properties', {})
    hardware_type = properties.get('hardware_type', None)
    if hardware_type is None:
        raise ValueError("hardware_type is not defined in the YAML file")
    if hardware_type != class_name:
        # reset pv_map and optional pvs for each hardware type
        current_optional_pvs = extract_differing_keys(file_pv_maps[hardware_type])
        current_pv_map = file_pv_info.get(hardware_type, {})
        if not current_pv_map:
            raise ValueError(f"No PV map found for {hardware_type} in {file}")
        pvs, read_only, pv_descriptions = construct_pv_map_info(current_pv_map)
    class_name = f"{hardware_type}"

    if class_name not in created_classes:
        # If the class has not been created yet, generate it
        print(f"Generating class for {class_name} with hardware type {hardware_type}")
        # Exclude specified entries from properties
        # These are default attributes of CATAP.common.machine.hardware.py and should not be redefined.
        excluded_keys = {"hardware_type", "name", "name_alias", "machine_area", "position",}
        filtered_properties = {k: v for k, v in properties.items() if k not in excluded_keys}

        # Get hardware type and set class name
        output_filename = f"{class_name.lower()}.py"
        env = Environment(loader=FileSystemLoader('../templates/classes'))
        template = env.get_template('component_model_template.j2')
        hardware_template = env.get_template('hardware_model_template.j2')

        # Ensure output directory exists
        model_output_dir = '../output/models'
        hardware_output_dir = '../output/hardware'
        os.makedirs(hardware_output_dir, exist_ok=True)
        # Render hardware template
        hardware_output = hardware_template.render(
            class_name=class_name,
            hardware_type=hardware_type.lower(),
        )
        os.makedirs(model_output_dir, exist_ok=True)

        # Render template with filtered properties
        model_output = template.render(
            class_name=class_name,
            pvs=pvs,
            read_only=read_only,
            hardware_type=hardware_type,
            properties=filtered_properties,
            pv_descriptions=pv_descriptions,
            optional_pvs=current_optional_pvs
        )

        with open(os.path.join(model_output_dir, output_filename), 'w') as f:
            f.write(model_output)
        created_classes.append(class_name)
        with open(os.path.join(hardware_output_dir, f"{class_name.lower()}.py"), 'w') as f:
            f.write(hardware_output)
        print(f"Generated {output_filename} and {class_name.lower()}.py for {hardware_type}")