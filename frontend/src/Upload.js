import React, { useState } from 'react';

function FileUpload() {
  const [selectedFile, setSelectedFile] = useState(null);

  // Function to handle file selection
  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  // Function to handle file upload
  const handleUpload = () => {
    if (selectedFile) {
      // You can send the selected file to your backend or process it here
      console.log("Selected file:", selectedFile);
    } else {
      alert("Please select a file to upload");
    }
  };

  return (
    <div class="Continer">
      <h2>File Upload</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default FileUpload;
