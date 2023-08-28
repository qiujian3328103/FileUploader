# File Uploader with PyQt5

This application provides a graphical user interface for users to easily select files from their system and upload them to S3. Built with PyQt5, the application supports functionalities like drag-and-drop file inputs, multi-threaded processing to ensure UI responsiveness, and detailed feedback through a spinner during processing.

## Features

- **Drag and Drop**: Users can simply drag files and drop them onto the app to select them for upload.
- **Multi-File Selection**: Supports selection of multiple files at once.
- **Configurable S3 Settings**: Allows users to specify S3 URL, Secret Key, and Bucket Name.
- **Multithreading**: Uses multi-threading to process files, ensuring the UI remains responsive.
- **Feedback**: Provides feedback to the user with a waiting spinner during file processing.

## Installation and Setup

1. Clone the repository:

2. Navigate to the project directory:

## Usage

1. Open the application.
2. Navigate to the `File` tab to drag and drop or select files for upload.
3. Move to the `Settings` tab to configure your S3 details.
4. Once files are selected and settings are configured, hit the `Upload` button to process the files.

## Dependencies

- PyQt5
- (Any other libraries or dependencies used, like `QtWaitingSpinner`)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)