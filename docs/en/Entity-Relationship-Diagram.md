## Table Structure

### User
| Field Name | Data Type |
|--------------|----------|
| userID       | String   |
| googleID     | String   |
| Name         | String   |
| Email        | String   |
| Creation Date Time    | Date Time |

### Folder
| Field Name      | Data Type |
|-------------------|----------|
| folderID          | String   |
| userID            | String   |
| googleFolderID    | String   |
| Folder Name        | String   |
| Creation Date Time         | Date Time |

### PDF File

| Field Name   | Data Type |
|----------------|----------|
| pdfID          | String   |
| folderID       | String   |
| googleFileID   | String   |
| File Name       | String   |
| Upload Date Time | Date Time |
| Status             | String   |

### OCR Result

| Field Name  | Data Type |
|---------------|----------|
| ocrResultID   | String   |
| pdfID         | String   |
| Content           | Text |
| Update Date Time     | Date Time |



# ER Diagram
```mermaid
erDiagram
    User {
        String userID
        String googleID
        String Name
        String Email
        Date Time Creation Date Time
    }

    Folder {
        String folderID
        String userID
        String googleFolderID
        String Folder Name
        Date Time Creation Date Time
    }

    PDF File {
        String pdfID
        String folderID
        String googleFileID
        String File Name
        Date Time Upload Date Time
        String Status
    }

    OCR Result {
        String ocrResultID
        String pdfID
        Text Content
        Date Time Update Date Time
    }

    User ||--o{ Folder : Owns
    Folder ||--o{ PDF File : Contains
    PDF File ||--|| OCR Result : Has
```