import re


def extract_metadata(text: str) -> dict:
    """
    Extract metadata from a medical document.
    """

    metadata = {}

    patterns = {
        "patient_id": r"Patient ID:\s*(.*)",
        "patient_name": r"Patient Name:\s*(.*)",
        "doctor": r"Doctor:\s*(.*)",
        "visit_date": r"Visit Date:\s*(.*)",
        "department": r"Department:\s*(.*)",
        "diagnosis": r"Diagnosis:\s*(.*)",
    }

    for key, pattern in patterns.items():

        match = re.search(pattern, text)

        if match:
            metadata[key] = match.group(1).strip()

    return metadata