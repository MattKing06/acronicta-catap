from jinja2 import Environment, FileSystemLoader
import json
import os
# Only non-optional fields are provided here

import os
from ruamel.yaml import YAML

yaml = YAML(typ="safe")
magnet_dir = '../lattice/Magnet'
magnet_info_list = []

for fname in os.listdir(magnet_dir):
    if fname.endswith('.yaml') or fname.endswith('.yml'):
        with open(os.path.join(magnet_dir, fname)) as f:
            data = yaml.load(f)
            properties = data['properties']
            info = {}
            # Try to get each field, fallback to None if not present
            info['name'] = properties.get('name')
            info['hardware_type'] = properties.get('hardware_type')
            info['type'] = properties.get('magnet_type') or data.get('type')
            info['name_alias'] = properties.get('name_alias')
            info['position'] = properties.get('position')
            info['machine_area'] = properties.get('machine_area')
            magnet_info_list.append(info)

for item in magnet_info_list:
    print(f"Rendering {item['name']}...")
    data_env = Environment(
        loader=FileSystemLoader('../yaml_templates'),
        trim_blocks=True,
        lstrip_blocks=True
    )
    magnet_template = data_env.get_template('magnet.j2')
    # Load the rendered YAML string into a Python dictionary
    magnet_data = json.loads(magnet_template.render(**item))

    yaml_env = Environment(
        loader=FileSystemLoader('../templates'),
        trim_blocks=True,
        lstrip_blocks=True
    )
    yaml_template = yaml_env.get_template('yaml_template.j2')

    output = yaml_template.render(**magnet_data)

    folder = item["hardware_type"]
    output_dir = f'../output/yaml/{folder}'
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{item['name']}.yaml"
    with open(f"{output_dir}/{filename}", "w") as f:
        f.write(output)

    print(f"YAML file rendered to ../output/yaml/{folder}/{filename}")