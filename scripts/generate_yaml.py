from jinja2 import Environment, FileSystemLoader
from jinja2.ext import Extension
import json
import os
# Only non-optional fields are provided here

import os
from ruamel.yaml import YAML

hardware_types = ["Magnet", "Charge", "Camera", "BPM", "Cavity", "EnergyMeter"]

missing_pv_default_text = "<ADD_PV_HERE>"

for hardware in hardware_types:
    yaml = YAML(typ="safe")
    hardware_dir = f'../lattice/{hardware}'
    hardware_info_list = []

    for fname in os.listdir(hardware_dir):
        if fname.endswith('.yaml') or fname.endswith('.yml'):
            with open(os.path.join(hardware_dir, fname)) as f:
                data = yaml.load(f)
                properties = data['properties']
                info = {}
                # Try to get each field, fallback to None if not present
                info['name'] = properties.get('name')
                info['hardware_type'] = hardware
                info['type'] = properties.get(f'{hardware.lower()}_type') or data.get('type') or data.get("CAM_TYPE")
                info['name_alias'] = properties.get('name_alias')
                info['position'] = properties.get('position')
                info['machine_area'] = properties.get('machine_area')
                info['missing_pv'] = missing_pv_default_text
                hardware_info_list.append(info)

    for item in hardware_info_list:
        print(f"Rendering {item['name']}...")
        data_env = Environment(
            loader=FileSystemLoader('../yaml_templates'),
            trim_blocks=True,
            lstrip_blocks=True,
            extensions=['jinja2.ext.do']
        )
        hardware_template = data_env.get_template(f'{hardware.lower()}.j2')
        # Load the rendered YAML string into a Python dictionary
        hardware_data = json.loads(hardware_template.render(**item))

        yaml_env = Environment(
            loader=FileSystemLoader('../templates'),
            trim_blocks=True,
            lstrip_blocks=True
        )
        yaml_template = yaml_env.get_template('yaml_template.j2')

        output = yaml_template.render(**hardware_data)

        folder = item["hardware_type"]
        output_dir = f'../output/yaml/{folder}'
        os.makedirs(output_dir, exist_ok=True)
        filename = f"{item['name']}.yaml"
        with open(f"{output_dir}/{filename}", "w") as f:
            f.write(output)

        print(f"YAML file rendered to ../output/yaml/{folder}/{filename}")