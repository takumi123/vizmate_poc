import os
import json
import subprocess
from pathlib import Path
import openai

# OpenAI API設定
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

# ディレクトリ設定
DOCS_DIR = Path(__file__).resolve().parent.parent / 'docs'
JA_DIR = DOCS_DIR / 'ja'
EN_DIR = DOCS_DIR / 'en'

def get_changed_files():
    """
    git diffを使用して、最新のコミットとその前のコミット間で変更されたファイルを取得
    """
    try:
        diff_output = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'], text=True)
        changed_files = [line.strip() for line in diff_output.splitlines() if line.strip()]
        print(f'Changed files via git diff: {changed_files}')
        return changed_files
    except subprocess.CalledProcessError as e:
        print(f'Error getting changed files via git diff: {e}')
        return []

def get_commit_messages():
    """
    最新のコミットメッセージを取得
    """
    try:
        commit_message = subprocess.check_output(['git', 'log', '-1', '--pretty=%B'], text=True).strip()
        print(f'Latest commit message: {commit_message}')
        return commit_message
    except subprocess.CalledProcessError as e:
        print(f'Error getting commit messages: {e}')
        return ''

def should_skip_translation(commit_message):
    """
    コミットメッセージに '[skip translation]' が含まれているか確認
    """
    skip_keywords = ['[skip translation]']
    for keyword in skip_keywords:
        if keyword in commit_message:
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
        )
        translated_text = response.choices[0].message['content'].strip()
        return translated_text
    except Exception as e:
        print(f'Translation error: {e}')
        raise e

def translate_files(source_dir, target_dir, target_lang):
    """
    指定されたディレクトリ内のファイルを翻訳し、ターゲットディレクトリに保存
    """
    for file_path in source_dir.glob('**/*'):
        if file_path.is_file():
            relative_path = file_path.relative_to(source_dir)
            target_file_path = target_dir / relative_path

            # ターゲットディレクトリに同じパスが存在しない場合は作成
            target_file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            print(f'Translating {file_path} to {target_lang}...')
            translated_content = translate_text(content, target_lang)

            with open(target_file_path, 'w', encoding='utf-8') as f:
                f.write(translated_content)
            print(f'Translated and saved to {target_file_path}')

def main():
    commit_message = get_commit_messages()
    if should_skip_translation(commit_message):
        print('Translation skipped due to commit message.')
        return

    changed_files = get_changed_files()

    is_ja_changed = any(file.startswith('docs/ja/') for file in changed_files)
    is_en_changed = any(file.startswith('docs/en/') for file in changed_files)

    print(f'isJaChanged: {is_ja_changed}, isEnChanged: {is_en_changed}')

    if is_ja_changed and not is_en_changed:
        print('Translating from Japanese to English...')
        translate_files(JA_DIR, EN_DIR, 'English')
    elif is_en_changed and not is_ja_changed:
        print('Translating from English to Japanese...')
        translate_files(EN_DIR, JA_DIR, 'Japanese')
    else:
        print('No relevant changes detected for translation.')

if __name__ == '__main__':
    main()
