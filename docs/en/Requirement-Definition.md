## Document
https://japan-marketing-co-jp.gitbook.io/bizmate/

---

# Requirements Specification

## 1. Introduction
This document is a requirements specification for the development of a web application for an OCR service. In this service, users log in with their Google account, automatically import PDF files from a specified Google Drive, and perform OCR processing. The processing results can be viewed and edited on the web, and can also be downloaded in CSV format.

## 2. System Overview
**Platform:** Web Application  
**Technology Stack:**  
- Front-end: Next.js (Vercel), TypeScript
- Back-end, Database, Storage: Vercel
- User Authentication: Only Google login

## 3. Functional Requirements

### 3.1 User Authentication
- Google login feature
- Login with Google account using OAuth 2.0
- No other login methods are provided

### 3.2 Google Drive Integration
- **Google Drive Selection:**  
  After logging in, the user selects a folder from Google Drive
- **PDF Data Import:**  
  Automatically import PDF files uploaded to the selected folder and save them in Vercel's storage  
  Import in real-time if there are new uploads

### 3.3 Display PDF List
- **Display PDF File List:**  
  Display imported PDF files in list format  
  Display information such as file name, upload date, and processing status

### 3.4 Display OCR Results
- **Simultaneous Display of OCR Results and PDF:**  
  In the detail screen, display the OCR results on the left and the PDF preview on the right  
  OCR results can be edited in a text area

### 3.5 OCR Detail Screen
- **Save Function:**  
  Confirm and save OCR results with the "Save" button
- **Navigation:**  
  Place "Next" and "Back" buttons in the header to facilitate movement to other files

### 3.6 CSV Download
- **Export OCR Results:**  
  Download all OCR results in CSV format  
  Provide a download button

## 4. Non-functional Requirements

### 4.1 Performance
- **Response Time:**  
  Page transitions and data loading should be completed within 3 seconds
- **Simultaneous Access:**  
  Maintain performance even when multiple users are using the service simultaneously

### 4.2 Security
- **Data Protection:**  
  User data is stored encrypted
- **Access Restrictions:**  
  Restrict access to data for each user

### 4.3 Usability
- **Intuitive UI:**  
  Design that allows even first-time users to operate without hesitation
- **Responsive Design:**  
  Compatible with access from PCs, tablets, and smartphones

## 5. System Configuration

### 5.1 Front-end
- **Next.js:**  
  Fast page display by server-side rendering
- **TypeScript:**  
  Safe code writing by type definition

### 5.2 Back-end
- **API Routes:**  
  Implementation of server-side processing using Next.js's API routes
- **Database & Storage:**  
  Use of database services provided by Vercel

### 5.3 Integration of External Services
- **Google API:**  
  Access files using Google Drive API  
  Implement authentication and authorization with Google OAuth 2.0

## 6. User Interface Details

### 6.1 Login Screen
- **Google Login Button:**  
  Redirects to Google's authentication screen when clicked

### 6.2 Folder Selection Screen
- **Display Google Drive Folder List:**  
  Select a folder from the user's drive

### 6.3 PDF List Screen
- **File List:**  
  Display thumbnail, file name, and status
- **Operation:**  
  Clicking on a file navigates to the detail screen

### 6.4 OCR Detail Screen
- **Display Area:**  
  Left: OCR result text area (editable)  
  Right: PDF preview
- **Operation Buttons:**  
  Place "Next", "Back", and "Save" buttons in the header

### 6.5 CSV Download Screen
- **Download Button:**  
  Click to generate and download a CSV file
- **Progress Display:**  
  Display a progress bar during the download process

## 7. Error Handling
- **Authentication Error:**  
  Display an appropriate error message if login fails
- **File Retrieval Error:**  
  Provide a retry option if file retrieval from Google Drive fails
- **Save Error:**  
  Notify the user and prompt for data resubmission if saving OCR results fails

## 8. Logs and Monitoring
- **Access Logs:**  
  Record user access conditions as logs
- **Error Logs:**  
  Record system errors and exceptions for debugging
- **Monitoring:**  
  Monitor the operation status of the system in real time

## 9. Security Requirements
- **HTTPS Communication:**  
  Encrypt all communications with SSL/TLS
- **Data Encryption:**  
  Apply encryption to stored data
- **Permission Management:**