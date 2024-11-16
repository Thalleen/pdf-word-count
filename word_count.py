import PyPDF2

def count_words_in_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            word_count = 0
            
            for page in reader.pages:
                text = page.extract_text()
                words = text.split()
                word_count += len(words)
                
            return word_count
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return 0

pdf_path = '/Users/thalleencn/Desktop/Sem 7/rough/FinalReport.pdf'
print("Total words:", count_words_in_pdf(pdf_path))