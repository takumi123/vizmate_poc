import path from 'path';
import axios from 'axios';

// OpenAI API設定
const OPENAI_API_KEY = process.env.OPENAI_API_KEY;
const OPENAI_API_URL = 'https://api.openai.com/v1/chat/completions';

// ディレクトリ設定
const docsDir = path.join(__dirname, '..', 'docs');
const jaDir = path.join(docsDir, 'ja');
const enDir = path.join(docsDir, 'en');

// 翻訳関数
async function translateText(text, targetLang) {
  try {
    const response = await axios.post(
      OPENAI_API_URL,
      {
        model: "gpt-4", // 使用するモデルを指定
        messages: [
          { role: "system", content: `You are a helpful assistant that translates text to ${targetLang}.` },
          { role: "user", content: text },
        ],
        max_tokens: 10000, // 必要に応じて調整
      },
      {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${OPENAI_API_KEY}`,
        },
      }
    );
    return response.data.choices[0].message.content.trim();
  } catch (error) {
    console.error('Translation error:', error.response ? error.response.data : error.message);
    throw error;
  }
}

// ファイル翻訳処理
async function translateFiles(sourceDir, targetDir, targetLang) {
  const files = fs.readdirSync(sourceDir);
  for (const file of files) {
    const sourceFilePath = path.join(sourceDir, file);
    const targetFilePath = path.join(targetDir, file);

    if (fs.lstatSync(sourceFilePath).isFile()) {
      const content = fs.readFileSync(sourceFilePath, 'utf-8');
      const translatedContent = await translateText(content, targetLang);
      fs.writeFileSync(targetFilePath, translatedContent, 'utf-8');
      console.log(`Translated ${file} to ${targetLang}`);
    }
  }
}

(async () => {
  // コミットメッセージを取得してスキップ判定
  const githubEventPath = process.env.GITHUB_EVENT_PATH;
  let shouldSkip = false;
  if (githubEventPath) {
    const githubEvent = JSON.parse(fs.readFileSync(githubEventPath, 'utf-8'));
    const commitMessages = githubEvent.commits.map(commit => commit.message);
    const skipKeywords = ['[skip translation]', '[skip ci]'];
    shouldSkip = commitMessages.some(message =>
      skipKeywords.some(keyword => message.includes(keyword))
    );
  }

  if (shouldSkip) {
    console.log('Translation skipped due to commit message.');
    process.exit(0);
  }

  // 変更されたファイルを取得
  const githubEvent = process.env.GITHUB_EVENT_PATH
    ? JSON.parse(fs.readFileSync(process.env.GITHUB_EVENT_PATH, 'utf-8'))
    : null;

  const changedFiles = githubEvent
    ? githubEvent.commits.flatMap(commit => commit.modified.concat(commit.added))
    : [];

  const isJaChanged = changedFiles.some(file => file.startsWith('docs/ja/'));
  const isEnChanged = changedFiles.some(file => file.startsWith('docs/en/'));

  if (isJaChanged && !isEnChanged) {
    // jaからenへ翻訳
    await translateFiles(jaDir, enDir, 'English');
  } else if (isEnChanged && !isJaChanged) {
    // enからjaへ翻訳
    await translateFiles(enDir, jaDir, 'Japanese');
  } else {
    console.log('No relevant changes detected for translation.');
  }
})();
