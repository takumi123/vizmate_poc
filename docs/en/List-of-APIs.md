# API Design
## 1. User Authentication API
- **Endpoint:** `/api/auth/google`
- **Method:** GET
- **Description:** Initiates Google OAuth authentication and redirects the user to the Google authentication screen.
- **Request Parameters:** None
- **Response:**
  - **Success:** Redirect to Google's authentication screen
  - **Error:** Returns an appropriate error message.

## 2. Folder List Retrieval API
- **Endpoint:** `/api/folders`
- **Method:** GET
- **Description:** Retrieves a list of folders from the user's Google Drive.
- **Request Parameters:** None
- **Response:**
  - **Success:**
    ```json
    {
      "folders": [
        {
          "id": "folderId1",
          "name": "Folder Name 1",
          "createdAt": "2023-10-01T12:00:00Z"
        },
        {
          "id": "folderId2",
          "name": "Folder Name 2",
          "createdAt": "2023-10-02T15:30:00Z"
        }
      ]
    }
    ```
  - **Error:** Returns an error message.

## 3. Folder Selection API
- **Endpoint:** `/api/folders/select`
- **Method:** POST
- **Description:** Selects a folder for OCR processing.
- **Request Parameters:**
  - `folderId` (string): The ID of the folder to be selected
    ```json
    {
      "folderId": "Selected Folder ID"
    }
    ```
- **Response:**
  - **Success:**
    ```json
    {
      "message": "The folder has been selected successfully.",
      "folderId": "Selected Folder ID"
    }
    ```
  - **Error:** Returns an error message.

## 4. PDF List Retrieval API
- **Endpoint:** `/api/pdfs`
- **Method:** GET
- **Description:** Retrieves a list of PDF files in the selected folder.
- **Request Parameters:** None
- **Response:**
  - **Success:**
    ```json
    {
      "pdfs": [
        {
          "id": "pdfId1",
          "name": "File Name 1.pdf",
          "uploadedAt": "2023-10-03T10:00:00Z",
          "status": "Processing Complete"
        },
        {
          "id": "pdfId2",
          "name": "File Name 2.pdf",
          "uploadedAt": "2023-10-04T11:30:00Z",
          "status": "Processing"
        }
      ]
    }
    ```
  - **Error:** Returns an error message.

## 5. OCR Result Retrieval API
- **Endpoint:** `/api/ocr/:pdfId`
- **Method:** GET
- **Description:** Retrieves the OCR result of a specific PDF file.
- **Request Parameters:**
  - `pdfId` (string): The ID of the PDF file to retrieve the OCR result
- **Response:**
  - **Success:**
    ```json
    {
      "pdfId": "pdfId1",
      "content": "Text content extracted by OCR"
    }
    ```
  - **Error:** Returns an error message.

## 6. OCR Result Update API
- **Endpoint:** `/api/ocr/:pdfId`
- **Method:** PUT
- **Description:** Updates the OCR result.
- **Request Parameters:**
  - `pdfId` (string): The ID of the PDF file to update the OCR result
  - Body:
    ```json
    {
      "content": "Updated OCR text content"
    }
    ```
- **Response:**
  - **Success:**
    ```json
    {
      "message": "The OCR result has been updated successfully.",
      "pdfId": "pdfId1"
    }
    ```
  - **Error:** Returns an error message.

## 7. CSV Export API
- **Endpoint:** `/api/export/csv`
- **Method:** GET
- **Description:** Exports all OCR results in CSV format.
- **Request Parameters:** None
- **Response:**
  - **Success:** Downloads a CSV file.
  - **Error:** Returns an error message.