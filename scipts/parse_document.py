import json
import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from app.parsers.pdf_parsers import parse_pdf


def main():
    input_path = "data/raw/sample.pdf"
    output_path = "data/processed/sample.json"

    pages = parse_pdf(input_path)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(
            pages,
            f,
            ensure_ascii=False,
            indent=2
        )

    print(f"解析完成，共 {len(pages)} 页")
    print(f"结果保存到：{output_path}")


if __name__ == "__main__":
    main()