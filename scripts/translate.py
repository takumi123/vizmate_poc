import os
import subprocess
from pathlib import Path
import openai

# OpenAI API設定
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    print('Error: OPENAI_API_KEY is not set.')
    exit(1)
openai.api_key = OPENAI_API_KEY

# ディレクトリ設定
DOCS_DIR = Path(__file__).resolve().parent.parent / 'docs'
JA_DIR = DOCS_DIR / 'ja'
EN_DIR = DOCS_DIR / 'en'

def get_changed_files():
    """
    git diffを使用して、GITHUB_EVENT_BEFORE と GITHUB_SHA の間で変更されたファイルを取得
    """
    before = os.getenv('GITHUB_EVENT_BEFORE')
    after = os.getenv('GITHUB_SHA')
    if not before or not after:
        print('Error: GITHUB_EVENT_BEFORE or GITHUB_SHA is not defined.')
        return []
    try:
        diff_output = subprocess.check_output(['git', 'diff', '--name-only', before, after], text=True)
        changed_files = [line.strip() for line in diff_output.splitlines() if line.strip()]
        print(f'Changed files via git diff: {changed_files}')
        return changed_files
    except subprocess.CalledProcessError as e:
        print(f'Error getting changed files via git diff: {e}')
        return []

def get_commit_author():
    """
    最新のコミットの作者を取得
    """
    try:
        author = subprocess.check_output(['git', 'log', '-1', '--pretty=format:%ae'], text=True).strip()
        print(f'Latest commit author email: {author}')
        return author
    except subprocess.CalledProcessError as e:
        print(f'Error getting commit author: {e}')
        return ''

def should_skip_translation(author_email):
    """
    特定のユーザー（例: GitHub Actions）によるコミットの場合、翻訳をスキップ
    """
    # GitHub Actions のデフォルトのユーザーは 'github-actions[bot]' のメールアドレスです
    # 確認するメールアドレスを以下に追加
    skip_authors = [
        'github-actions[bot]@users.noreply.github.com',
        # 必要に応じて他のメールアドレスを追加
    ]
    if author_email in skip_authors:
        return True
    return False

def translate_text(text, target_lang):
    """
    OpenAI APIを使用してテキストを翻訳
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant that translates text to {target_lang}."},
                {"role": "user", "content": text},
            ],
            max_tokens=2000,
            temperature=0.3,
        )
        translated_text = response.choices[0].message['content'].strip()
        return translated_text
    except Exception as e:
        print(f'Translation error: {e}')
        raise e

def translate_file(source_file_path, target_file_path, target_lang):
    """
    単一ファイルを翻訳し、ターゲットファイルに保存
    """
    try:
        with open(source_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f'Error reading {source_file_path}: {e}')
        return

    print(f'Translating {source_file_path} to {target_lang}...')
    try:
        translated_content = translate_text(content, target_lang)
    except Exception as e:
        print(f'Failed to translate {source_file_path}: {e}')
        return

    try:
        with open(target_file_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        print(f'Translated and saved to {target_file_path}')
    except Exception as e:
        print(f'Error writing to {target_file_path}: {e}')

def main():
    # 最新のコミットの作者を取得
    author_email = get_commit_author()
    if should_skip_translation(author_email):
        print('Translation skipped due to commit author.')
        return

    changed_files = get_changed_files()

    if not changed_files:
        print('No changed files detected.')
        return

    # リストを整理
    ja_changed_files = [file for file in changed_files if file.startswith('docs/ja/')]
    en_changed_files = [file for file in changed_files if file.startswith('docs/en/')]

    print(f'ja_changed_files: {ja_changed_files}')
    print(f'en_changed_files: {en_changed_files}')

    # jaからenへ翻訳
    for file in ja_changed_files:
        source_file_path = DOCS_DIR / file
        relative_path = Path(file).relative_to('docs/ja')
        target_file_path = EN_DIR / relative_path

        # ターゲットディレクトリに同じパスが存在しない場合は作成
        target_file_path.parent.mkdir(parents=True, exist_ok=True)

        translate_file(source_file_path, target_file_path, 'English')

    # enからjaへ翻訳
    for file in en_changed_files:
        source_file_path = DOCS_DIR / file
        relative_path = Path(file).relative_to('docs/en')
        target_file_path = JA_DIR / relative_path

        # ターゲットディレクトリに同じパスが存在しない場合は作成
        target_file_path.parent.mkdir(parents=True, exist_ok=True)

        translate_file(source_file_path, target_file_path, 'Japanese')

    if not ja_changed_files and not en_changed_files:
        print('No relevant changes detected for translation.')

if __name__ == '__main__':
    main()
