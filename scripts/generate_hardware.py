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

created_classes = []
for file in example_files:
    with open(file, 'r') as f:
        data = yaml.safe_load(f)
    properties = data.get('properties', {})
    hardware_type = properties.get('hardware_type', None)
    if hardware_type is None:
        raise ValueError("hardware_type is not defined in the YAML file")
    class_name = f"{hardware_type}"
    if class_name not in created_classes:
        # Extract controls_information and properties
        controls_info = data.get('controls_information', {})
        pv_map = controls_info.get('pv_record_map', {})


        # Exclude specified entries from properties
        excluded_keys = {"hardware_type", "name", "name_alias", "machine_area"}
        filtered_properties = {k: v for k, v in properties.items() if k not in excluded_keys}

        # Get hardware type and set class name
        output_filename = f"{class_name.lower()}.py"

        # Prepare PVs and read_only dicts for template
        pvs = {}
        read_only = {}
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

        # Extract property descriptions (optional, can be improved)
        descriptions = {}
        for prop in filtered_properties:
            descriptions[prop] = ""  # Add logic to extract descriptions if available

        env = Environment(loader=FileSystemLoader('../templates'))
        template = env.get_template('hardware_template.j2')

        # Ensure output directory exists
        output_dir = '../output'
        os.makedirs(output_dir, exist_ok=True)

        # Render template with filtered properties
        output = template.render(
            class_name=class_name,
            pvs=pvs,
            read_only=read_only,
            hardware_type=hardware_type,
            properties=filtered_properties,
            descriptions=descriptions,
        )

        with open(os.path.join(output_dir, output_filename), 'w') as f:
            f.write(output)
        created_classes.append(class_name)