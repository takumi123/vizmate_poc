## Document
https://japan-marketing-co-jp.gitbook.io/bizmate/

---

# Requirements Specification Document

## 1. Introduction
This document is a requirements specification for the development of a web application for OCR services. This service allows users to log in with their Google account, automatically import PDF files from a specified Google Drive, and perform OCR processing. The processing results can be viewed and edited on the web, and can also be downloaded in CSV format.

## 2. System Overview
**Platform:** Web Application  
**Technology Stack:**  
- Frontend: Next.js (Vercel), TypeScript
- Backend, Database, Storage: Vercel
- User Authentication: Google login only

## 3. Functional Requirements

### 3.1 User Authentication
- Google login feature
- Login with Google account using OAuth 2.0
- No other login methods are provided


### 3.2 Google Drive Integration
- **Google Drive Selection:**  
  After logging in, the user selects a folder from their Google Drive
- **PDF Data Import:**  
  Automatically import PDF files uploaded to the selected folder and save them in Vercel's storage  
  Import in real-time when a new upload is made

### 3.3 PDF List Display
- **PDF File List Display:**  
  Display imported PDF files in a list format  
  Display information such as file name, upload date, processing status, etc.

### 3.4 OCR Result Display
- **Simultaneous Display of OCR Results and PDF:**  
  In the detail screen, display the OCR results on the left and the PDF preview on the right  
  OCR results can be edited in a text area

### 3.5 OCR Detail Screen
- **Save Feature:**  
  Confirm and save OCR results with the "Save" button
- **Navigation:**  
  Place "Next" and "Back" buttons in the header to facilitate movement to other files

### 3.6 CSV Download
- **OCR Result Export:**  
  Bulk download of all OCR results in CSV format  
  Provide a download button

## 4. Non-Functional Requirements

### 4.1 Performance
- **Response Time:**  
  Page transitions and data loads are completed within 3 seconds
- **Simultaneous Access:**  
  Maintain performance even when multiple users are using the service simultaneously

### 4.2 Security
- **Data Protection:**  
  User data is stored encrypted
- **Access Restriction:**  
  Restrict access to data for each user

### 4.3 Usability
- **Intuitive UI:**  
  Design that allows even first-time users to operate without hesitation
- **Responsive Design:**  
  Compatible with access from PCs, tablets, and smartphones

## 5. System Configuration

### 5.1 Frontend
- **Next.js:**  
  Fast page display with server-side rendering
- **TypeScript:**  
  Safe code writing with type definitions

### 5.2 Backend
- **API Routes:**  
  Implement server-side processing using Next.js API routes
- **Database & Storage:**  
  Use the database service provided on Vercel

### 5.3 External Service Integration
- **Google API:**  
  Access files using Google Drive API  
  Implement authentication and authorization with Google OAuth 2.0

## 6. User Interface Details

### 6.1 Login Screen
- **Google Login Button:**  
  Redirect to Google's authentication screen when clicked

### 6.2 Folder Selection Screen
- **Google Drive Folder List Display:**  
  Select a folder from the user's Drive

### 6.3 PDF List Screen
- **File List:**  
  Display thumbnail, file name, status
- **Operation:**  
  Click on the file to transition to the detail screen

### 6.4 OCR Detail Screen
- **Display Area:**  
  Left side: OCR result text area (editable)  
  Right side: PDF preview
- **Operation Buttons:**  
  Place "Next", "Back", and "Save" buttons in the header

### 6.5 CSV Download Screen
- **Download Button:**  
  Generate and download a CSV file when clicked
- **Progress Display:**  
  Display a progress bar during download processing

## 7. Error Handling
- **Authentication Error:**  
  Display appropriate error messages when login fails
- **File Retrieval Error:**  
  If file retrieval from Google Drive fails, offer a retry option
- **Save Error:**  
  If saving OCR results fails, notify the user and prompt for data resubmission

## 8. Logs and Monitoring
- **Access Logs:**  
  Record user access conditions as logs
- **Error Logs:**  
  Record system errors and exceptions for debugging
- **Monitoring:**  
  Monitor the system's operating status in real time

## 9. Security Requirements
- **HTTPS Communication:**  
  Encrypt all communications with SSL/TLS
- **Data Encryption:**  
  Apply encryption to stored data
- **Permission Management:**  
  Implement data access control for each user

## 10. Constraints
- **Google Account Required:**  
  A Google account is required to use the service
- **Vercel Resources:**  
  Only use features that can be completed on Vercel
- **File Format:**  
  Only PDF files are supported

## 11. Development Environment
- **Development Language:**  
  TypeScript
- **Framework:**  
  Next.js
- **Hosting:**  
  Vercel

## 12. Risks and Countermeasures
- **Google API Limitations:**  
  Countermeasure: Check API usage limits and design to avoid exceeding them
- **Data Security:**  
  Countermeasure: Thoroughly implement data encryption and access control