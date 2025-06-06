from jinja2 import Environment, FileSystemLoader
from jinja2.ext import Extension
import json
import os

# Only non-optional fields are provided here

import os
from ruamel.yaml import YAML

hardware_types = [
    "Magnet",
    "Charge",
    "Camera",
    "BPM",
    "Cavity",
    "EnergyMeter",
    "Mirror",
    "Screen",
]

def zip_filter(a, b):
    return zip(a, b)

missing_pv_default_text = "<ADD_PV_HERE>"
missing_property_default_text = "<MISSING_PROPERTY>"
missing_property_default_int = -999
missing_property_default_float = -999.0
missing_state_map_text = {"STATE_NAME": "<ADD_STATE_HERE>"}

for hardware in hardware_types:
    yaml = YAML(typ="safe")
    hardware_dir = f"../lattice/{hardware}"
    hardware_info_list = []

    for fname in os.listdir(hardware_dir):
        if fname.endswith(".yaml") or fname.endswith(".yml"):
            with open(os.path.join(hardware_dir, fname)) as f:
                data = yaml.load(f)
                properties = data["properties"]
                controls_info = data.get("controls_information", {})
                pv_record_map = controls_info.pop("pv_record_map", {})
                info = {}
                # Try to get each field, fallback to None if not present
                info["name"] = properties.get("name")
                info["hardware_type"] = hardware
                info["type"] = (
                    properties.get(f"{hardware.lower()}_type")
                    or data.get("type")
                    or data.get("subtype")
                    or data.get("CAM_TYPE")
                )
                info["name_alias"] = properties.get("name_alias")
                info["position"] = properties.get("position")
                info["machine_area"] = properties.get("machine_area")
                info["pv_records"] = pv_record_map.keys()
                info["controls_information"] = controls_info
                info["properties"] = properties
                hardware_info_list.append(info)

    for item in hardware_info_list:
        print(f"Rendering {item['name']}...")
        data_env = Environment(
            loader=FileSystemLoader("../templates/yaml/components"),
            trim_blocks=True,
            lstrip_blocks=True,
            extensions=["jinja2.ext.do"],
        )
        data_env.filters["zip"] = zip_filter
        # Load the hardware template based on the hardware type
        hardware_template = data_env.get_template(f"{hardware.lower()}.j2")
        # Load the rendered YAML string into a Python dictionary
        
        rendered_hardware_template = hardware_template.render(
            **item,
            missing_property_default_text=missing_property_default_text,
            missing_state_map=missing_state_map_text,
            missing_pv_default_text=missing_pv_default_text,
            missing_property_int=missing_property_default_int,
            missing_property_float=missing_property_default_float,
        )
        print(f"Rendered template for {item['name']}:\n \"{rendered_hardware_template}\"")
        # Convert the rendered template to a dictionary
        hardware_data = json.loads(
            rendered_hardware_template,
        )

        yaml_env = Environment(
            loader=FileSystemLoader("../templates/yaml"),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        yaml_template = yaml_env.get_template("base_yaml_template.j2")

        output = yaml_template.render(**hardware_data)

        folder = item["hardware_type"]
        output_dir = f"../output/yaml/{folder}"
        os.makedirs(output_dir, exist_ok=True)
        filename = f"{item['name']}.yaml"
        with open(f"{output_dir}/{filename}", "w") as f:
            f.write(output)

        print(f"YAML file rendered to ../output/yaml/{folder}/{filename}")
