## Table Structure

### User
| Field Name | Data Type |
|--------------|----------|
| userID       | String   |
| googleID     | String   |
| Name         | String   |
| Email        | String   |
| Created At   | DateTime |


### Folder
| Field Name      | Data Type |
|-------------------|----------|
| folderID          | String   |
| userID            | String   |
| googleFolderID    | String   |
| Folder Name       | String   |
| Created At        | DateTime |

### PDF File

| Field Name   | Data Type |
|----------------|----------|
| pdfID          | String   |
| folderID       | String   |
| googleFileID   | String   |
| File Name      | String   |
| Uploaded At    | DateTime |
| Status         | String   |

### OCR Result

| Field Name  | Data Type |
|---------------|----------|
| ocrResultID   | String   |
| pdfID         | String   |
| Content       | Text     |
| Updated At    | DateTime |



# ER Diagram
```mermaid
erDiagram
    User {
        String userID
        String googleID
        String Name
        String Email
        DateTime Created At
    }

    Folder {
        String folderID
        String userID
        String googleFolderID
        String Folder Name
        DateTime Created At
    }

    PDF File {
        String pdfID
        String folderID
        String googleFileID
        String File Name
        DateTime Uploaded At
        String Status
    }

    OCR Result {
        String ocrResultID
        String pdfID
        Text Content
        DateTime Updated At
    }

    User ||--o{ Folder : Owns
    Folder ||--o{ PDF File : Contains
    PDF File ||--|| OCR Result : Has
```