from app.services.document_processor import DocumentProcessor

def test_clean_text():

    processor = DocumentProcessor()

    text = "Hello\n\n\nWorld       GPT"

    cleaned_text = processor._clean_text(text)
    assert cleaned_text == "Hello World GPT"



def test_clean_empty_text():

    processor = DocumentProcessor()
    cleaned = processor._clean_text("")
    assert cleaned == ""