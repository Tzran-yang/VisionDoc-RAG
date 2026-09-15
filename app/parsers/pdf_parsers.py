import fitz


def parse_pdf(pdf_path: str):
    doc = fitz.open(pdf_path)

    document = {
        "file_name": pdf_path,
        "page_count": len(doc),
        "pages": []
    }

    for page_number, page in enumerate(doc, start=1):
        text = page.get_text()
        images = page.get_images(full=True)

        page_data = {
            "page_number": page_number,
            "text": text,
            "image_count": len(images),
            "images": []
        }

        document["pages"].append(page_data)

    doc.close()

    return document


if __name__ == "__main__":
    result = parse_pdf("data/raw/sample.pdf")

    print(f"总页数：{result['page_count']}")

    for page in result["pages"]:
        print("=" * 60)
        print(f"第 {page['page_number']} 页")
        print(f"图片数量：{page['image_count']}")
        print(page["text"][:500])