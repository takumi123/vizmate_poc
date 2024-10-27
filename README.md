## docs
https://japan-marketing-co-jp.gitbook.io/vizmate_poc

---

# English
 // Start Generation Here
## Project Overview

This project is a web application that allows users to log in with their Google accounts, automatically import PDF files from a specified folder in Google Drive, perform OCR processing, view and edit the results on the web, and supports downloading them in CSV format.

## Main Features

### User Authentication
- OAuth 2.0-based login using Google accounts
- No other login methods are provided

### Google Drive Integration
- Users can select folders from their own Google Drive
- Automatically import PDF files uploaded to the selected folder into Vercel storage

### PDF Management
- Display a list of imported PDF files (file name, upload date, processing status)
- Simultaneous display and editing of OCR results and PDF previews for each PDF file

### OCR Results Management
- Edit and save OCR processing results
- Bulk download OCR results of multiple files in CSV format

## Technology Stack

- **Frontend:** Next.js (Vercel), TypeScript
- **Backend:** Next.js API routes, Vercel database services
- **Authentication:** Google OAuth 2.0
- **OCR Processing:** Vercel storage

## Non-functional Requirements

- **Performance:** Maintain response times within 3 seconds for each page
- **Security:** Implement encryption and access restrictions for user data
- **Usability:** Intuitive and responsive user interface

## Project Purpose

This project aims to enable users to efficiently manage PDF files and perform OCR processing, facilitating easy viewing, editing, and exporting of data. Integration with Google Drive simplifies file management, and leveraging Vercel's infrastructure provides a scalable service.


# Japanese
## プロジェクト概要

このプロジェクトは、ユーザーがGoogleアカウントでログインし、指定したGoogle Drive内のPDFファイルを自動的に取り込み、OCR処理を行うウェブアプリケーションです。処理結果はウェブ上で閲覧・編集が可能であり、CSV形式でのダウンロードもサポートしています。

## 主な機能

### ユーザー認証
- Googleアカウントを使用したOAuth 2.0ベースのログイン機能
- 他のログイン方法は提供していません

### Google Drive連携
- ユーザーが自身のGoogle Driveからフォルダを選択
- 選択したフォルダにアップロードされたPDFファイルを自動的にVercelのストレージに取り込み

### PDF管理
- 取り込んだPDFファイルの一覧表示（ファイル名、アップロード日時、処理ステータス）
- 各PDFファイルのOCR結果とPDFプレビューの同時表示および編集

### OCR結果の管理
- OCR処理結果の編集および保存機能
- 複数ファイルのOCR結果をCSV形式で一括ダウンロード

## 技術スタック

- **フロントエンド:** Next.js（Vercel）、TypeScript
- **バックエンド:** Next.jsのAPIルート、Vercelのデータベースサービス
- **認証:** Google OAuth 2.0
- **OCR処理:** Vercel上のストレージを使用

## 非機能要件

- **パフォーマンス:** 各ページのレスポンスタイムは3秒以内を維持
- **セキュリティ:** ユーザーデータの暗号化とアクセス制限の実装
- **ユーザビリティ:** 直感的でレスポンシブなユーザーインターフェース

## プロジェクトの目的

このプロジェクトは、ユーザーが効率的にPDFファイルを管理し、OCR処理を行うことで、データの閲覧・編集およびエクスポートを容易にすることを目的としています。Google Driveとの連携により、ファイル管理が簡便になり、Vercelのインフラを活用してスケーラブルなサービスを提供します。
