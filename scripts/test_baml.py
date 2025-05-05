from boundaryml.boundaryml import BoundaryML

# Sample email content (you'd normally read it from your .eml files)
with open('labels/email_01.json', 'r') as file:
    email_data = json.load(file)

email_body = email_data['content']
boundary_ml = BoundaryML()

result = boundary_ml.extract_email_details(email_body)
print(result)
