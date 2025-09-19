from PyPDF2 import PdfMerger

# 📥 Get list of PDF files to merge
pdf_files = input("Enter PDF file paths separated by commas:\n").split(',')

# 📤 Output file name
output_file = input("Enter output PDF file name (e.g., merged.pdf): ").strip()

# 📚 Create a PdfMerger object
merger = PdfMerger()

# ➕ Add each PDF to the merger
for file in pdf_files:
    file = file.strip()
    try:
        merger.append(file)
        print(f"Added: {file}")
    except Exception as e:
        print(f"❌ Failed to add {file}: {e}")

# 💾 Write out the merged PDF
merger.write(output_file)
merger.close()

print(f"\n✅ Merged PDF saved as: {output_file}")
