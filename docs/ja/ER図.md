
## テーブル構造

### User table

| フィールド名 | データ型 |
|--------------|----------|
| userID       | string   |
| googleID     | string   |
| name         | string   |
| email        | string   |
| createdAt    | datetime |

### Folder

| フィールド名      | データ型 |
|-------------------|----------|
| folderID          | string   |
| userID            | string   |
| googleFolderID    | string   |
| folderName        | string   |
| createdAt         | datetime |

### PDFFile

| フィールド名   | データ型 |
|----------------|----------|
| pdfID          | string   |
| folderID       | string   |
| googleFileID   | string   |
| fileName       | string   |
| uploadedAt     | datetime |
| status         | string   |

### OCRResult

| フィールド名  | データ型 |
|---------------|----------|
| ocrResultID   | string   |
| pdfID         | string   |
| content       | text     |
| updatedAt     | datetime |



# ER Diagram
```mermaid
erDiagram
    User {
        string userID
        string googleID
        string name
        string email
        datetime createdAt
    }

    Folder {
        string folderID
        string userID
        string googleFolderID
        string folderName
        datetime createdAt
    }

    PDFFile {
        string pdfID
        string folderID
        string googleFileID
        string fileName
        datetime uploadedAt
        string status
    }

    OCRResult {
        string ocrResultID
        string pdfID
        text content
        datetime updatedAt
    }

    User ||--o{ Folder : owns
    Folder ||--o{ PDFFile : contains
    PDFFile ||--|| OCRResult : has
```
