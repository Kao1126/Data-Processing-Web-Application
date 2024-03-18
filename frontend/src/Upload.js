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
 <div className="container mt-5">
      <h2>Bootstrap File Upload</h2>
      <div className="input-group mb-3">
        <div className="custom-file">
          <input type="file" className="custom-file-input" id="inputGroupFile" onChange={handleFileChange} />
          <label className="custom-file-label" htmlFor="inputGroupFile">
            {selectedFile ? selectedFile.name : 'Choose file'}
          </label>
        </div>
        <div className="input-group-append">
          <button className="btn btn-primary" type="button" onClick={handleUpload}>Upload</button>
        </div>
      </div>
    </div>
  );

  return (
    <div class="Continer">
      <h2>File Upload</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
  
}

export default FileUpload;
