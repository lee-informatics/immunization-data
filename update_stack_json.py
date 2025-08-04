import json

# Read the stack.json file
with open('public/stack-hosted.json', 'r') as f:
    data = json.load(f)

# Counter for patient bundles
patient_count = 0

# Iterate through the data array
for item in data['data']:
    # Check if this is a patient bundle
    if item.get('type') == 'Patient Bundle':
        patient_count += 1
        # If this is patient 21 or beyond, set load to false
        if patient_count > 20:
            item['load'] = False

# Write the updated data back to stack.json
with open('public/stack-hosted.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Updated {patient_count - 20} patient entries to have 'load': false")
print("First 20 patients remain with 'load': true")