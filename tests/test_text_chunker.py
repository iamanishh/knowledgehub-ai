from app.chunking.text_chunker import TextChunker
from app.schemas.parsed_document import ParsedDocument


def test_chunker_returns_chunks():

    text = "Hello World" * 500

    document = ParsedDocument(
        filename="resume.pdf",
        pages=1,
        text=text,
        metadata={}
    )

    chunker = TextChunker()

    chunks = chunker.split(document)

    assert len(chunks) > 1


def test_chunk_contains_source():

    document = ParsedDocument(
        filename="resume.pdf",
        pages=1,
        text="Hello World" * 300,
        metadata={}
    )
    chunker = TextChunker()
    chunks = chunker.split(document)
    assert chunks[0].source_document == "resume.pdf"