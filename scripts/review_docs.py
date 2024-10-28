import os
import json
import subprocess
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)

# リポジトリのルートディレクトリを設定
ROOT_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT_DIR / 'docs'
JA_DIR = DOCS_DIR / 'ja'
EN_DIR = DOCS_DIR / 'en'
REVIEWS_DIR = DOCS_DIR / 'reviews'

def get_existing_reviews():
    """
    既存のレビューファイルの内容を取得
    """
    reviews = {}
    review_files = {
        'ja': REVIEWS_DIR / 'review_ja.md',
        'en': REVIEWS_DIR / 'review_en.md'
    }
    
    for lang, file_path in review_files.items():
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    reviews[lang] = f.read()
            except Exception as e:
                print(f'Error reading existing review file {file_path}: {e}')
                reviews[lang] = ''
        else:
            reviews[lang] = ''
            
    return reviews

def review_document(content, existing_review, lang):
    """
    ChatGPTを使用してドキュメントをレビュー
    """
    prompt = f"""以下の点に注目してシステム設計上の抜け漏れをレビューしてください：
- 必要な機能要件の欠落
- システムコンポーネント間の連携の不足
- セキュリティ上の懸念点
- スケーラビリティに関する考慮不足
- エラーハンドリングの不備
- 監視やログ収集の仕組みの欠如

既存のレビュー内容も考慮して、システム的な観点から簡潔にレビューを行ってください。

既存のレビュー内容:
{existing_review}

レビュー対象のドキュメント:
{content}"""

    try:
        response = client.chat.completions.create(
            model="o1-preview",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_completion_tokens=1000,  # max_tokensからmax_completion_tokensに変更
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f'レビューエラー: {e}')
        raise e

def review_directory(dir_path, existing_review, lang):
    """
    ディレクトリ内の全Markdownファイルをレビュー
    """
    reviews = []
    for file_path in dir_path.glob('**/*.md'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            relative_path = file_path.relative_to(dir_path)
            review_content = review_document(content, existing_review, lang)
            reviews.append(f"\n## {relative_path}\n\n{review_content}\n")
            
        except Exception as e:
            print(f'Error reviewing {file_path}: {e}')
            
    return '\n'.join(reviews)

def save_review(content, file_path):
    """
    レビュー結果をファイルに保存
    """
    try:
        REVIEWS_DIR.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'レビュー結果を{file_path}に保存しました')
    except Exception as e:
        print(f'レビュー結果の保存中にエラーが発生しました {file_path}: {e}')

def main():
    existing_reviews = get_existing_reviews()
    
    # 日本語ドキュメントのレビュー
    ja_review = review_directory(JA_DIR, existing_reviews['ja'], '日本語')
    save_review(ja_review, REVIEWS_DIR / 'review_ja.md')
    
    # 英語ドキュメントのレビュー
    en_review = review_directory(EN_DIR, existing_reviews['en'], 'English')
    save_review(en_review, REVIEWS_DIR / 'review_en.md')

if __name__ == '__main__':
    main()
