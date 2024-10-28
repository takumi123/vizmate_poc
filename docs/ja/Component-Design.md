# Reactコンポーネント設計


## コンポーネントの説明
1. **App**: アプリケーションのルートコンポーネント
2. **Layout**: 共通のレイアウトを提供するコンポーネント
   - Header: ヘッダーセクションを表示
   - Footer: フッターセクションを表示
   - Main Content: メインコンテンツエリア
   - Sidebar: サイドバーセクションを表示

3. **ページコンポーネント**:
   - LoginPage: ログイン画面
   - FolderSelectionPage: Google Driveフォルダ選択画面
   - PDFListPage: PDFファイルリスト画面
   - OCRDetailPage: OCR結果詳細および編集画面
   - CSVDownloadPage: CSVダウンロード画面

4. **再利用可能なコンポーネント**:
   - PDFListItem: PDFリストの各項目を表示
   - OCRTextEditor: OCRテキストの編集用コンポーネント
   - PDFViewer: PDFのプレビュー用コンポーネント
   - NavigationButtons: "次へ"と"戻る"のナビゲーションボタン

## 状態管理

- グローバル状態（ユーザー情報、選択されたフォルダなど）はReact ContextまたはReduxを使用して管理
- ローカル状態（フォーム入力、一時的なUI状態など）はReactのuseStateフックを使用

## データ取得

- サーバーサイドレンダリングが必要な場合は、Next.jsのgetServerSidePropsを使用
- クライアントサイドのデータ取得には、キャッシュと再取得を最適化するためにReact Queryを使用

## エラーハンドリング

- アプリケーション全体でエラーをキャッチして表示するためのグローバルエラーハンドリングコンポーネントを作成

## アクセシビリティ

- セマンティックHTML要素を使用
- ARIA属性を適切に設定
- キーボードナビゲーションをサポート