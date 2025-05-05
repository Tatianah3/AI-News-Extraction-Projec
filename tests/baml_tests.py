# baml_tests.py

import sys
import os

# Add the root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from boundaryml.boundaryml import BoundaryML  # Import the class from boundaryml.py

import pytest
from boundaryml import BoundaryML  # Import BoundaryML directly from boundaryml.py

# Test example to check if BoundaryML works as expected
def test_boundary_ml_extraction():
    # Initialize the BoundaryML class
    boundary_ml = BoundaryML()

    # Example email content (you can replace this with real test data)
    email_body = """
    From: sender@example.com
    Subject: Today's Headlines
    Date: 2025-04-30
    Content: Here's some interesting news.
    """

    # Extract details from the email
    result = boundary_ml.extract_details(email_body)

    # Check if the extraction works as expected
    assert result["sender"] == "Example Sender"
    assert result["subject"] == "Example Subject"
    assert result["date"] == "2025-04-30"
