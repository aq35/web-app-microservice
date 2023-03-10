import os


def run_linters():
    # Mypy静的型チェック
    os.system("mypy .")

    # isortインポート順序チェック
    os.system("isort .")

    # Blackコードフォーマットチェック
    os.system("black --check .")

    # Flake8コード品質チェック
    os.system("flake8 .")
    
    if __name__ == "__main__":
        run_linters()

# 空行を追加