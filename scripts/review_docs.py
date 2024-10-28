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
REVIEWS_DIR = ROOT_DIR / 'reviews'

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
    system_prompt = f"""あなたは{lang}のドキュメントレビュワーです。
以下の点に注意してドキュメントをレビューしてください：
- 文法や表現の誤り
- 一貫性のない用語や表現
- 不明確または曖昧な説明
- 技術的な正確性

既存のレビュー内容も考慮して、新しい視点からレビューを行ってください。
"""

    context = f"既存のレビュー内容:\n{existing_review}\n\nレビュー対象のドキュメント:\n{content}"

    try:
        response = client.chat.completions.create(
            model="o1-preview",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": context}
            ],
            max_tokens=2000,
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
            reviews.append(f"\n## {relative_path}\n")
            reviews.append(review_document(content, existing_review, lang))
            
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
        print(f'Review saved to {file_path}')
    except Exception as e:
        print(f'Error saving review to {file_path}: {e}')

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
