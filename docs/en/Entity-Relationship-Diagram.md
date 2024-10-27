## Table Structure


### User
| Field Name | Data Type |
|--------------|----------|
| userID       | string   |
| googleID     | string   |
| name         | string   |
| email        | string   |
| createdAt    | datetime |

### Folder
| Field Name      | Data Type |
|-------------------|----------|
| folderID          | string   |
| userID            | string   |
| googleFolderID    | string   |
| folderName        | string   |
| createdAt         | datetime |

### PDFFile

| Field Name   | Data Type |
|----------------|----------|
| pdfID          | string   |
| folderID       | string   |
| googleFileID   | string   |
| fileName       | string   |
| uploadedAt     | datetime |
| status         | string   |

### OCRResult

| Field Name  | Data Type |
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