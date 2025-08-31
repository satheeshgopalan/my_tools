import PyPDF2
import os

def lock_pdf(input_pdf_path, output_pdf_path, password):
    with open(input_pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)
        print(f"🔒 PDF locked and saved as: {output_pdf_path}")

def unlock_pdf(input_pdf_path, output_pdf_path, password):
    with open(input_pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        if reader.is_encrypted:
            try:
                reader.decrypt(password)
            except:
                print("❌ Failed to decrypt PDF. Incorrect password?")
                return

        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)
        print(f"🔓 PDF unlocked and saved as: {output_pdf_path}")

# Example usage
if __name__ == "__main__":
    action = input("Do you want to lock or unlock the PDF? (lock/unlock): ").strip().lower()
    input_path = input("Enter input PDF path: ").strip()
    output_path = input("Enter output PDF path: ").strip()
    password = input("Enter password: ").strip()

    if not os.path.exists(input_path):
        print("❌ Input PDF file does not exist.")
    elif action == "lock":
        lock_pdf(input_path, output_path, password)
    elif action == "unlock":
        unlock_pdf(input_path, output_path, password)
    else:
        print("❌ Invalid action. Please enter 'lock' or 'unlock'.")

