# React Component Design

## Component Description
1. **App**: The root component of the application
2. **Layout**: A component that provides a common layout
   - Header: Displays the header section
   - Footer: Displays the footer section
   - Main Content: The main content area

3. **Page Components**:
   - LoginPage: Login screen
   - FolderSelectionPage: Google Drive folder selection screen
   - PDFListPage: PDF file list screen
   - OCRDetailPage: OCR result detail and editing screen
   - CSVDownloadPage: CSV download screen

4. **Reusable Components**:
   - PDFListItem: Displays each item in the PDF list
   - OCRTextEditor: Component for editing OCR text
   - PDFViewer: Component for previewing PDFs
   - NavigationButtons: "Next" and "Back" navigation buttons

## State Management

- Global states (user information, selected folders, etc.) are managed using React Context or Redux
- Local states (form inputs, temporary UI states, etc.) use the React useState hook

## Data Fetching

- If server-side rendering is necessary, use Next.js's getServerSideProps
- For client-side data fetching, use React Query to optimize caching and refetching

## Error Handling

- Create a global error handling component to catch and display errors throughout the application

## Accessibility

- Use semantic HTML elements
- Properly set ARIA attributes
- Support keyboard navigation