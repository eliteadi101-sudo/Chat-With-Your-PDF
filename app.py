import streamlit as st
from pypdf import PdfReader
import re
st.set_page_config(page_title="PDF Q&A",page_icon="📄")
st.title("📄 Chat With Your PDF")
st.write("Upload a text-based PDF, then ask a question. This demo retrieves matching passages using keywords.")
file=st.file_uploader("Choose a PDF",type=["pdf"])
def chunks(text,size=900,overlap=120):
    text=re.sub(r"\\s+"," ",text).strip()
    return [text[i:i+size] for i in range(0,len(text),size-overlap)] if text else []
if file:
    try:
        reader=PdfReader(file)
        text="\\n".join(page.extract_text() or "" for page in reader.pages)
        st.success(f"Loaded {len(reader.pages)} page(s). Extracted {len(text):,} characters.")
        parts=chunks(text)
        question=st.text_input("Ask a question about the document")
        if question:
            terms={t.lower() for t in re.findall(r"[a-zA-Z0-9]{3,}",question)}
            ranked=sorted(((sum(term in p.lower() for term in terms),i,p) for i,p in enumerate(parts)),reverse=True)
            hits=[p for score,_,p in ranked[:3] if score>0]
            if hits:
                st.subheader("Relevant passages")
                for i,passage in enumerate(hits,1): st.markdown(f"**Passage {i}**\\n\\n> {passage}")
            else: st.info("No matching passage found. Try different keywords or check whether the PDF contains selectable text.")
        with st.expander("Preview extracted text"): st.text(text[:5000] or "No text extracted.")
    except Exception as e: st.error(f"Could not read this PDF: {e}")
else:
    st.info("For best results, use a PDF with selectable text. Scanned image PDFs need OCR.")
st.caption("This is keyword retrieval, not an AI model. Your uploaded file is processed by the local Streamlit app.")
