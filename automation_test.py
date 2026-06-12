import json
import yaml
import xml.etree.ElementTree as ET

# This matches the YAML configuration data from your course slides
yaml_data = """
device:
  hostname: csr1kv1
  vendor: cisco
  osversion: "16.09"
  status: active
"""

print("\n--- TASK 1: PARSING YAML ---")
# Load the raw YAML string into a clean Python dictionary
device_dict = yaml.safe_load(yaml_data)

# Print a confirmation message to see if it worked
print(f"Successfully loaded configuration for: {device_dict['device']['hostname']}")
print(f"OS Version is: {device_dict['device']['osversion']}\n")

print("--- TASK 2: CONVERTING TO JSON ---")
# Convert our Python dictionary into a clean JSON string with neat spacing
json_payload = json.dumps(device_dict, indent=4)

# Print it out to see the change!
print(json_payload)
print("-> Ready to send to a REST API!\n")

print("--- TASK 3: EXTRACTING FROM XML ---")
# Raw XML text data mimicking a router interface response
xml_response = """
<inventory>
    <device name="csr1kv1">
        <osversion>16.09</osversion>
    </device>
</inventory>
"""

# Convert the raw XML string into an interactable Element Tree
root = ET.fromstring(xml_response)

# Search for the <device> tag
device_element = root.find('device')

# Extract the 'name' attribute from inside the brackets, and the text between the <osversion> tags
device_name = device_element.attrib['name']
os_version = device_element.find('osversion').text

print(f"Extracted from XML -> Device Name: {device_name}")
print(f"Extracted from XML -> OS Version: {os_version}\n")

print("--- TASK 4: TRANSLATING XML TO JSON VIA DICTIONARY ---")
# 1. We start with raw XML text from a router
router_xml = "<router><name>edge-rt01</name><ip>192.168.1.1</ip></router>"

# 2. Convert XML text into Python memory objects
xml_root = ET.fromstring(router_xml)

# 3. Build the mandatory bridge (Python Dictionary)
bridge_dict = {
    "router_name": xml_root.find('name').text,
    "management_ip": xml_root.find('ip').text
}

# 4. Convert that Python dictionary into a JSON string
final_json = json.dumps(bridge_dict, indent=4)

# Print the final result!
print(final_json)
print("-> Successfully converted XML to JSON using a dictionary bridge!\n")

print("--- TASK 5: CONVERTING DICTIONARY TO XML ---")
# 1. Assume we loaded this from a YAML file into Python memory
config_dict = {
    "hostname": "core-switch01",
    "vlan": "10"
}

# 2. Build the XML tree structure using our dictionary data
root_element = ET.Element("configuration")

host_tag = ET.SubElement(root_element, "hostname")
host_tag.text = config_dict["hostname"]

vlan_tag = ET.SubElement(root_element, "vlan_id")
vlan_tag.text = config_dict["vlan"]

# 3. Convert the internal XML tree into a raw string format
final_xml_string = ET.tostring(root_element, encoding="unicode")

print(final_xml_string)
print("-> Successfully generated XML to send to a legacy router!\n")

print("--- TASK 6: THE CROSS-GENERATION BRIDGE (JSON TO XML) ---")
# 1. Simulate data retrieved from a modern router/API
modern_json_data = '{"hostname": "br-router-01", "ip_address": "10.1.1.1"}'

# 2. Parse JSON string into Python memory (Dictionary)
bridge_dict = json.loads(modern_json_data)

# 3. Convert that Python dictionary into XML for the legacy router
legacy_root = ET.Element("device-config")

name_node = ET.SubElement(legacy_root, "host")
name_node.text = bridge_dict["hostname"]

ip_node = ET.SubElement(legacy_root, "mgmt-ip")
ip_node.text = bridge_dict["ip_address"]

# 4. Generate the final XML text string
final_legacy_xml = ET.tostring(legacy_root, encoding="unicode")

print("Data from Modern Router (JSON):", modern_json_data)
print("Translated for Legacy Router (XML):", final_legacy_xml)
print("-> Cross-generation translation complete!\n")

print("--- TASK 7: EXPORTING ROUTER DATA TO HUMAN-READABLE YAML ---")
# 1. Imagine this messy data structure was retrieved from a network device
router_inventory = {
    "interfaces": {
        "GigabitEthernet1": {"ip": "10.0.0.1", "status": "up"},
        "GigabitEthernet2": {"ip": "192.168.1.1", "status": "down"}
    }
}

# 2. Convert the Python data structure directly into a clean YAML string
human_readable_yaml = yaml.safe_dump(router_inventory, default_flow_style=False)

# 3. Print it out to see how clean it is!
print(human_readable_yaml)
print("-> Successfully exported raw network data into clean YAML for humans!\n")